# Design Phase | Write the Higher/Lower Game Pseudocode

**SDLC progress:** [Start Here](../README.md) → [1 Analyze](../analysis/README.md) → **2 Design** → [3 Construct (Practice)](../src/README.md) → [4 Test (Practice)](../tests/README.md) → [Submit](../README.md#submit-your-assignment)

## Purpose

The Design phase is the focus of the Module Four Assignment. You will turn the higher/lower game requirements into **pseudocode** that another programmer could follow when writing the program.

This assignment has **one graded design deliverable**. You do not need to create or submit a flowchart.

## Graded Deliverable

Complete:

- [`hilow_game.pseudo`](hilow_game.pseudo) — **graded pseudocode deliverable**

The [Software Design Document (SDD)](hilow_game_sdd.md) is a reference that explains design goals and review checks without providing a completed pseudocode solution. The [SDW](../hilow_game_sdw.md) is optional working space.

## Before You Design

Make sure you have:

1. Read the Module Four Assignment Guidelines and Rubric.
2. Reviewed the Higher/Lower Game Sample Output.
3. Completed the [Analyze Phase](../analysis/README.md).
4. Reviewed the [SRS](../analysis/hilow_game_srs.md).
5. Identified the required inputs, validation rules, decision outcomes, repeated behavior, and outputs.

Module Four focuses on loops. Review the relevant course material on `while` loops, loop stopping conditions, decision branching, relational operators, input/output, and indentation if any of these concepts are unclear.

## Write the Pseudocode

Open [`hilow_game.pseudo`](hilow_game.pseudo).

Replace the `TODO:` prompts with your own pseudocode. Your design should logically account for all required functionality.

### Bounds and Setup

Your pseudocode must make clear:

- How the lower and upper bounds are obtained
- How the relationship between the bounds is validated
- How invalid bounds cause the program to obtain new values
- When the random number is generated

### Guess Input and Validation

Your pseudocode must make clear:

- How a guess is obtained
- How the guess is checked against the selected bounds
- How an out-of-range guess is handled
- How the player gets another opportunity to enter a valid guess

### Decision Branching

For a valid guess, account for all three outcomes:

- Guess is too low
- Guess is too high
- Guess is correct

The pseudocode should make it clear which output belongs to each outcome.

### Loops

Your design must show repeated behavior rather than copying the same steps many times.

For each loop, make the stopping condition understandable. In particular, the guessing process must continue until the correct number is guessed.

> [!TIP]
> Trace your pseudocode using the scenarios in the Higher/Lower Game Sample Output. Follow one statement at a time and keep track of the current lower bound, upper bound, and guess.

## Keep Pseudocode Separate From Python

Pseudocode is a design tool, not executable Python.

Use clear structured language and indentation. Appropriate pseudocode keywords may include words such as:

- `INPUT`
- `OUTPUT`
- `SET` or `LET`
- `IF`
- `ELSE`
- `WHILE`
- `REPEAT`
- `UNTIL`

You do not need to make your pseudocode match Python punctuation or syntax exactly.

## Check Against the Rubric

### Logical Steps — 35%

- [ ] The pseudocode logically outlines the full program.
- [ ] The steps are in an order that another programmer can follow.
- [ ] All required functionality is represented.

### Input/Output — 30%

- [ ] Lower-bound and upper-bound inputs are represented.
- [ ] Guess input is represented.
- [ ] Bound and guess validation behavior is represented.
- [ ] Feedback and success outputs are represented.

### Program Flow — 35%

- [ ] Decision branching distinguishes too-low, too-high, and correct guesses.
- [ ] Loops represent the required repeated behavior.
- [ ] The guessing loop has a clear stopping condition.
- [ ] Indentation makes nested branches and loops understandable.

## Final Trace

Before considering the design complete, trace at least these situations:

1. Valid bounds and a correct first guess
2. Invalid bounds followed by valid bounds
3. An out-of-range guess followed by a valid guess
4. A valid guess that is too low
5. A valid guess that is too high
6. Several guesses before the correct guess

If you cannot explain exactly what your pseudocode does in one of these situations, revise the design before submitting.

## Help and Support

For supplemental explanations about pseudocode, loops, or the course tools, see the [Module Four Assignment Wiki](https://github.com/GC-STEM/it140-m4-assignment/wiki).

For assignment requirements, grading, or feedback, contact your instructor through D2L Brightspace.

## Next Step

Your graded design work is complete when `hilow_game.pseudo` meets the current Guidelines and Rubric.

You may now:

- Go to [Submit Your Assignment](../README.md#submit-your-assignment), or
- Continue to the [Construct Phase](../src/README.md) for optional Python practice.
