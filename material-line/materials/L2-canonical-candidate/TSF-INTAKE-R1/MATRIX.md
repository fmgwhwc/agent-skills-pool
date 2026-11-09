# TSF-INTAKE-R1 — 候选 × 12 能力格

图例：`●` 主映射（score≥3 或队列 grid 主格）· `○` 次映射 · `·` 无 · `H` HOLD（许可/队列）· `R` reject/weak

格点：

```text
T-plan T-navigate T-source T-retro
S-scout S-shoot-card S-rights-exif S-select
F-shortlist F-order-note F-allergen-hours F-taste-vs-fact
```

| id | T-plan | T-nav | T-src | T-retro | S-scout | S-shoot | S-rights | S-select | F-short | F-order | F-aller | F-taste | disposition |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| C01 | ● | ● | · | · | · | · | · | · | · | · | · | · | adapt |
| C02 | ● | · | · | · | · | · | · | · | · | · | · | · | adapt_secondary |
| C03 | ● | · | ● | · | · | · | · | · | · | · | · | · | adapt_secondary |
| C04 | ○ | · | · | · | ● | · | · | · | · | · | · | · | adapt_secondary |
| C05 | · | ● | · | · | · | · | · | · | · | · | · | · | hold_queue |
| C06 | · | · | · | · | · | ● | · | ○ | · | · | · | · | adapt |
| C07 | · | · | · | · | ● | ● | · | ○ | · | · | · | · | adapt |
| C08 | ○ | · | · | · | · | · | · | · | ● | ○ | ○ | ○ | hold_license **H** |
| C09 | · | · | · | · | · | · | · | · | ● | · | · | ○ | hold_license **H** |
| C10 | · | · | · | · | · | · | · | · | ● | · | · | ● | adapt |
| C11 | · | · | · | · | · | · | · | · | · | · | · | ○ | weak_fit |
| C12 | ● | · | · | · | · | · | · | · | · | · | · | · | duplicate_like |
| C13 | ● | · | · | · | · | · | · | · | · | · | · | · | hold_queue |
| C14 | ● | · | · | · | · | · | · | · | · | · | · | · | hold_queue |
| C15 | ● | · | · | · | · | · | · | · | · | · | · | · | hold_queue |
| C16 | ● | · | · | · | · | · | · | · | · | · | · | · | duplicate_like |
| C17 | ● | · | · | · | · | · | · | · | · | · | · | · | duplicate_like |
| C18 | · | · | · | · | · | ● | · | · | · | · | · | · | duplicate_like |
| C19 | · | · | · | · | · | ● | · | · | · | · | · | · | hold_queue |
| C20 | · | · | · | · | · | · | · | · | ○ | · | · | · | reject_narrow **R** |
| C21 | · | · | · | · | · | R | · | · | · | · | · | · | reject **R** |
| C22 | · | R | · | · | · | · | · | · | · | · | · | · | reject **R** |
| C23 | R | · | · | · | · | · | · | · | · | · | · | · | reject **R** |
| C24 | · | · | · | · | · | · | · | · | · | · | · | ○ | weak_fit |
| C25 | ● | · | · | · | · | · | · | · | · | · | · | · | hold_queue |

## Fermin 覆盖（本轮 candidate）

| Fermin skill | 主格 | 填补 |
|---|---|---|
| fermin-tsf-itinerary-structure | T-plan, T-navigate | T-source（约束澄清） |
| fermin-tsf-landscape-shoot | S-shoot-card, S-scout | S-rights-exif（默认 UNKNOWN） |
| fermin-tsf-food-discovery | F-shortlist, F-taste-vs-fact | F-allergen-hours（未知则 UNKNOWN） |

未覆盖优先格（下轮候选，不扩墙硬凑）：T-retro、S-select、F-order-note。
