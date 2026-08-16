# Analyze Phase | Understand the Higher/Lower Game

**SDLC progress:** [Start Here](../README.md) → **1 Analyze** → [2 Design](../design/README.md) → [3 Construct (Practice)](../src/README.md) → [4 Test (Practice)](../tests/README.md) → [Submit](../README.md#submit-your-assignment)

## Purpose

The Analyze phase is where you make sure you understand **what the solution must do** before deciding exactly how to express the solution in pseudocode.

For this assignment, the Module Four Assignment Guidelines and Rubric is the official source of requirements. The Higher/Lower Game Sample Output shows example program behavior. The provided [Software Requirements Specification (SRS)](hilow_game_srs.md) reorganizes those requirements into a form commonly used during software development.

The Analyze phase does **not** create a graded deliverable. It prepares you to create the graded pseudocode in the Design phase.

## What You Will Use

- Module Four Assignment Guidelines and Rubric in D2L Brightspace
- Higher/Lower Game Sample Output in D2L Brightspace
- [Higher/Lower Game SRS](hilow_game_srs.md)
- [Software Development Worksheet (SDW)](../hilow_game_sdw.md) for recommended working notes

## What You Will Do

1. Read the complete Module Four Assignment Guidelines and Rubric.
2. Review the Higher/Lower Game Sample Output.
3. Read the [SRS](hilow_game_srs.md).
4. Identify the program's inputs, validation rules, generated value, decisions, loops, and outputs.
5. Pay special attention to the two different validation needs:
   - The lower bound must be less than the upper bound.
   - Guesses must stay between the selected bounds.
6. Identify what must repeat and what condition stops each repetition.
7. Record concise notes in the Analyze section of the [SDW](../hilow_game_sdw.md), if useful.
8. Compare your understanding with the rubric before moving to Design.

## Read Sample Output as Evidence

The sample output is not pseudocode. Use it to observe **behavior**.

For each line or group of lines, ask:

- Is this user input or program output?
- What must have happened immediately before this?
- What decision caused this output?
- Does the program continue or stop afterward?
- What changed between this step and the next repetition?

The assignment notes that your output wording may differ slightly from the samples. Focus on the required behavior rather than copying every sentence exactly.

## Check Your Work

Before moving to Design, you should be able to explain in your own words:

- What the lower and upper bounds represent
- What makes the bounds valid
- What the program does after valid bounds are established
- What makes a guess valid
- Which three outcomes a valid guess can produce
- Which behaviors repeat
- What causes the game to end

You do not need Python code to answer these questions.

## Help and Support

For supplemental explanations, see the [Module Four Assignment Wiki](https://github.com/GC-STEM/it140-m4-assignment/wiki).

For assignment requirements, grading, or feedback, contact your instructor through D2L Brightspace.

## Next Step

Continue to the [Design Phase](../design/README.md) to create the graded pseudocode deliverable.
