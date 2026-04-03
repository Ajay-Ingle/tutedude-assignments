---
description: How to capture and save terminal screenshots for assignment submissions
---

# Screenshot Capture Workflow

## When to Capture
- After running each required command from the assignment
- When the assignment explicitly asks for "screenshot proof"
- When showing output of a script execution

## How to Capture
1. Run the command in the terminal using `run_command`
2. Use the `browser_subagent` to open a page showing the terminal output, or capture the terminal window
3. Save screenshots with descriptive names like `task1-docker-ps.png`

## Naming Convention
Use this format: `task<number>-<brief-description>.png`
Examples:
- `task1-git-clone.png`
- `task2-docker-build.png`
- `task3-kubectl-get-pods.png`

## Organization
- All screenshots go into the assignment's `screenshots/` folder
- Reference them in `notes.md` with relative paths
