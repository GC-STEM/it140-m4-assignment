# Software Design Document (SDD)

- **Course:** IT 140 - *Introduction to Scripting*
- **Activity:** Module Four Assignment
- **Program:** Higher/Lower Game
- **Status:** Design reference; do not edit

## 0. Purpose

This SDD helps you organize the Higher/Lower Game design without providing completed pseudocode. The graded design decisions belong in your own `hilow_game.pseudo` file.

The current Module Four Assignment Guidelines and Rubric remains the official source for assignment requirements.

## 1. Design Inputs

Use these sources while designing:

1. The Module Four Assignment Guidelines and Rubric
2. The Higher/Lower Game Sample Output
3. [`../analysis/hilow_game_srs.md`](../analysis/hilow_game_srs.md)
4. Your optional [`../hilow_game_sdw.md`](../hilow_game_sdw.md) notes

## 2. Solution Overview

The design needs to represent several related kinds of work:

- **Input** — obtain the range bounds and player guesses.
- **Validation** — determine whether bounds and guesses satisfy the assignment rules.
- **Random selection** — establish the target number after valid bounds are available.
- **Decision branching** — distinguish a valid guess that is too low, too high, or correct.
- **Repetition** — obtain new input when required and continue the game until the correct guess.
- **Output** — communicate prompts, feedback, and success.

Your pseudocode should make the relationship among these steps clear without adding requirements that are not in the assignment.

## 3. Input and Output

The assignment requires the design to identify the user information the program receives and the information it communicates.

Trace the design to confirm that:

- lower and upper bounds are obtained before they are used;
- a guess is obtained before it is evaluated;
- invalid input leads to the required opportunity for new input; and
- each game outcome provides the appropriate feedback.

Exact wording for every prompt or message is not the focus of the rubric. The behavior should be understandable.

## 4. Validation and Decision Branching

Validation and game comparison serve different purposes.

### Bounds validation

The lower and upper bounds must satisfy the relationship stated in the assignment before the game proceeds.

### Guess validation

The player should proceed only with guesses that satisfy the selected-range requirement.

### Guess comparison

After a valid guess is available, the design must distinguish three outcomes:

- lower than the target number;
- higher than the target number; and
- equal to the target number.

The incorrect paths must allow the game to continue. The correct path ends the guessing process.

## 5. Repetition and Stopping Conditions

Module Four introduces loops, so repeated behavior and stopping conditions are major design concerns.

For every repeated section, ask:

1. What condition causes this section to repeat?
2. What new information can be obtained or changed?
3. What condition lets execution continue beyond the loop?

At minimum, the design must account for:

- obtaining bounds again when the required relationship is not satisfied;
- obtaining another guess when a guess does not satisfy the selected range; and
- continuing the game after an incorrect valid guess until the target is guessed.

A loop should have a path toward its stopping condition. Repetition without updated information may describe an infinite loop rather than the required behavior.

## 6. Pseudocode Design Constraints

Your pseudocode should:

- use clear, logically ordered steps;
- identify the required inputs and outputs;
- represent both validation requirements;
- represent random-number generation;
- use decision branching for the three valid-guess outcomes;
- use loops for required repetition;
- make stopping conditions understandable;
- use indentation to show statements inside branches and loops; and
- be detailed enough to guide optional construction without becoming Python code.

## 7. Requirements Traceability

Use the table to verify that major requirement groups appear in the graded design.

| Requirement group | SRS references | Pseudocode evidence to locate |
| --- | --- | --- |
| Bounds input and validation | FR-1 through FR-3 | Input, validation, repetition |
| Target generation | FR-4 | Random-number step after valid bounds |
| Guess input and validation | FR-5 through FR-7 | Guess input, validation, repetition |
| Guess outcomes | FR-8 and FR-9 | Too-low, too-high, correct branches |
| Game repetition and ending | FR-10 and FR-11 | Guessing loop and stopping condition |

This table is a review tool. It does not prescribe exact pseudocode statements.

## 8. Design Review

Before submission, ask:

- [ ] Are lower and upper bounds obtained?
- [ ] Is the required relationship between the bounds validated?
- [ ] Can invalid bounds lead to new bound input?
- [ ] Is the target number generated after valid bounds are available?
- [ ] Is a guess obtained and validated against the selected range?
- [ ] Can an invalid guess lead to another guess?
- [ ] Are too-low, too-high, and correct outcomes represented?
- [ ] Do incorrect valid guesses allow play to continue?
- [ ] Does a correct guess stop the guessing process?
- [ ] Are loop and branch bodies clearly indented?
- [ ] Can the official sample-output behaviors be traced through the design?

## 9. Optional Construction Handoff

If you continue into the optional Construct phase, treat your completed pseudocode as the design handed to the programmer.

Implement what your design says. If coding reveals a design problem, revise the pseudocode first, then update the code so the design and implementation stay consistent.
