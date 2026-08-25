# Software Requirements Specification (SRS)

- **Course:** IT 140 - *Introduction to Scripting*
- **Activity:** Module Four Assignment
- **Program:** Higher/Lower Game
- **Status:** Provided requirements reference; do not edit

## 0. General Description

The Higher/Lower Game allows a player to choose a lower and upper bound and then guess a randomly selected number between those bounds. The program provides feedback after valid guesses and continues until the player guesses the selected number correctly.

This SRS reorganizes requirements from the Module Four Assignment Guidelines and Rubric and the Higher/Lower Game Sample Output. It does not replace or expand those course materials. If this file and the current course materials differ, follow the current course materials.

## 1. Functional Requirements

The planned program shall:

- **FR-1 — Obtain bounds.** Prompt the player to enter a lower bound and an upper bound.
- **FR-2 — Validate bounds.** Ensure the lower bound is less than the upper bound.
- **FR-3 — Repeat invalid-bound input.** Obtain bounds again when the entered bounds do not satisfy the required relationship.
- **FR-4 — Generate the target number.** Generate a random number between the valid lower and upper bounds.
- **FR-5 — Obtain a guess.** Prompt the player to enter a guess between the selected bounds.
- **FR-6 — Validate guesses.** Ensure the player proceeds only with guesses between the selected bounds.
- **FR-7 — Repeat invalid-guess input.** Obtain another guess when the entered guess is outside the selected bounds.
- **FR-8 — Compare a valid guess.** Use decision branching to distinguish a valid guess that is lower than, higher than, or equal to the target number.
- **FR-9 — Output guess feedback.** Output appropriate feedback for too-low, too-high, and correct guesses.
- **FR-10 — Continue the game.** Continue prompting for guesses until the target number is guessed correctly.
- **FR-11 — End after success.** Stop the guessing process after a correct guess.

## 2. Design Requirements

The graded assignment has one design deliverable.

### DR-1 — Pseudocode

Create `design/hilow_game.pseudo` that:

- logically outlines each step needed to satisfy the required game functionality;
- identifies the required user inputs and program outputs;
- represents validation of the lower and upper bounds;
- represents validation of guesses;
- uses decision branching for too-low, too-high, and correct guesses;
- uses loops for required repeated behavior;
- makes the stopping condition for the guessing process clear; and
- uses indentation and pseudocode keywords so the program flow is understandable.

### DR-2 — Rubric Alignment

The official rubric evaluates the pseudocode using three criteria:

- **Logical Steps — 35%**
- **Input/Output — 30%**
- **Program Flow — 35%**

A complete design should satisfy all three criteria without adding unrelated functionality.

## 3. Technology and File Constraints

- **TC-1:** The graded deliverable shall remain a pseudocode text file (`.pseudo`).
- **TC-2:** The assignment does not require a flowchart submission.
- **TC-3:** Python construction and testing are optional practice and are not graded Module Four deliverables.

## 4. Behavior Verification Cases

A design is ready for final review when a reader can trace each required behavior through the pseudocode.

The scenarios below restate or derive from the required behaviors. They are **repository learning checks**, not additional graded requirements and not prescribed output wording.

| Scenario | Condition | Behavior to trace |
| --- | --- | --- |
| Valid bounds | Lower bound is less than upper bound | Continue using the selected range |
| Invalid bounds | Lower bound is not less than upper bound | Obtain bounds again |
| Guess below range | Guess is below the selected lower bound | Reject it through validation and obtain another guess |
| Guess above range | Guess is above the selected upper bound | Reject it through validation and obtain another guess |
| Guess too low | Valid guess is lower than the target number | Output too-low feedback and continue |
| Guess too high | Valid guess is higher than the target number | Output too-high feedback and continue |
| Correct guess | Guess equals the target number | Output success and stop the guessing loop |

Use the official Higher/Lower Game Sample Output for concrete examples of these behaviors.

## 5. Interpretation Notes

### 5.1 "Between" the Selected Bounds

The assignment requires the random number and valid guesses to be between the lower and upper bounds. The rubric does not separately define endpoint terminology.

When you complete the optional Python practice, use the provided starter operation and current course guidance for the intended Python behavior. Do not turn an implementation detail into a new graded pseudocode requirement.

### 5.2 Validation and Guess Comparison Are Different Decisions

A guess must first satisfy the selected range before the game compares it with the target number.

Keep these ideas distinct when reviewing the design:

1. **Validation:** Is the guess within the selected bounds?
2. **Game decision:** Is the valid guess too low, too high, or correct?

### 5.3 Repetition Must Make Progress

Each repeated section should have a clear condition that can eventually allow the program to continue or stop. A design that repeats without a path toward new input can describe an infinite loop instead of the required game behavior.

## 6. Out of Scope Unless Your Instructor Adds a Requirement

The Module Four Assignment Guidelines and Rubric does not explicitly require:

- handling nonnumeric text entered where a number is expected;
- a fixed number of guesses;
- a score or guess counter;
- multiple rounds after the correct number is guessed;
- exact wording for every output message; or
- a flowchart submission.

Do not add these as graded requirements unless your instructor or current course materials direct you to do so.

## Requirements Traceability

| Rubric criterion | Primary requirements |
| --- | --- |
| Logical Steps — 35% | FR-1 through FR-11; DR-1 |
| Input/Output — 30% | FR-1, FR-5, FR-9; DR-1 |
| Program Flow — 35% | FR-2, FR-3, FR-6 through FR-11; DR-1 |

<!-- Artifact Metadata

* Course: IT 140 - Introduction to Scripting
* Artifact Title: Higher/Lower Game Software Requirements Specification
* Artifact Type: Course-provided requirements reference
* Artifact Purpose: Reorganize the official Module Four requirements for systematic analysis without adding graded requirements.
* Artifact Version: {{semantic version number}}
* Artifact Date: {{artifact date in YYYY-MM-DD format}}
* Development Status: {{development status}}

-->
