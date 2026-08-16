<!--
Draft artifact for human review.
Target repository: GC-STEM/it140-m4-assignment
Draft date: 2026-08-15
-->

# IT 140 Module Four Assignment

- **Course**: IT 140 - Introduction to Scripting
- **Activity**: Module Four Assignment
- **Design problem**: Higher/Lower Game
- **Graded deliverable**: `design/hilow_game.pseudo`

**Assignment progress:** **0 Start Here** → [1 Analyze](analysis/README.md) → [2 Design](design/README.md) → [3 Construct (Practice)](src/README.md) → [4 Test (Practice)](tests/README.md) → [5 Submit](#submit-your-assignment)

## Start With the Assignment Guidelines and Rubric

Before using this repository, open the **Module Four Assignment Guidelines and Rubric** in [D2L Brightspace](https://learn.snhu.edu/).

Review the complete assignment, including:

- Overview
- Scenario
- Prompt
- Higher/Lower Game Sample Output
- Pseudocode requirements
- What to Submit
- AI Usage
- Assignment Rubric

The **Module Four Assignment Guidelines and Rubric** is the official source for assignment requirements, grading criteria, and submission requirements. The **Higher/Lower Game Sample Output** is an official supporting resource for understanding expected program behavior. This repository provides starter files, reference documents, working files, and step-by-step guidance to help you complete those requirements.

> [!IMPORTANT]
> This assignment is graded on the **pseudocode** you create in `design/hilow_game.pseudo`. Writing and testing a Python program is **optional practice** and is not a graded deliverable for this assignment.

After reviewing the Guidelines and Rubric and Sample Output, return here to set up your personal assignment repository.

## About This Repository

This repository organizes the assignment around a simplified Software Development Life Cycle (SDLC):

> **Analyze → Design → Construct → Test**

For the graded assignment, you will Analyze the problem and Design the solution as pseudocode. After your pseudocode is complete, you are encouraged to continue through Construct and Test for additional programming practice.

Module Four adds **loops** to concepts you have already practiced, including input/output and decision branching. The higher/lower game combines these concepts in one design.

> [!NOTE]
> The Codio Virtual Desktop (CVD) is the reference environment for IT 140. If you completed the [Module One Setup Tasks](https://github.com/GC-STEM/it140-m1-setup-tasks) and use the CVD for this course, Git, GitHub CLI, VS Code, pseudocode support, Python, and the expected course repository configuration should already be available. We recommend all students use the CVD for coursework to minimize environment differences and troubleshooting issues.
>
> You may also complete this assignment on a supported local computer configured through the Module One Setup Tasks. Local environments can vary, so some commands or troubleshooting steps may differ.

You will create your own personal GitHub repository from this course repository template and clone your repository to the CVD or your supported local computer. Your personal repository lets you:

- Complete your assignment work
- Save changes with Git
- Push your work to GitHub for backup
- Continue working from your own copy of the assignment
- Practice a professional repository-based development workflow

The main assignment folders are:

```text
it140-m4-assignment/
├── analysis/
│   ├── README.md
│   └── hilow_game_srs.md
├── design/
│   ├── README.md
│   ├── hilow_game.pseudo
│   └── hilow_game_sdd.md
├── src/
│   ├── README.md
│   └── hilow_game.py
├── tests/
│   ├── README.md
│   └── test_hilow_game.py
├── hilow_game_sdw.md
└── README.md
```

### What You May Edit

Your required assignment work should be limited to:

- [`design/hilow_game.pseudo`](design/hilow_game.pseudo) — **graded pseudocode deliverable**

You may also edit these working or practice files:

- [`hilow_game_sdw.md`](hilow_game_sdw.md) — recommended Software Development Worksheet (SDW) notes; not submitted for grading
- [`src/hilow_game.py`](src/hilow_game.py) — optional Python construction practice; not submitted for grading

Leave the READMEs, SRS, SDD, tests, repository configuration, and other provided files unchanged unless your instructor or course instructions tell you otherwise.

## Set Up Your Personal Assignment Repository

Complete these steps only once before beginning the assignment.

If you already created an `it140-m4-assignment` repository in your GitHub account or already have an `it140-m4-assignment` folder in `~/Repos`, do not repeat these setup steps. Open your existing repository instead.

If you need to start over, see [Reset Your Assignment Repository](#reset-your-assignment-repository).

### 1. Open the VS Code Integrated Terminal

In VS Code, select:

> **Terminal > New Terminal**

You will use the integrated terminal in VS Code to create and clone your personal assignment repository.

> [!IMPORTANT]
> Windows users must use a **PowerShell** or **Git Bash** terminal in VS Code to run the commands in this file. A Command Prompt (`cmd.exe`) terminal will not work.

### 2. Confirm Your GitHub Account

1. Type the following command in the VS Code integrated terminal:

   ```bash
   gh auth status
   ```

2. Review the results and identify the active account.
   - If your IT 140 GitHub account is listed but is not active, continue to Step 2.3.
   - If your IT 140 GitHub account is not listed, continue to Step 2.4.
   - If the correct IT 140 GitHub account is active, continue to Step 3.

3. If your IT 140 GitHub account is listed but is not active, type the following command, replacing `your-github-username` with your GitHub username:

   ```bash
   gh auth switch --user your-github-username
   ```

   Then return to Step 2.1 to confirm that the correct account is now active.

4. If your IT 140 GitHub account is not listed, type:

   ```bash
   gh auth login --web
   ```

   Follow the GitHub CLI prompts and sign in with the GitHub account you use for IT 140.

5. When sign-in is complete, return to Step 2.1 and check your account again.

6. Continue to Step 3 - Create and Clone Your Personal Repository.

### 3. Create and Clone Your Personal Repository

The following command block will:

1. Go to your course `Repos` folder.
2. Configure Git to use your GitHub CLI authentication.
3. Star the original IT 140 assignment repository so it is easier to find again.
4. Create your personal assignment repository in GitHub from the current course template.
5. Make your personal repository private.
6. Clone your new repository to your CVD or local computer.
7. Enter the cloned repository folder.
8. Show the GitHub repository connected to your local copy.

Copy the entire command block and paste it into the VS Code integrated terminal:

```bash
cd ~/Repos
gh auth setup-git
gh api --method PUT /user/starred/GC-STEM/it140-m4-assignment
gh repo create it140-m4-assignment --template GC-STEM/it140-m4-assignment --private --clone
cd it140-m4-assignment
git remote -v
```

Review the final output and confirm that the repository belongs to your GitHub account.

If a command reports an error, do not repeat the entire command block. Review the error message and use the [Help and Support](#help-and-support) resources before continuing.

### 4. Open Your Assignment Repository in VS Code

In VS Code:

1. Select **File > Open Folder**.
2. Open `~/Repos/it140-m4-assignment`.
3. Confirm that `it140-m4-assignment` is the top-level folder shown in the Explorer.

You are now working in your personal copy of the Module Four Assignment.

## Complete the Assignment

### 1. Analyze the Requirements

Open the [Analyze Phase instructions](analysis/README.md).

Use the assignment Guidelines and Rubric, the Higher/Lower Game Sample Output, the provided Software Requirements Specification (SRS), and the optional SDW to make sure you understand:

- The lower-bound and upper-bound inputs
- How invalid bounds must be handled
- How the secret number is selected
- The player's guess input and its validation
- The three possible guess results: too low, too high, or correct
- Why the game must repeat until the correct number is guessed

Do not begin by writing Python code. The purpose of this assignment is to practice designing the solution before constructing it.

### 2. Create the Graded Pseudocode

Open the [Design Phase instructions](design/README.md).

Complete:

[`design/hilow_game.pseudo`](design/hilow_game.pseudo)

Your pseudocode should logically describe the complete game, including input/output, validation, decision branching, and loops. Review it against the assignment Guidelines and Rubric before continuing.

### 3. Optional Practice: Construct the Python Program

After your graded pseudocode is complete, you are encouraged to continue to the [Construct Phase](src/README.md).

Use your own completed pseudocode as the plan for completing `src/hilow_game.py`. This practice helps connect program design to working Python code.

This file is **not required for the Module Four Assignment grade**.

### 4. Optional Practice: Test the Python Program

If you complete the optional Python program, continue to the [Test Phase](tests/README.md).

Use the official sample-output scenarios, additional manual cases, and the provided optional practice tests to check your implementation.

Testing is **not required for the Module Four Assignment grade**, but it provides practice with the full SDLC and helps you see whether the pseudocode design can be implemented successfully.

### 5. Save Your Work to GitHub

Save your files normally while you work in VS Code.

Periodically commit and push your assignment work so your personal GitHub repository contains a current backup. From the repository root in the VS Code integrated terminal, run:

```bash
cd ~/Repos/it140-m4-assignment
git status
git add design/hilow_game.pseudo hilow_game_sdw.md src/hilow_game.py
git commit -m "Save Module Four assignment progress"
git push
```

Git ignores unchanged files, so including optional files in the `git add` command does not create extra work if you did not edit them.

> [!NOTE]
> GitHub is a backup and version-control tool for this assignment. **D2L Brightspace remains the assignment submission, grading, and feedback system.**

## Submit Your Assignment

Before submitting, return to the **Module Four Assignment Guidelines and Rubric** in D2L Brightspace and verify the current submission requirements.

The graded deliverable identified by the provided assignment is:

- `design/hilow_game.pseudo`

### Final Check

- [ ] I completed the pseudocode in `design/hilow_game.pseudo`.
- [ ] My pseudocode logically outlines the required game steps.
- [ ] My pseudocode identifies the required inputs and outputs.
- [ ] My pseudocode validates the lower and upper bounds.
- [ ] My pseudocode validates guesses against the selected bounds.
- [ ] My pseudocode uses decision branching for too-low, too-high, and correct guesses.
- [ ] My pseudocode uses loops so the game continues as required.
- [ ] I reviewed the Higher/Lower Game Sample Output.
- [ ] I reviewed the current Module Four Assignment Guidelines and Rubric.
- [ ] I saved my `.pseudo` file before submitting it.

Submit the `.pseudo` file in **D2L Brightspace** according to the current assignment instructions.

The optional SDW, Python file, and tests are not graded deliverables unless your instructor specifically tells you otherwise.

## Reset Your Assignment Repository

Use this only if you intentionally want to discard your current local and GitHub copies and start again from the current course template.

> [!CAUTION]
> Starting over can permanently discard work that exists only in your current repository. Save any work you need before resetting.

1. Delete or rename the local `~/Repos/it140-m4-assignment` folder.
2. Delete the personal `it140-m4-assignment` repository from your GitHub account if you intend to reuse the same name.
3. Return to [Create and Clone Your Personal Repository](#3-create-and-clone-your-personal-repository).

Do not reuse an assignment repository from an earlier course attempt. Creating a repository from the current course template ensures that you receive the current assignment files and instructions.

## Help and Support

Start with the [Module Four Assignment Wiki](https://github.com/GC-STEM/it140-m4-assignment/wiki) for supplemental explanations and common questions.

Use the repository's [Issues](https://github.com/GC-STEM/it140-m4-assignment/issues) area for a reproducible technical problem with the repository, starter files, or repository instructions.

Use the repository's [Discussions](https://github.com/GC-STEM/it140-m4-assignment/discussions) area for repository-related questions that may help other students.

Do **not** ask for or post a completed pseudocode solution. Ask for explanations or resources that help you discover the solution yourself.

Post questions about course content that are not specific to this repository in your section's **General Questions** discussion topic.

Contact your instructor through the course-approved D2L Brightspace channel for questions related to:

- Assignment submissions
- Grading
- Rubric feedback
- Deadlines
- Accommodations
- Your individual work
