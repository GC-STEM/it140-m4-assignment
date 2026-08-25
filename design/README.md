<!-- To see this file in a clean, formatted view, right-click on the filename and choose "Open Preview." -->

# Design Phase | Write the Higher/Lower Game Pseudocode

**Required assignment progress:** [0 Start Here](../README.md) → [1 Analyze](../analysis/README.md) → **2 Design** → [3 Submit](../README.md#3-submit-your-assignment)

**Optional SDLC practice after Design:** [Construct](../src/README.md) → [Test](../tests/README.md)

## Purpose

During the Design phase, your goal is to decide **how** the Higher/Lower Game will meet the requirements before writing Python code.

Module Four has one graded design deliverable: pseudocode. You do **not** need to create or submit a flowchart.

## Graded Deliverable

Complete:

- [`hilow_game.pseudo`](hilow_game.pseudo) — graded pseudocode

The [Software Design Document (SDD)](hilow_game_sdd.md) provides design guidance without giving you a completed solution. The [SDW](../hilow_game_sdw.md) provides optional working space.

The course-provided [`hilow_game.drawio`](hilow_game.drawio) file is a reference artifact. Do not edit or submit it for this assignment.

## What You Will Use

Use:

- the Module Four Assignment Guidelines and Rubric in D2L Brightspace;
- the Higher/Lower Game Sample Output;
- the [SRS](../analysis/hilow_game_srs.md);
- the [SDD](hilow_game_sdd.md);
- the optional [SDW](../hilow_game_sdw.md); and
- the pseudocode starter template.

Relevant zyBooks topics include loops, `while` loops, decision branching, relational and Boolean expressions, indentation, and incremental development.

## What You Will Do

### 1. Review Requirements Before Designing

Make sure you can explain:

- what lower and upper bounds the player provides;
- what makes the bounds valid;
- when a random number is generated;
- what makes a guess valid;
- the too-low, too-high, and correct outcomes;
- what work repeats; and
- what causes each repeated section to stop.

If any of these are unclear, return to the [Analyze Phase](../analysis/README.md) before editing the graded file.

### 2. Plan the Major Stages

Use the Design section of the [SDW](../hilow_game_sdw.md), if useful, to list the major stages in words before writing detailed pseudocode.

A useful design question is:

> What must happen before the next stage can safely begin?

For example, the game should not depend on a valid range until the range requirements have actually been satisfied.

Do not begin by writing Python. The purpose of this assignment is to practice design before construction.

### 3. Identify Repeated Behavior

The assignment contains several situations in which the program must obtain new input or continue the game.

For each repeated behavior, identify:

1. what condition causes repetition;
2. what happens during one repetition;
3. what information can change; and
4. what condition lets the program continue or stop.

A loop should have a path toward its stopping condition. If the design repeats without obtaining new information, trace it carefully for a possible infinite loop.

### 4. Separate Validation From Game Decisions

The assignment includes two different kinds of decisions:

- **validation decisions** determine whether input is acceptable; and
- **game decisions** determine whether a valid guess is too low, too high, or correct.

Keep those purposes distinct in your design. A guess should satisfy the range requirement before it is treated as a valid game guess.

### 5. Write the Pseudocode

Open [`hilow_game.pseudo`](hilow_game.pseudo).

Replace the `TODO:` prompts with your own pseudocode. Your finished design should:

- logically outline the complete required game;
- identify the required inputs and outputs;
- represent validation for the lower and upper bounds;
- represent validation for guesses;
- represent random-number generation;
- use decision branching for the three valid-guess outcomes;
- use loops for repeated behavior;
- make stopping conditions understandable; and
- use indentation and pseudocode keywords consistently.

Pseudocode is a design tool, not executable Python. Focus on clear logic rather than exact Python punctuation or syntax.

Appropriate pseudocode keywords may include words such as:

- `INPUT`
- `OUTPUT`
- `SET` or `LET`
- `IF`
- `ELSE`
- `WHILE`
- `REPEAT`
- `UNTIL`

There is no single universal pseudocode language. Use consistent terms that make the algorithm understandable.

### 6. Trace Required Behaviors

Use the [SRS behavior verification cases](../analysis/hilow_game_srs.md#4-behavior-verification-cases) and the official sample output to trace your pseudocode by hand.

At minimum, make sure you can follow the design for:

- valid bounds;
- invalid bounds followed by valid bounds;
- a guess below the selected range;
- a guess above the selected range;
- a valid guess that is too low;
- a valid guess that is too high; and
- a correct guess that ends the game.

If you cannot explain exactly what happens next in one of these cases, revise the design before submission.

## 7. Review Against the Rubric

### Logical Steps — 35%

- [ ] The pseudocode logically outlines the complete required program.
- [ ] The steps are in an order another programmer can follow.
- [ ] All required functionality is represented.

### Input/Output — 30%

- [ ] Lower-bound and upper-bound inputs are represented.
- [ ] Guess input is represented.
- [ ] Validation behavior is represented.
- [ ] Required feedback and success output are represented.

### Program Flow — 35%

- [ ] Decision branching distinguishes too-low, too-high, and correct guesses.
- [ ] Loops represent the required repeated behavior.
- [ ] The stopping conditions are understandable.
- [ ] Indentation makes nested decisions and loops easy to follow.

### Starter completion

- [ ] No starter `TODO:` prompts remain in the graded pseudocode.
- [ ] The file remains in `.pseudo` format.

## 8. Review the Assignment Checks

After you commit and push, GitHub Assignment Checks can verify basic file state, including whether the graded pseudocode changed from its starter state, keeps its outer `START` / `END` structure, and no longer contains starter `TODO:` prompts.

The checks also verify basic repository integrity. They do **not** evaluate whether your pseudocode correctly satisfies the rubric. A green check is not a grade and does not submit your assignment.

## Help and Support

If you have difficulty completing this phase:

- Compare the [SRS](../analysis/hilow_game_srs.md), [SDD](hilow_game_sdd.md), and your SDW notes one requirement at a time.
- Review the official Higher/Lower Game Sample Output for behavior examples.
- See the [Module Four Assignment Wiki](https://github.com/GC-STEM/it140-m4-assignment/wiki) for supplemental explanations of pseudocode, validation, branching, and loops.
- Use [GitHub Discussions](https://github.com/GC-STEM/it140-m4-assignment/discussions) for repository-related questions that do not request a completed graded solution.
- Use [GitHub Issues](https://github.com/GC-STEM/it140-m4-assignment/issues) to report a technical problem with the provided files, documentation, or automated checks.
- Contact your instructor through D2L Brightspace for assignment requirements, grading, or feedback.

## Next Step

When `hilow_game.pseudo` meets the current Guidelines and Rubric, go to [Submit Your Assignment](../README.md#3-submit-your-assignment).

After the graded work is ready, you may also continue to the [Construct Phase](../src/README.md) for optional Python practice.

<!-- Artifact Metadata

* Course: IT 140 - Introduction to Scripting
* Artifact Title: Module Four Assignment | Design Phase
* Artifact Type: Required assignment guidance for the graded pseudocode design
* Artifact Purpose: Guide students in planning, writing, tracing, and reviewing the Higher/Lower Game pseudocode without providing a completed solution.
* Artifact Description: Students identify repeated behavior, validation, decision paths, and stopping conditions; write structured pseudocode; and review it against the official rubric.
* Artifact Version: {{semantic version number}}
* Artifact Date: {{artifact date in YYYY-MM-DD format}}
* Development Status: {{development status}}

-->
