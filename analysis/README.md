<!-- To see this file in a clean, formatted view, right-click on the filename and choose "Open Preview." -->

# Analyze Phase | Understand the Higher/Lower Game Requirements

**Required assignment progress:** [0 Start Here](../README.md) → **1 Analyze** → [2 Design](../design/README.md) → [3 Submit](../README.md#3-submit-your-assignment)

**Optional SDLC practice after Design:** [Construct](../src/README.md) → [Test](../tests/README.md)

## Purpose

During the Analyze phase, your goal is to understand **what the Higher/Lower Game must do** before deciding how to express the solution in pseudocode.

The **Module Four Assignment Guidelines and Rubric in D2L Brightspace** is the official source for assignment requirements. The official **Higher/Lower Game Sample Output** provides examples of program behavior. The provided [Software Requirements Specification (SRS)](hilow_game_srs.md) reorganizes the stated requirements into a software-development format so you can examine them systematically.

The Analyze phase does not create a graded deliverable. It prepares you to create the graded pseudocode during Design.

## Deliverable

**This phase does not produce a graded or submitted file.**

You may record brief working notes in the [Software Development Worksheet (SDW)](../hilow_game_sdw.md). The SDW is a learning aid and is not submitted unless your instructor specifically asks for it.

## What You Will Use

Use these materials:

- **Module Four Assignment Guidelines and Rubric** in D2L Brightspace — official assignment and grading requirements
- **Higher/Lower Game Sample Output** in D2L Brightspace — official behavior examples
- [Higher/Lower Game SRS](hilow_game_srs.md) — organized requirements reference
- [Software Development Worksheet (SDW)](../hilow_game_sdw.md) — optional guided working notes

Relevant zyBooks topics include:

- **4.1 Loops (general)**
- **4.2 While loops**
- **4.3 More while examples**
- **4.7 While vs. for loops**
- **4.9 Developing programs incrementally**

Earlier decision-branching and relational-operator topics are also important.

## What You Will Do

### 1. Read the Official Assignment

Read the complete Module Four Assignment Guidelines and Rubric before working from the repository guidance.

Identify what the assignment says about:

- lower-bound and upper-bound inputs;
- validation of the relationship between the bounds;
- random-number generation;
- guess input and validation;
- too-low, too-high, and correct outcomes;
- repeated behavior; and
- the one required submission file.

### 2. Review the Sample Output as Behavior

The sample output is not pseudocode. Use it as evidence of what the planned program should do.

For each interaction, ask:

- What input did the player provide?
- What output did the program produce?
- What decision caused that output?
- What must repeat next?
- What condition would stop that repetition?

The assignment allows output wording to differ. Focus on the required behavior rather than copying exact sentences.

### 3. Read the SRS

Open the [SRS](hilow_game_srs.md) and read it from beginning to end.

Pay particular attention to:

- `## 1. Functional Requirements`
- `## 2. Design Requirements`
- `## 3. Technology and File Constraints`
- `## 4. Behavior Verification Cases`
- `## 5. Interpretation Notes`
- `## 6. Out of Scope Unless Your Instructor Adds a Requirement`

### 4. Identify Input, Processing, and Output

Think about the required behavior as:

> **Input → Processing → Output**

Identify:

- what information comes from the player;
- what value the program generates;
- what validation is required;
- what comparisons determine game feedback;
- what information is output; and
- what work must repeat.

Record these ideas in the Analyze section of the [SDW](../hilow_game_sdw.md), if useful.

### 5. Separate the Three Repetition Needs

The assignment contains more than one repeated behavior.

Your design must account for:

1. obtaining bounds again when the lower bound is not less than the upper bound;
2. obtaining another guess when a guess is outside the selected bounds; and
3. continuing the game after an incorrect valid guess until the correct number is guessed.

Do not write the finished pseudocode yet. First be able to explain what condition starts or continues each repetition and what condition allows it to stop.

### 6. Distinguish Requirements From Extra Features

The assignment does **not** require you to add unrelated features such as:

- handling nonnumeric text input;
- counting guesses;
- limiting the number of guesses;
- starting another round after a correct guess; or
- matching one exact output sentence.

Those behaviors should not become graded requirements unless your instructor or current course materials add them.

### 7. Complete the Analyze Checkpoint

Use the checkpoint in the SDW before moving to Design.

## Check Your Work

Before continuing, make sure:

- [ ] I read the complete Module Four Assignment Guidelines and Rubric.
- [ ] I reviewed the Higher/Lower Game Sample Output.
- [ ] I read the complete SRS.
- [ ] I can explain the game's purpose in my own words.
- [ ] I identified the required inputs, generated value, decisions, outputs, and repeated behavior.
- [ ] I can explain both input-validation requirements.
- [ ] I can explain what stops each repeated section.
- [ ] I did not add extra requirements that the assignment does not state.
- [ ] I am ready to express the complete design as pseudocode.

## Help and Support

If you have difficulty completing this phase:

- Review the [SRS](hilow_game_srs.md) first.
- See the [Module Four Assignment Wiki](https://github.com/GC-STEM/it140-m4-assignment/wiki) for supplemental explanations.
- Use [GitHub Discussions](https://github.com/GC-STEM/it140-m4-assignment/discussions) for questions about the repository or provided analysis materials.
- Use [GitHub Issues](https://github.com/GC-STEM/it140-m4-assignment/issues) to report a technical problem with repository files or tools.
- Contact your instructor through D2L Brightspace for assignment requirements, grading, or feedback.

## Next Step

When you can explain the requirements without writing the finished solution, continue to the [Design Phase](../design/README.md).

<!-- Artifact Metadata

* Course: IT 140 - Introduction to Scripting
* Artifact Title: Module Four Assignment | Analyze Phase
* Artifact Type: Required assignment guidance; no Analyze-phase deliverable submitted for grading
* Artifact Purpose: Guide students through understanding the Higher/Lower Game requirements before creating the graded pseudocode design.
* Artifact Description: Students review the official assignment, sample output, and SRS; identify inputs, validation, decisions, outputs, and repetition; and distinguish stated requirements from optional features.
* Artifact Version: {{semantic version number}}
* Artifact Date: {{artifact date in YYYY-MM-DD format}}
* Development Status: {{development status}}

-->
