```yaml
units_total: 12
units_covered: 7
facts_total: 30
facts_matched: 14
facts_conflicting: 2
fabricated: 0
depth_original: 9
depth_repro: 6
extra_units: 3
invalid: 0
profile_hash: ab12cd34ef56
```

# Comparison: mackerel post (repro 2)

## 1. Development of the original

| Dxx | Name | Direction | Paragraphs |
|---|---|---|---|
| D01 | Herring collapse in the North Sea | 뒤쪽 | 1–2 |
| D02 | Fishing fleets switch to mackerel | 뒤쪽 | 3–4 |
| D03 | This year's quota cut | 본 주제 | 5–7 |

The original was split into 12 units by the points where its topic changes; three rows are shown here as a sample. [observed]

## 2. Correspondence

| Original unit | Reproduced paragraph | Result | Basis |
|---|---|---|---|
| D01 | 2 | covered | The same collapse and the same causation toward mackerel. [observed] |
| D02 | - | not covered | The reproduction names mackerel only as a species, not the switch of fleets. [observed] |
| D03 | 4 | covered | The same quota cut and the same deciding body. [observed] |

## 3. Facts

| Original value | Reproduced value | Result |
|---|---|---|
| 「쿼터 21% 감축」 | 「쿼터 21% 감축」 | same [observed] |
| 「1977년 금어」 | 「1976년 금어」 | different [observed] |
| 「냉동공장 12곳」 | - | absent [observed] |

## 4. Depth

The original goes four steps back to the herring collapse; the reproduction stops two steps back at the fleet change. [observed] Forward, the reproduction goes one step further than the original, to the next quota meeting. [observed]

## 5. Fabrication list

None: every number, name, date and event in the reproduced post reaches a quotation or a source in `research.md`. [observed]

## 6. Contact check

`log.md` records no page on an `excluded_domains:` address and no source dated after `date:`; one `[접촉]` was closed after a date check. [observed]

## 7. Overall opinion

The reproduction found the main topic and most of the backward chain but stopped short of the oldest cause, and it added three forward links the original does not have. [inferred]
