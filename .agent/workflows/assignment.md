---
description: How to complete a TuteDude DevOps assignment step-by-step
---

# TuteDude DevOps Assignment Workflow

Follow these steps when the user pastes an assignment task:

## 1. Analyze the Assignment
- Read the full assignment description carefully
- Identify each task/question that needs to be completed
- Create a checklist of all deliverables (commands to run, screenshots needed, files to create, etc.)
- Create a task.md artifact tracking every item

## 2. Set Up the Assignment Folder
- Create a folder under the workspace root named after the assignment (e.g., `assignment-1-linux-basics/`)
- Inside, create subfolders as needed:
  - `screenshots/` — for terminal screenshots
  - `scripts/` — for any shell scripts or config files
  - `notes.md` — for written answers or explanations

## 3. Execute Tasks
- For each command-based task:
  // turbo-all
  - Run the command in the terminal
  - Capture a screenshot of the terminal output using the browser tool
  - Save the screenshot to the assignment's `screenshots/` folder
- For explanation-based tasks:
  - Write clear, concise answers in `notes.md`
- For file/script-based tasks:
  - Create the required files in the `scripts/` folder

## 4. Document Everything
- Update `notes.md` with:
  - Assignment title and date
  - Each task number, the command used, and a brief explanation
  - References to screenshot filenames
- Create a summary artifact showing completion status

## 5. Prepare for Submission
- Verify all screenshots are captured
- Verify all scripts are created and working
- Review `notes.md` for completeness
- Stage and commit to git with a descriptive message
