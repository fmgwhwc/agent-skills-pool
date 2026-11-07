# Catalog lint note

- entry_id: toy-entry
- check_name: name_matches_dir
- observed: frontmatter name `Foo_Bar`
- expected: kebab-case equal to directory `toy-entry` (e.g. `toy-entry`)
- severity: error
- next_action: Edit `toy-entry/SKILL.md` frontmatter `name` to `toy-entry`; re-run static name check.
- skill_status_reminder: candidate
