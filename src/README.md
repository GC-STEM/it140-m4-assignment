# Construct Phase | Optional Python Practice

**SDLC progress:** [Start Here](../README.md) → [1 Analyze](../analysis/README.md) → [2 Design](../design/README.md) → **3 Construct (Practice)** → [4 Test (Practice)](../tests/README.md) → [Submit](../README.md#submit-your-assignment)

## Purpose

The Construct phase turns a design into working code.

For the Module Four Assignment, construction is **optional practice**. Your grade is based on `design/hilow_game.pseudo`, not on `hilow_game.py`.

Complete this phase only **after** your graded pseudocode is finished. The goal is to practice using your own design as the plan for a Python program.

## What You Will Use

- Your completed [`../design/hilow_game.pseudo`](../design/hilow_game.pseudo)
- The provided starter file [`hilow_game.py`](hilow_game.py)
- The Higher/Lower Game Sample Output
- Module Four loop content
- Relevant earlier content on input/output and decision branching
- Relevant zyBooks material, especially sections on `while` loops, `for` loops, loop stopping conditions, developing programs incrementally, `if`/`else`, relational operators, type conversion, and indentation

## What You Will Do

1. Open your completed pseudocode beside `hilow_game.py`.
2. Read one design step at a time.
3. Replace the matching `TODO:` comment in the Python starter file with the simplest Python code that performs that step.
4. Run the program after small changes instead of waiting until the entire program is complete.
5. Keep your code aligned with the pseudocode. If coding reveals that the design is incomplete or incorrect, revise the pseudocode first and then update the code.

> [!IMPORTANT]
> Do not use the optional construction work as a substitute for completing the graded pseudocode.

## Keep the Program Appropriate for Module Four

Focus on concepts introduced by this point in the course:

- Variables
- Numeric input and type conversion
- Output
- Relational and Boolean expressions
- `if` / `elif` / `else`
- `while` loops
- `for` loops when appropriate
- `range()` when appropriate
- Indentation
- Incremental development

The starter file includes `main()` and a main guard as organizational scaffolding. You may follow the TODOs without needing to master functions yet; functions are taught later in the course.

The starter also provides Python's `randint` function for the random-number requirement. Use your pseudocode to decide **when** that operation belongs in the program.

## Run the Program

From the repository root in the VS Code integrated terminal:

```bash
python3 src/hilow_game.py
```

On Windows, if `python3` is not available but the course IDE provides `python`, use:

```powershell
python src/hilow_game.py
```

Use the official sample-output scenarios as a guide, but remember that a randomly selected number can cause the exact sequence of too-low and too-high messages to differ from one run to another.

## Check Your Work

Before moving to optional testing:

- [ ] The program runs without a syntax error.
- [ ] It obtains lower and upper bounds.
- [ ] It does not proceed with an invalid bound relationship.
- [ ] It generates a random number from the selected range.
- [ ] It obtains and validates guesses.
- [ ] It gives too-low or too-high feedback for incorrect valid guesses.
- [ ] It keeps asking until the correct number is guessed.
- [ ] Its behavior matches your pseudocode.

## Next Step

Continue to the [Test Phase](../tests/README.md) for optional practice, or return to [Submit Your Assignment](../README.md#submit-your-assignment).
