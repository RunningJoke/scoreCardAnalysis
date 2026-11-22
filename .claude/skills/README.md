# Project skills

Each skill is a folder with a `SKILL.md`:

```
.claude/skills/<skill-name>/SKILL.md
```

`SKILL.md` starts with frontmatter (`name`, `description`). The description says when the skill applies; Claude Code reads it to decide when to load the skill. Supporting scripts or reference files go next to it in the same folder.

Candidates once the pipeline exists: parse a new score sheet, run the weekly rating update, write a scouting report for a named opponent.
