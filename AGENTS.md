# Agent Instructions

## Bootstrap (required)

Before your first command in this workspace, run:

\`\`\`sh
bun run .claude/setup.mjs
\`\`\`

It is idempotent and prepares the shared toolchain for all agents. If \`bun\`
is not on PATH, use \`node .claude/setup.mjs\`.

## Conventions

- Execute shell work through the environment configured by \`.claude/settings.json\`; its hooks are part of the managed infrastructure.
- Do not edit, rename or delete files under \`.claude/\` unless explicitly asked to do so.
