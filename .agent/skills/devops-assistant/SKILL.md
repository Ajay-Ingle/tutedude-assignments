---
name: DevOps Assignment Assistant
description: Analyzes TuteDude DevOps assignments, breaks them into actionable tasks, executes commands, captures screenshots, and prepares submission-ready deliverables.
---

# DevOps Assignment Assistant

## Purpose
This skill helps complete TuteDude online course DevOps assignments by:
- Parsing assignment descriptions into structured task lists
- Running required terminal commands (Linux, Docker, Kubernetes, Git, CI/CD, etc.)
- Capturing terminal output and screenshots as proof of completion
- Writing explanations and documentation
- Organizing deliverables for submission

## How to Use

### Step 1: Receive the Assignment
The user will paste the full assignment text. Parse it to identify:
- **Command tasks**: Commands to execute and screenshot
- **Script tasks**: Shell scripts, Dockerfiles, YAML configs to create
- **Explanation tasks**: Written answers or concept explanations
- **Setup tasks**: Environment setup, installations, configurations

### Step 2: Create Task Breakdown
Create a `task.md` artifact with a checklist of every deliverable. Group by task number.

### Step 3: Execute Sequentially
Work through each task:

#### For Command Tasks
1. Run the command using `run_command`
2. Note the output
3. If a screenshot is needed, inform the user to capture manually OR use browser tools
4. Log the command and output in the assignment's `notes.md`

#### For Script/Config Tasks
1. Create the file in the assignment's `scripts/` folder
2. Make it executable if needed (`chmod +x`)
3. Run it to verify it works
4. Capture output

#### For Explanation Tasks
1. Write clear, accurate, and concise answers
2. Include relevant examples where helpful
3. Add to `notes.md`

### Step 4: Verify & Submit
- Cross-check every task against the assignment requirements
- Ensure all screenshots are present and clearly labeled
- Commit all files to git

## DevOps Topics Covered
This skill supports assignments across common DevOps topics:
- **Linux Fundamentals**: File system, permissions, processes, shell scripting
- **Version Control**: Git commands, branching, merging, GitHub workflows
- **Containers**: Docker build, run, compose, networking, volumes
- **Orchestration**: Kubernetes pods, deployments, services, ingress
- **CI/CD**: Jenkins, GitHub Actions, GitLab CI pipelines
- **Infrastructure as Code**: Terraform, Ansible, CloudFormation
- **Monitoring**: Prometheus, Grafana, ELK stack
- **Cloud Platforms**: AWS, GCP, Azure basics
- **Networking**: DNS, HTTP, TCP/IP, firewalls, load balancers

## Output Format
For each assignment, produce:
```
assignment-X-<topic>/
├── screenshots/
│   ├── task1-<description>.png
│   ├── task2-<description>.png
│   └── ...
├── scripts/
│   ├── script1.sh
│   ├── Dockerfile
│   └── ...
└── notes.md          # Full documentation with answers
```

## Important Notes
- Always explain **what** a command does and **why** it's used
- Use the `// turbo-all` annotation in workflows for safe auto-execution
- If a tool/package is not installed, guide the user through installation
- For Windows users: use PowerShell or WSL as appropriate
- Flag any tasks that require cloud accounts or paid services
