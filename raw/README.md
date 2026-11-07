# raw/ — upstream skill archives (R3 pins)

Immutable local copies of upstream OSS Agent Skills trees at the R3-verified SHAs, so curated `pool/` entries can always map back to unmodified originals.

## Purpose

- Provenance: re-clean / re-ADAPT against the exact bytes that were researched.
- Crosswalk: `INDEX.yaml` links each released `pool/skills/<id>` `source` / `adapted_from` path to a file under `sources/`.
- **Not** a fork or mirror of upstream repos. **Not** loadable runtime skills — loaders and validators use `pool/` only.

## Pins are frozen

Each directory under `sources/` is keyed by `owner__repo__<sha12>` at a full commit SHA recorded in that directory’s `SOURCE.yaml`.

- Never mutate an existing snapshot.
- New upstream versions → add a new `sources/<…__newsha>/` directory.

## License

Each snapshot includes the upstream license file(s). Redistribution follows the SPDX recorded in `SOURCE.yaml` / `INDEX.yaml`. Anthropic document skills (`docx` / `pdf` / `pptx` / `xlsx`) are **excluded** (source-available, not open source).

## Layout

```text
raw/
├── README.md
├── INDEX.yaml              # sources[] + links[] crosswalk to pool/
└── sources/
    └── <owner>__<repo>__<sha12>/
        ├── SOURCE.yaml
        ├── LICENSE         # (or equivalent notice)
        └── <upstream paths preserved>
```

## Related

- Curated packages: [`pool/skills/`](../pool/skills/)
- Rejected notes: [`rejected/`](../rejected/)
- Attribution: [`ATTRIBUTION.md`](../ATTRIBUTION.md)
