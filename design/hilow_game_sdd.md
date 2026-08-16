# Software Design Document (SDD)

- **Course**: IT 140 - Introduction to Scripting
- **Activity**: Module Four Assignment
- **Program name**: Higher/Lower Game
- **Status**: Design reference; do not edit

## 0. Purpose

This SDD helps you organize the design work without providing completed pseudocode. The graded design decisions belong in your own `hilow_game.pseudo` file.

The current Module Four Assignment Guidelines and Rubric remains the official source for assignment requirements.

## 1. Design Inputs

Use these sources while designing:

1. The Module Four Assignment Guidelines and Rubric
2. The Higher/Lower Game Sample Output
3. [`../analysis/hilow_game_srs.md`](../analysis/hilow_game_srs.md)
4. Your optional [`../hilow_game_sdw.md`](../hilow_game_sdw.md) notes

## 2. Design Model

The solution needs to represent several related types of work:

- **Input** — obtain range bounds and player guesses.
- **Validation** — make sure bounds and guesses satisfy the assignment rules.
- **Random selection** — establish the number the player is trying to guess.
- **Decision branching** — distinguish too-low, too-high, and correct guesses.
- **Repetition** — repeat work when input is invalid and continue the game until the correct guess.
- **Output** — communicate prompts, validation feedback, guess feedback, and success.

Your pseudocode should make the relationship among these steps clear without adding requirements that are not in the assignment.

## 3. Repetition to Represent

Module Four introduces loops, so stopping conditions are a major part of the design.

At minimum, your design needs to make clear:

- How the program responds when the lower and upper bounds do not satisfy the required relationship.
- How the player gets another opportunity when a guess is outside the selected range.
- How guessing continues after an incorrect valid guess.
- What condition ends the guessing process.

A loop must have a path toward its stopping condition. When reviewing your design, make sure each repeated section can eventually end when valid input or the correct guess is provided.

## 4. Decision Branching to Represent

Once a valid guess is available, the design must distinguish three relationships between the guess and the random number:

- Lower
- Higher
- Equal

Each path needs the appropriate result, and the incorrect paths must allow the game to continue.

## 5. Pseudocode Design Constraints

Your pseudocode should:

- Use clear, logically ordered steps.
- Use indentation to show statements inside branches and loops.
- Use appropriate pseudocode keywords.
- Identify inputs and outputs.
- Represent both input-validation needs.
- Represent the required decision branches.
- Represent repetition and its stopping conditions.
- Be detailed enough to guide optional construction without becoming Python code.

## 6. Design Review

Use this table after completing `hilow_game.pseudo`.

| Question | Check |
| --- | :---: |
| Are lower and upper bounds obtained? | ☐ |
| Is the relationship between the bounds validated? | ☐ |
| Are invalid bounds handled by obtaining bounds again? | ☐ |
| Is a random number established from the selected range? | ☐ |
| Is a guess obtained and validated against the range? | ☐ |
| Are too-low, too-high, and correct outcomes represented? | ☐ |
| Do incorrect guesses lead to another guess? | ☐ |
| Does a correct guess stop the guessing loop? | ☐ |
| Are loop and branch bodies clearly indented? | ☐ |
| Can the sample-output scenarios be traced through the design? | ☐ |

## 7. Optional Construction Handoff

If you continue into the optional Construct phase, treat your completed pseudocode as the design handed to the programmer.

Implement what your design says. If coding reveals a design problem, revise the pseudocode first, then update the code so the design and implementation stay consistent.
