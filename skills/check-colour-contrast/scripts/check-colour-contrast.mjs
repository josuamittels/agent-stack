#!/usr/bin/env node

const formats = new Set(['hex', 'rgb', 'hsl']);
const usage = "Usage: node check-colour-contrast.mjs <format> '<foreground>' <format> '<background>'\nFormats: hex, rgb, hsl";

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
    return [(n >> 16) / 255, ((n >> 8) & 255) / 255, (n & 255) / 255];
  }

  const functionName = format === 'rgb' ? 'rgb' : 'hsl';
  value = value.replace(new RegExp(`^${functionName}\\s*\\(`, 'i'), '').replace(/\)\s*$/, '');
  const parts = value.replace(/,/g, ' ').trim().split(/\s+/).filter(Boolean);
  if (parts.length !== 3) throw new Error(`${format} requires three channels`);
  const channels = parts.map((part) => {
    const match = part.match(/^([+-]?(?:\d+\.?\d*|\.\d+))(deg|%)?$/i);
    if (!match) throw new Error(`invalid ${format} channel: ${part}`);
    return { value: Number(match[1]), unit: (match[2] || '').toLowerCase() };
  });

  if (format === 'rgb') {
    return channels.map(({ value: channel, unit }) => {
      if (unit !== '' && unit !== '%') throw new Error('RGB channels use numbers or percentages');
      const normalized = unit === '%' ? channel / 100 : channel / 255;
      if (normalized < 0 || normalized > 1) throw new Error('RGB channels must be between 0 and 255, or 0% and 100%');
      return normalized;
    });
  }

  if (channels[0].unit === '%') throw new Error('HSL hue must be an angle, not a percentage');
  if (channels[0].unit !== '' && channels[0].unit !== 'deg') throw new Error('HSL hue must be in degrees');
  const hue = ((channels[0].value % 360) + 360) % 360;
  const saturation = normalizeHslChannel(channels[1]);
  const lightness = normalizeHslChannel(channels[2]);
  return hslToRgb(hue, saturation, lightness);
}

function normalizeHslChannel({ value, unit }) {
  if (unit === 'deg') throw new Error('HSL saturation and lightness cannot use angle units');
  const normalized = unit === '%' || value > 1 ? value / 100 : value;
  if (normalized < 0 || normalized > 1) throw new Error('HSL saturation and lightness must be between 0 and 1, or 0% and 100%');
  return normalized;
}

function hslToRgb(hue, saturation, lightness) {
  const chroma = (1 - Math.abs(2 * lightness - 1)) * saturation;
  const section = hue / 60;
  const x = chroma * (1 - Math.abs((section % 2) - 1));
  const rgb = section < 1 ? [chroma, x, 0]
    : section < 2 ? [x, chroma, 0]
      : section < 3 ? [0, chroma, x]
        : section < 4 ? [0, x, chroma]
          : section < 5 ? [x, 0, chroma]
            : [chroma, 0, x];
  const match = lightness - chroma / 2;
  return rgb.map((channel) => channel + match);
}

function relativeLuminance(rgb) {
  const [r, g, b] = rgb.map((channel) => channel <= 0.04045 ? channel / 12.92 : ((channel + 0.055) / 1.055) ** 2.4);
  return 0.2126 * r + 0.7152 * g + 0.0722 * b;
}

function contrastRatio(first, second) {
  const a = relativeLuminance(first);
  const b = relativeLuminance(second);
  return (Math.max(a, b) + 0.05) / (Math.min(a, b) + 0.05);
}

function status(ratio, threshold) { return ratio >= threshold ? 'PASS' : 'FAIL'; }

const args = process.argv.slice(2);
if (args.length !== 4) fail('Provide a format and value for each color.');
const [foregroundFormat, foregroundValue, backgroundFormat, backgroundValue] = args;
if (!formats.has(foregroundFormat)) fail(`Unsupported foreground format: ${foregroundFormat}`);
if (!formats.has(backgroundFormat)) fail(`Unsupported background format: ${backgroundFormat}`);

try {
  const foreground = parseColor(foregroundFormat, foregroundValue);
  const background = parseColor(backgroundFormat, backgroundValue);
  const ratio = contrastRatio(foreground, background);
  console.log(`Contrast ratio: ${ratio.toFixed(3)}:1`);
  console.log(`WCAG AA normal text (4.5:1): ${status(ratio, 4.5)}`);
  console.log(`WCAG AAA normal text (7:1): ${status(ratio, 7)}`);
  console.log(`WCAG AA large text (3:1): ${status(ratio, 3)}`);
  console.log(`WCAG AAA large text (4.5:1): ${status(ratio, 4.5)}`);
  console.log(`WCAG AA non-text UI/graphics (3:1): ${status(ratio, 3)}`);
} catch (error) {
  fail(error.message);
}
