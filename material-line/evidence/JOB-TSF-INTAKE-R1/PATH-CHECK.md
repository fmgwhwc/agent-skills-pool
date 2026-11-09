# PATH-CHECK — JOB-TSF-INTAKE-R1

| 字段 | 值 |
|---|---|
| checked_at | 2026-11-09 Asia/Shanghai |
| method | `gh api repos/<owner>/<repo>/contents/<path>` |
| ref | default branch `main`（pin_pending） |
| scope | disposition ∈ {adapt, adapt_secondary, hold_license} |

## Results

| id | repo | path | EXISTS | blob sha (contents) | size | html_url |
|---|---|---|---|---|---:|---|
| C01 | moonlight-lupin/agent-skills | productivity/travel-itinerary/SKILL.md | **YES** | `51a73421672ccf61aae032e1503ea8fabc686258` | 13210 | https://github.com/moonlight-lupin/agent-skills/blob/main/productivity/travel-itinerary/SKILL.md |
| C02 | jeffreytse/grimoire-core | skills/travel/planning/skills/design-trip-itinerary/SKILL.md | **YES** | `41d9e46d57ed5cb34621fae6e93eeb3d79039ac4` | 4112 | https://github.com/jeffreytse/grimoire-core/blob/main/skills/travel/planning/skills/design-trip-itinerary/SKILL.md |
| C03 | AtlasOmnia/donna-starter | skills/productivity/destination-trip-planning/SKILL.md | **YES** | `3813bd1e58c92e2b1b402f6e95be3ca03f999ec1` | 9475 | https://github.com/AtlasOmnia/donna-starter/blob/main/skills/productivity/destination-trip-planning/SKILL.md |
| C04 | pjt222/agent-almanac | skills/plan-hiking-tour/SKILL.md | **YES** | `4292c121ad8e491d4e61ff1d387fbed8b721a73a` | 19422 | https://github.com/pjt222/agent-almanac/blob/main/skills/plan-hiking-tour/SKILL.md |
| C06 | clawic/skills | skills/photography/SKILL.md | **YES** | `c096c61e01665c8895a70503345ec4821a7c4402` | 4523 | https://github.com/clawic/skills/blob/main/skills/photography/SKILL.md |
| C07 | makaronz/skilslsls | landscape-photography/SKILL.md | **YES** | `749bf95d2d3cb5b3c8a517f125f6e9760f52ab2d` | 8238 | https://github.com/makaronz/skilslsls/blob/main/landscape-photography/SKILL.md |
| C08 | FerroxLabs/murage | skills-library/food-tourism-planner/SKILL.md | **YES** | `9f77820ca84cfd211ba23410c6580959c0185d85` | 49098 | https://github.com/FerroxLabs/murage/blob/main/skills-library/food-tourism-planner/SKILL.md |
| C09 | FerroxLabs/murage | skills-library/international-cuisine-explorer/SKILL.md | **YES** | `9f0f82592cc4682f7257191d627b94f98a9f763d` | 16718 | https://github.com/FerroxLabs/murage/blob/main/skills-library/international-cuisine-explorer/SKILL.md |
| C10 | hwspen7/PoreiaGo | plugins/skills/culinary-specialty-discovery/SKILL.md | **YES** | `5822268b42743c7fda2fd84970c013c2d2cf1a98` | 2835 | https://github.com/hwspen7/PoreiaGo/blob/main/plugins/skills/culinary-specialty-discovery/SKILL.md |

## main HEAD (observed at check；未写入 meta 冻结 pin)

| repo | main SHA |
|---|---|
| moonlight-lupin/agent-skills | `ceacc13d2bbc98d9dea5cbabcb4f44e4c7fd14a9` |
| jeffreytse/grimoire-core | `7ff5861b00836cb0d675c00a09a26d143722579e` |
| AtlasOmnia/donna-starter | `b6eaf1bab0527daab22ad02043fcd7c9869d0323` |
| pjt222/agent-almanac | `ce87dce34c9e6ff9621cb597af3ea3be10d49f3c` |
| clawic/skills | `f825206afbf1c697202533a9187be68c7b697e0e` |
| makaronz/skilslsls | `f2d8e7b86fb4b5b2bebd32e8a657285fa62977d3` |
| FerroxLabs/murage | `f28a6bad8ecc9c370bd42d9aa9e6a7c361163d54` |
| hwspen7/PoreiaGo | `76d5e2171b302594ad0ae83d9b36d513c4b7ac44` |

## Verdict

**PASS** — 全部建议 ADAPT / adapt_secondary / HOLD 条目路径 EXISTS。hold_queue / reject 条目本轮未强制二次 API 抽查。
