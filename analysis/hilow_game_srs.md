# Software Requirements Specification (SRS)

- **Course**: IT 140 - Introduction to Scripting
- **Activity**: Module Four Assignment
- **Program name**: Higher/Lower Game
- **Status**: Provided requirements reference; do not edit

## 0. General Description

The Higher/Lower Game is a guessing game for Bella. The player chooses a lower and upper bound, the program selects a random number from that range, and the player continues guessing until the selected number is guessed correctly. The program provides feedback after guesses and validates the range information and guesses described by the assignment.

This SRS reorganizes requirements from the Module Four Assignment Guidelines and Rubric and its Higher/Lower Game Sample Output. If this file and the current course materials differ, follow the current course materials.

## 1. Functional Requirements

The program shall:

- **1.1** Prompt the player to enter a lower bound and an upper bound.
- **1.2** Validate the bounds so the lower bound is less than the upper bound.
- **1.3** Obtain new bounds when the entered bounds do not satisfy the required relationship.
- **1.4** Generate a random number between the valid lower and upper bounds.
- **1.5** Prompt the player to enter a guess between the selected bounds.
- **1.6** Validate guesses so the player only proceeds with guesses that are between the selected bounds.
- **1.7** Use decision branching to distinguish a guess that is:
  - Lower than the random number
  - Higher than the random number
  - Equal to the random number
- **1.8** Output appropriate feedback for each guess result.
- **1.9** Continue prompting for guesses until the player guesses the random number correctly.
- **1.10** End the guessing process after a correct guess and communicate that the guess is correct.

## 2. Design Requirements

The graded pseudocode shall:

- **2.1** Logically outline each step needed to satisfy the required game functionality.
- **2.2** Identify the required user inputs and program outputs.
- **2.3** Represent input validation for the bounds.
- **2.4** Represent input validation for guesses.
- **2.5** Use decision branching to control the too-low, too-high, and correct-guess paths.
- **2.6** Use loops to represent repeated behavior, including continued guessing until the correct number is guessed.
- **2.7** Use clear indentation and pseudocode keywords so the program flow is understandable.

## 3. Technology and File Constraints

- **3.1** The graded deliverable shall remain a pseudocode text file (`.pseudo`).
- **3.2** The assignment does not require a flowchart deliverable.
- **3.3** Python construction and testing are optional practice for this assignment and are not graded deliverables.

## 4. Acceptance Conditions

A design is ready for submission when a reader can follow the pseudocode from start to finish and determine how it handles each required behavior.

Use the official Higher/Lower Game Sample Output and the following behavior checks when reviewing your design:

| Scenario | Condition | Expected behavior |
| --- | --- | --- |
| Valid bounds | Lower bound is less than upper bound | Program continues using the selected range |
| Invalid bounds | Lower bound is not less than upper bound | Program explains the problem and obtains bounds again |
| Guess below range | Guess is below the selected lower bound | Guess is rejected through input validation and another guess is obtained |
| Guess above range | Guess is above the selected upper bound | Guess is rejected through input validation and another guess is obtained |
| Guess too low | Valid guess is lower than the random number | Program indicates the guess is too low and continues |
| Guess too high | Valid guess is higher than the random number | Program indicates the guess is too high and continues |
| Correct guess | Guess equals the random number | Program indicates success and ends the guessing loop |

The sample output demonstrates these behaviors with example values. The assignment notes that output wording in your pseudocode may differ slightly from the sample.

## 5. Important Interpretation Notes

The provided assignment materials require the program to generate a random number "between" the lower and upper bounds and to accept guesses "between" those bounds. They do not separately define endpoint terminology in the rubric text.

When converting your pseudocode to optional Python practice, use the current course starter file and instructor guidance for the intended Python random-number operation. Do not add unrelated input rules or advanced error handling as graded requirements unless current course instructions require them.

## 6. Out of Scope Unless Your Instructor Adds a Requirement

The assignment Guidelines and Rubric does not explicitly require:

- Handling nonnumeric text entered where a number is expected
- A fixed number of guesses
- A score or guess counter
- Multiple rounds after the correct number is guessed
- Exact wording for every output message
- A flowchart submission

Do not add these as graded requirements unless your instructor or current course materials direct you to do so.
