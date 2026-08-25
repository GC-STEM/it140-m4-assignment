<!-- To see this file in a clean, formatted view, right-click on the filename and choose "Open Preview." -->

# Construct Phase | Optional Python Practice

**Required assignment path:** [Start Here](../README.md) → [Analyze](../analysis/README.md) → [Design](../design/README.md) → [Submit](../README.md#3-submit-your-assignment)

**Optional SDLC practice:** **Construct** → [Test](../tests/README.md)

## Purpose

The Construct phase turns a design into working code.

For Module Four, construction is **optional practice**. Your grade is based on `design/hilow_game.pseudo`, not on `hilow_game.py`.

Complete this phase only **after** your graded pseudocode is finished. The goal is to practice using your own design as the plan for a Python program.

## Deliverable

**This phase produces no graded or submitted Module Four deliverable.**

If you choose the practice, edit:

- [`hilow_game.py`](hilow_game.py)

Do not submit this file unless your instructor specifically requests it.

## What You Will Use

Use:

- your completed [`../design/hilow_game.pseudo`](../design/hilow_game.pseudo);
- the provided starter [`hilow_game.py`](hilow_game.py);
- the Higher/Lower Game Sample Output;
- the [SRS](../analysis/hilow_game_srs.md); and
- relevant zyBooks material.

Useful Module Four sections include:

- 4.1 Loops (general)
- 4.2 While loops
- 4.3 More while examples
- 4.7 While vs. for loops
- 4.9 Developing programs incrementally

Earlier material on input/output, type conversion, decision branching, relational operators, Boolean expressions, and indentation also applies.

## What You Will Do

### 1. Finish the Graded Design First

Do not use coding as a substitute for the graded pseudocode.

Before editing `hilow_game.py`, make sure your pseudocode represents:

- bound input and validation;
- random-number generation;
- guess input and validation;
- the three valid-guess outcomes; and
- repetition until the correct guess.

### 2. Open Design and Code Side by Side

Open your completed pseudocode beside `hilow_game.py`.

Translate one design step at a time. The goal is:

> **Pseudocode step → matching Python behavior**

If coding reveals that the design is incomplete or inconsistent, revise the pseudocode first, then update the code.

### 3. Edit Only TODO Areas

The starter provides organizational scaffolding, including:

- `from random import randint`
- `def main() -> None:`
- the `main()` docstring
- the `if __name__ == "__main__":` main guard

Leave that scaffolding in place and replace the TODO comments with your own code.

The `main()` function and main guard organize the starter file. Functions are taught later in the course; you do not need to master them to complete this optional practice.

### 4. Use the Provided Random Operation

The starter imports `randint` for the random-number requirement.

Use your pseudocode to decide **when** the random number should be generated and which values should be passed to the provided operation.

### 5. Use Loops for Repetition

Translate repeated design behavior into loops rather than copying the same statements many times.

For each loop, keep the same questions you used during Design:

- What condition controls repetition?
- What changes during the loop?
- What lets the loop stop?

### 6. Run Incrementally

Do not wait until the entire optional program is complete before running it.

A useful cycle is:

1. make one small change;
2. save the file;
3. run the program;
4. correct any syntax or runtime error; and
5. continue only after the program runs again.

From the repository root:

```bash
python3 src/hilow_game.py
```

On Windows, if your configured environment uses `python` rather than `python3`, use:

```powershell
python src/hilow_game.py
```

### 7. Complete the Module Docstring

Replace the TODOs in the module docstring so it briefly describes:

- the optional program's purpose;
- major inputs;
- major processing; and
- major output categories.

Keep the description about this Higher/Lower Game, not another assignment.

### 8. Acknowledge Outside Help

If you used outside sources, examples, people, IDE-generated suggestions, or generative AI assistance while completing the optional practice, acknowledge the assistance according to current SNHU and assignment guidance.

If you did not use an outside source, delete the unused reference TODO line.

## Check Your Work

Before moving to optional testing:

- [ ] My graded pseudocode was complete before I began optional coding.
- [ ] I changed only TODO areas in the starter.
- [ ] My module docstring describes the Higher/Lower Game.
- [ ] My code follows my own pseudocode.
- [ ] I left the starter import, `main()` definition, and main guard in place.
- [ ] I used loops for repeated behavior.
- [ ] Each loop has a path toward its stopping condition.
- [ ] I ran after small changes and corrected errors incrementally.
- [ ] I acknowledged outside help I actually used or deleted the unused reference TODO.
- [ ] No TODO lines remain in my completed optional file.
- [ ] The program runs without a Python error for a normal input sequence.

## Help and Support

If you have difficulty:

- Start with your completed pseudocode and translate one step at a time.
- Return to [Design](../design/README.md) if the design is incomplete.
- Review the Higher/Lower Game Sample Output for expected behavior.
- See the [Module Four Assignment Wiki](https://github.com/GC-STEM/it140-m4-assignment/wiki) for supplemental guidance.
- Use [GitHub Discussions](https://github.com/GC-STEM/it140-m4-assignment/discussions) for questions about optional practice tools.
- Use [GitHub Issues](https://github.com/GC-STEM/it140-m4-assignment/issues) to report technical problems with the provided starter.
- Contact your instructor through D2L Brightspace for assignment requirements or grading questions.

## Next Step

Continue to [Test](../tests/README.md) for optional practice, or return to [Submit Your Assignment](../README.md#3-submit-your-assignment).

<!-- Artifact Metadata

* Course: IT 140 - Introduction to Scripting
* Artifact Title: Module Four Assignment | Construct Phase
* Artifact Type: Optional Python construction-practice guidance
* Artifact Purpose: Help students translate their completed graded pseudocode into a simple Python program using Module Four concepts.
* Artifact Version: {{semantic version number}}
* Artifact Date: {{artifact date in YYYY-MM-DD format}}
* Development Status: {{development status}}

-->
