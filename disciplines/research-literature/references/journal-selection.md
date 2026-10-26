---
name: "journal-selection"
description: "Evidence and CSV calibration behind Research Literature's journal-influence presets."
version: "0.2.0"
updated: "2026-10-26"
author:
  - "Josua Mittelstaedt"
references:
  - "Clarivate"
  - "Elsevier"
  - "DORA"
type: "reference"
status: "draft"
---

# Journal-selection rationale

Consult this reference when explaining or revisiting the journal-selection presets. The [discipline](../SKILL.md#journal-selection) owns the operational cutoffs and eligibility rules. Evidence was checked on 2026-10-26.

## Why use these cutoffs?

The user selected the three presets: lenient uses Article Influence at least 1.0 or percentile at least 60, default uses 2.5 or 80, and strict uses 5.0 or 90. These are user-defined selection thresholds, rather than externally validated quality standards. Article Influence is a different metric from Journal Impact Factor. An Article Influence cutoff of 5.0 does not mean Impact Factor at least 5.

Clarivate defines Article Influence with an article-level mean of 1.00 across its network. This gives context for the absolute cutoffs. It does not mean that the unweighted mean of journal scores is 1.0. See [Clarivate's Journal Profile, Other Metrics](https://journalcitationreports.zendesk.com/hc/en-gb/articles/28351430970001-Journal-Profile).

The percentile bounds express upper-40%, upper-20%, and upper-10% selection bands on the supplied percentile scale. Scopus offers quartile filters and a top-10% filter, which provides precedent for percentile-based venue selection. Its CiteScore percentiles do not establish the meaning or provenance of this CSV's `influence_percentile`. See [Scopus Sources filtering](https://www.elsevier.support/scopus/answer/how-do-i-use-the-scopus-sources-feature).

OR admits journals through either supplied metric. This preserves journals that meet the percentile threshold despite a lower absolute score, and journals with a qualifying absolute score despite a lower or unavailable percentile. It does not guarantee that the retained set is exactly a named percentile band. Higher cutoffs on both metrics make the three eligible sets nested.

Journal influence describes a venue. It does not validate an individual paper's methods or conclusions. Retain source-level appraisal throughout Research. See the [DORA Declaration](https://sfdora.org/read/).

## Calibration against the supplied CSV

The [CSV](journals.csv) contains 30,991 category rows, 21,996 distinct combinations of print ISSN, electronic ISSN, and journal title, and 21,995 distinct titles. Using any qualifying category row and the discipline's inclusive OR rule gives:

| Selection | Eligible journal identities | Share of all identities |
| --- | ---: | ---: |
| Lenient | 7,309 | 33.2% |
| Default | 3,241 | 14.7% |
| Strict | 1,536 | 7.0% |

These counts describe the supplied snapshot without a category restriction. They are not counts of matched OpenAlex sources, relevant works, or individual studies retained. ISSN normalization and identity resolution can also affect live search counts.

Article Influence is missing in 1,298 rows. Percentile is missing in 13 rows. Thirteen journal identities have neither score. Available values range from 0 to 80.147 for Article Influence and 0 to 99.9 for percentile. Article Influence is constant within each inspected journal identity. Percentile varies across categories for two identities, ACCESS-Access to science business innovation in the digital economy and ACS Environmental Au. Preserve category rows and treat zero as a valid value.

To reproduce the counts from the repository root with an available Python interpreter:

```python
import csv
import math
from collections import defaultdict

groups = defaultdict(list)
with open("disciplines/research-literature/references/journals.csv",
          encoding="utf-8-sig", newline="") as source:
    for row in csv.DictReader(source):
        groups[row["issn_print"], row["issn_online"], row["journal"]].append(row)

def passes(raw, cutoff, maximum=math.inf):
    try:
        value = float(raw)
    except (TypeError, ValueError):
        return False
    return math.isfinite(value) and 0 <= value <= maximum and value >= cutoff

for name, absolute, percentile in [
    ("lenient", 1.0, 60), ("default", 2.5, 80), ("strict", 5.0, 90)
]:
    count = sum(any(passes(row["article_influence"], absolute)
                    or passes(row["influence_percentile"], percentile, 100)
                    for row in rows) for rows in groups.values())
    print(name, count, f"{count / len(groups):.1%}")
```

## Snapshot and interpretation limits

The CSV has no explicit metric year or percentile derivation. Do not describe its scores as current-year rankings, substitute another percentile metric, or infer exact field normalization. `inception` describes journal inception, not the metric year. Use the supplied values as the agreed selection policy, and disclose their provenance limits.

Coverage favors venues represented in the CSV and successfully matched to OpenAlex. Missing scores or matches establish unknown eligibility rather than low quality. Record these exclusions separately and honor explicit numeric overrides or requests to disable filtering. Broader coverage requires an explicit selection change rather than silent relaxation after sparse results.
