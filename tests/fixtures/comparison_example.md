```yaml
units_total: 12
units_covered: 7
facts_total: 30
facts_matched: 14
facts_conflicting: 2
fabricated: 0
depth_back_original: 5
depth_back_repro: 6
depth_forward_original: 4
depth_forward_repro: 4
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
| D04 | Export prices to the next buyer country | 앞쪽 | 8–9 |

The original was split into 12 units by the points where its topic changes; four rows are shown here as a sample. Counted over all 12 rows, 5 are 뒤쪽 and 4 are 앞쪽. [observed]

## 2. Correspondence

| Original unit | Reproduced paragraph | Reproduction direction | Result | Basis |
|---|---|---|---|---|
| D01 | 2 | 뒤쪽 | covered | The same collapse and the same causation toward mackerel. [observed] |
| D02 | - | - | not covered | The reproduction names mackerel only as a species, not the switch of fleets. [observed] |
| D03 | 4 | 본 주제 | covered | The same quota cut and the same deciding body. [observed] |
| D04 | - | - | not covered | The reproduction gives no export price. [observed] |

Extra units (links of the reproduction that fill no original unit):

| Paragraph | Name | Direction |
|---|---|---|
| 1 | Herring stock survey | 뒤쪽 |
| 9 | Next quota meeting | 앞쪽 |
| 10 | Canning plants' order book | 앞쪽 |

Rows are a sample. Over all reproduction units (covered rows plus extra units), 6 are 뒤쪽 and 4 are 앞쪽. [observed]

## 3. Facts

| Original value | Reproduced value | Result |
|---|---|---|
| image: 「어획량 추이 그래프」 | image: 「어획량 추이 그래프」 | same; `image:` line under R01 names S04, which states the series [observed] |
| 「최대 수출국」 | 「최대 수출국」 | same; the qualifier is in S07 [observed] |
| 「쿼터 21% 감축」 | 「쿼터 21% 감축」 | same [observed] |
| 「1977년 금어」 | 「1976년 금어」 | different [observed] |
| 「냉동공장 12곳」 | - | absent [observed] |

## 4. Depth

Backward, the original has 5 units and the reproduction 6: it adds a step on the herring stock survey that the original does not have. [observed] Forward, both have 4 units; the reproduction replaces the export-price step with the next quota meeting. [observed]

## 5. Fabrication list

Image descriptions and qualifiers were checked first: each placeholder has an `image:` line with ids that state it, and each qualifier reaches a quotation. [observed] None: every number, name, date and event in the reproduced post reaches a quotation or a source in `research.md`. [observed]

## 6. Contact check

`log.md` records no page on an `excluded_domains:` address and no source dated after `date:`; one `[접촉]` was closed after a date check. [observed]

## 7. Overall opinion

The reproduction found the main topic and went as far as the original in both directions, but it missed the fleet switch and added three links the original does not have. [inferred]

## 8. Failure routing

- D02 (not covered): `research-method.md` has a rule to ask what changed for the people who depended on the collapsed resource (layer B), and `log.md` shows no search for it → reproduction. [observed]
- D04 (not covered): no rule in `research-method.md` leads from a quota cut to the buyer countries' prices → method extraction, layer F. [observed]
- Depth: neither direction is below the original's. [observed]

Method extraction: layer F needs a rule that follows a supply cut to the prices the buyers pay (D04).
Reproduction: run the layer-B question on who depended on the collapsed stock (D02).
