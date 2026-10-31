#!/usr/bin/env node

const formats = new Set(['hex', 'rgb', 'hsl', 'hsv', 'cmyk', 'lab', 'lch', 'p3']);
const usage = 'Usage: node convert-colour.mjs <input-format> <value> <output-format>\nFormats: hex, rgb, hsl, hsv, cmyk, lab, lch, p3';

function fail(message) {
  console.error(`${message}\n${usage}`);
  process.exit(2);
}

function parseColor(format, source) {
  let value = source.trim();
  if (format === 'hex') {
    value = value.replace(/^#/, '');
    if (/^[0-9a-f]{3}$/i.test(value)) value = [...value].map((c) => c + c).join('');
    if (!/^[0-9a-f]{6}$/i.test(value)) throw new Error('hex requires #RGB or #RRGGBB');
    const n = Number.parseInt(value, 16);
    return srgbToXyz([(n >> 16) / 255, ((n >> 8) & 255) / 255, (n & 255) / 255]);
  }

  value = value.replace(/^\s*(?:rgb|hsl|hsv|cmyk|lab|lch)\s*\(/i, '').replace(/\)\s*$/, '');
  value = value.replace(/^\s*color\(\s*display-p3\s+/i, '').replace(/\)\s*$/, '');
  const parts = value.replace(/,/g, ' ').trim().split(/\s+/).filter(Boolean);
  const expectedChannels = format === 'cmyk' ? 4 : 3;
  if (parts.length !== expectedChannels) throw new Error(`provide ${expectedChannels} channel${expectedChannels === 1 ? '' : 's'}`);
  const nums = parts.map((part) => {
    const number = Number.parseFloat(part.replace(/%$/, ''));
    if (!Number.isFinite(number)) throw new Error(`invalid channel: ${part}`);
    return { number, percent: part.endsWith('%') };
  });
  const c = nums.map(({ number, percent }) => ({ number: percent ? number / 100 : number, percent }));

  switch (format) {
    case 'rgb': {
      const rgb = c.slice(0, 3).map(({ number, percent }) => percent ? number : number / 255);
      return srgbToXyz(rgb);
    }
    case 'p3': {
      const p3 = c.slice(0, 3).map(({ number, percent }) => percent ? number : number);
      return p3ToXyz(p3);
    }
    case 'hsl':
      if (c[0].percent) throw new Error('hsl hue must be an angle, not a percentage');
      return srgbToXyz(hslToRgb(c[0].number, c[1].number, c[2].number));
    case 'hsv':
      if (c[0].percent) throw new Error('hsv hue must be an angle, not a percentage');
      return srgbToXyz(hsvToRgb(c[0].number, c[1].number, c[2].number));
    case 'cmyk': {
      // Use the conventional algebraic RGB/CMYK model; print profiles require separate ICC data.
      const [cyan, magenta, yellow, key] = nums.map(({ number }) => number / 100);
      return srgbToXyz([(1 - cyan) * (1 - key), (1 - magenta) * (1 - key), (1 - yellow) * (1 - key)]);
    }
    case 'lab': return labToXyzD65(
      c[0].percent ? c[0].number * 100 : c[0].number,
      c[1].percent ? c[1].number * 125 : c[1].number,
      c[2].percent ? c[2].number * 125 : c[2].number,
    );
    case 'lch': {
      if (c[2].percent) throw new Error('lch hue must be an angle, not a percentage');
      const angle = c[2].number * Math.PI / 180;
      const lightness = c[0].percent ? c[0].number * 100 : c[0].number;
      const chroma = c[1].percent ? c[1].number * 150 : c[1].number;
      return labToXyzD65(lightness, chroma * Math.cos(angle), chroma * Math.sin(angle));
    }
    default: throw new Error(`unsupported input format: ${format}`);
  }
}

function formatColor(format, xyz) {
  switch (format) {
    case 'hex': {
      const rgb = xyzToSrgb(xyz).map(clamp01).map((v) => Math.round(v * 255));
      return `#${rgb.map((v) => v.toString(16).padStart(2, '0')).join('')}`;
    }
    case 'rgb': {
      const rgb = xyzToSrgb(xyz).map(clamp01).map((v) => Math.round(v * 255));
      return `rgb(${rgb.join(' ')})`;
    }
    case 'hsl': {
      const [h, s, l] = rgbToHsl(xyzToSrgb(xyz).map(clamp01));
      return `hsl(${round(h, 2)}deg ${round(s * 100, 2)}% ${round(l * 100, 2)}%)`;
    }
    case 'hsv': {
      const [h, s, v] = rgbToHsv(xyzToSrgb(xyz).map(clamp01));
      return `hsv(${round(h, 2)}deg ${round(s * 100, 2)}% ${round(v * 100, 2)}%)`;
    }
    case 'cmyk': {
      const [r, g, b] = xyzToSrgb(xyz).map(clamp01);
      const k = 1 - Math.max(r, g, b);
      const values = k >= 1 ? [0, 0, 0, 1] : [(1 - r - k) / (1 - k), (1 - g - k) / (1 - k), (1 - b - k) / (1 - k), k];
      return `cmyk(${values.map((v) => `${round(v * 100, 2)}%`).join(' ')})`;
    }
    case 'lab': {
      const [l, a, b] = xyzD50ToLab(xyzD65ToD50(xyz));
      return `lab(${round(l, 4)} ${round(a, 4)} ${round(b, 4)})`;
    }
    case 'lch': {
      const [l, a, b] = xyzD50ToLab(xyzD65ToD50(xyz));
      const chroma = Math.hypot(a, b);
      const hue = chroma <= 0.0015 ? 0 : (Math.atan2(b, a) * 180 / Math.PI + 360) % 360;
      return `lch(${round(l, 4)} ${round(chroma, 4)} ${round(hue, 4)}deg)`;
    }
    case 'p3': {
      const rgb = xyzToP3(xyz);
      return `color(display-p3 ${rgb.map((v) => round(v, 6)).join(' ')})`;
    }
    default: throw new Error(`unsupported output format: ${format}`);
  }
}

function srgbToXyz(rgb) {
  const [r, g, b] = rgb.map(decodeSrgb);
  return multiply([
    [0.4123907992659595, 0.357584339383878, 0.1804807884018343],
    [0.2126390058715104, 0.715168678767756, 0.0721923153607337],
    [0.0193308187155919, 0.119194779794626, 0.9505321522496607],
  ], [r, g, b]);
}

function xyzToSrgb(xyz) {
  const linear = multiply([
    [3.2409699419045226, -1.537383177570094, -0.4986107602930034],
    [-0.9692436362808796, 1.8759675015077202, 0.04155505740717559],
    [0.05563007969699366, -0.20397695888897652, 1.0569715142428786],
  ], xyz);
  return linear.map(encodeSrgb);
}

function p3ToXyz(rgb) {
  const [r, g, b] = rgb.map(decodeSrgb);
  return multiply([
    [0.4865709486482162, 0.26566769316909306, 0.1982172852343625],
    [0.2289745640697488, 0.6917385218365064, 0.079286914093745],
    [0, 0.04511338185890264, 1.043944368900976],
  ], [r, g, b]);
}

function xyzToP3(xyz) {
  const linear = multiply([
    [2.493496911941425, -0.9313836179191239, -0.40271078445071684],
    [-0.8294889695615747, 1.7626640603183463, 0.023624685841943577],
    [0.03584583024378447, -0.07617238926804182, 0.9568845240076872],
  ], xyz);
  return linear.map(encodeSrgb);
}

function labToXyzD65(l, a, b) {
  const fy = (l + 16) / 116;
  const fx = fy + a / 500;
  const fz = fy - b / 200;
  const delta = 6 / 29;
  const inverse = (t) => t > delta ? t ** 3 : 3 * delta ** 2 * (t - 4 / 29);
  const d50 = [0.96422 * inverse(fx), inverse(fy), 0.82521 * inverse(fz)];
  return xyzD50ToD65(d50);
}

function xyzD50ToLab([x, y, z]) {
  const delta = 6 / 29;
  const f = (t) => t > delta ** 3 ? Math.cbrt(t) : t / (3 * delta ** 2) + 4 / 29;
  const fx = f(x / 0.96422);
  const fy = f(y);
  const fz = f(z / 0.82521);
  return [116 * fy - 16, 500 * (fx - fy), 200 * (fy - fz)];
}

function xyzD65ToD50(xyz) {
  return multiply([
    [1.0479298208405488, 0.022946793341019088, -0.05019222954313557],
    [0.029627815688159344, 0.990434484573249, -0.01707382502938514],
    [-0.009243058152591178, 0.015055144896577895, 0.7518742814281371],
  ], xyz);
}

function xyzD50ToD65(xyz) {
  return multiply([
    [0.9554734527042182, -0.023098536874261423, 0.0632593086610217],
    [-0.028369706963208136, 1.0099954580058226, 0.021041398966943008],
    [0.012314001688319899, -0.020507696433477912, 1.3303659366080753],
  ], xyz);
}

function decodeSrgb(v) { return v <= 0.04045 ? v / 12.92 : ((v + 0.055) / 1.055) ** 2.4; }
function encodeSrgb(v) { return v <= 0.0031308 ? 12.92 * v : 1.055 * Math.sign(v) * Math.abs(v) ** (1 / 2.4) - 0.055; }
function multiply(matrix, vector) { return matrix.map((row) => row.reduce((sum, value, i) => sum + value * vector[i], 0)); }
function clamp01(v) { return Math.max(0, Math.min(1, v)); }
function round(v, places) { const factor = 10 ** places; return Math.round((v + Number.EPSILON) * factor) / factor; }

function hueToRgb(p, q, t) {
  if (t < 0) t += 1;
  if (t > 1) t -= 1;
  if (t < 1 / 6) return p + (q - p) * 6 * t;
  if (t < 1 / 2) return q;
  if (t < 2 / 3) return p + (q - p) * (2 / 3 - t) * 6;
  return p;
}

function hslToRgb(h, s, l) {
  h = ((h % 360) + 360) % 360 / 360;
  if (s > 1) s /= 100;
  if (l > 1) l /= 100;
  if (s === 0) return [l, l, l];
  const q = l < 0.5 ? l * (1 + s) : l + s - l * s;
  const p = 2 * l - q;
  return [hueToRgb(p, q, h + 1 / 3), hueToRgb(p, q, h), hueToRgb(p, q, h - 1 / 3)];
}

function hsvToRgb(h, s, v) {
  h = ((h % 360) + 360) % 360;
  if (s > 1) s /= 100;
  if (v > 1) v /= 100;
  const chroma = v * s;
  const x = chroma * (1 - Math.abs((h / 60) % 2 - 1));
  const m = v - chroma;
  const sector = Math.floor(h / 60);
  const rgb = sector === 0 ? [chroma, x, 0] : sector === 1 ? [x, chroma, 0] : sector === 2 ? [0, chroma, x] : sector === 3 ? [0, x, chroma] : sector === 4 ? [x, 0, chroma] : [chroma, 0, x];
  return rgb.map((channel) => channel + m);
}

function rgbToHsl([r, g, b]) {
  const max = Math.max(r, g, b), min = Math.min(r, g, b), delta = max - min;
  let h = 0;
  const l = (max + min) / 2;
  let s = 0;
  if (delta !== 0) {
    s = delta / (1 - Math.abs(2 * l - 1));
    if (max === r) h = 60 * (((g - b) / delta) % 6);
    else if (max === g) h = 60 * ((b - r) / delta + 2);
    else h = 60 * ((r - g) / delta + 4);
  }
  return [((h % 360) + 360) % 360, s, l];
}

function rgbToHsv([r, g, b]) {
  const max = Math.max(r, g, b), min = Math.min(r, g, b), delta = max - min;
  let h = 0;
  if (delta !== 0) {
    if (max === r) h = 60 * (((g - b) / delta) % 6);
    else if (max === g) h = 60 * ((b - r) / delta + 2);
    else h = 60 * ((r - g) / delta + 4);
  }
  return [((h % 360) + 360) % 360, max === 0 ? 0 : delta / max, max];
}

const [inputFormat, ...rest] = process.argv.slice(2);
if (!inputFormat || rest.length < 2) fail('Provide an input format, value, and output format.');
const outputFormat = rest.pop();
const value = rest.join(' ');
if (!formats.has(inputFormat)) fail(`Unsupported input format: ${inputFormat}`);
if (!formats.has(outputFormat)) fail(`Unsupported output format: ${outputFormat}`);

try {
  console.log(formatColor(outputFormat, parseColor(inputFormat, value)));
} catch (error) {
  fail(error.message);
}
