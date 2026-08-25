<!-- To see this file in a clean, formatted view, right-click on the filename and choose "Open Preview." -->

# Test Phase | Optional Practice

**Required assignment path:** [Start Here](../README.md) → [Analyze](../analysis/README.md) → [Design](../design/README.md) → [Submit](../README.md#3-submit-your-assignment)

**Optional SDLC practice:** [Construct](../src/README.md) → **Test**

## Purpose

Testing checks whether a constructed program behaves as its requirements and design say it should.

For Module Four, testing Python code is **optional practice**. You do not submit the optional Python program, test file, or test output for grading.

You can also apply testing ideas before code exists by tracing required behaviors through your pseudocode.

## Deliverable

**This phase produces no graded or submitted Module Four deliverable.**

If testing exposes a design problem, correct the graded pseudocode and review it against the rubric again.

## What You Will Use

Use:

- [`../src/hilow_game.py`](../src/hilow_game.py) — optional program you constructed;
- your graded [`../design/hilow_game.pseudo`](../design/hilow_game.pseudo);
- the official Higher/Lower Game Sample Output;
- the [SRS behavior verification cases](../analysis/hilow_game_srs.md#4-behavior-verification-cases); and
- [`test_hilow_game.py`](test_hilow_game.py) — provided optional practice tests.

Do not modify the provided test file to make a failing test pass.

## 1. Make Sure the Program Runs

Before automated testing, run your optional program yourself from the repository root:

```bash
python3 src/hilow_game.py
```

On Windows, if your environment uses `python` rather than `python3`, use:

```powershell
python src/hilow_game.py
```

If Python reports a syntax or runtime error, return to the [Construct Phase](../src/README.md), correct one problem, and run the program again.

## 2. Test Manually

Across several runs, check the required behaviors:

- valid lower and upper bounds;
- invalid bounds followed by valid bounds;
- a guess below the selected range;
- a guess above the selected range;
- a valid guess below the target number;
- a valid guess above the target number;
- a correct guess; and
- several guesses before the correct guess.

Because the target number is random, you may need more than one normal run to exercise every path.

Compare actual behavior with the SRS, your pseudocode, and the official Sample Output.

## 3. Optional: Run the Practice Tests

The provided [`test_hilow_game.py`](test_hilow_game.py) script uses controlled input and a controlled target number so several paths can be checked repeatably.

You have not studied Python testing yet. You are not expected to understand or modify all of the test code.

From the repository root, run:

```bash
python3 tests/test_hilow_game.py
```

The practice tests intentionally check only selected structural behavior. They do not require one exact set of prompt or output sentences.

They assume you keep the provided `randint` import in `src/hilow_game.py`. If you intentionally change that starter structure, use manual testing instead.

> [!NOTE]
> These optional tests are not part of the active student Assignment Checks. A student can receive a green repository check without completing the optional Python program.

## 4. Interpret the Results

### All Tests Pass

A passing test is normally reported as `ok`, and a fully passing run ends with `OK`.

That means the optional implementation satisfied the behaviors covered by these repository practice tests.

It does **not** mean:

- your pseudocode has been graded;
- every rubric criterion is automatically satisfied; or
- the assignment has been submitted.

### A Test Fails

Read:

1. the failing test name;
2. the behavior that the test expected; and
3. any program output or assertion message shown.

Then compare the same case with:

- the SRS;
- your pseudocode; and
- your Python code.

Find the **first place** where they stop agreeing.

### The Program Has a Python Error

If the program cannot run normally, the test output may report `ERROR` or show a Python traceback.

Read the last part of the error information, correct one problem in `hilow_game.py`, run the program manually, and then rerun the tests.

Do not edit `test_hilow_game.py` simply to remove a failure.

## 5. Debug One Problem at a Time

Testing is iterative:

> **Test → Find a problem → Correct → Retest**

A useful debugging sequence is:

1. reproduce one failing behavior manually;
2. check what the SRS requires;
3. trace the same behavior through your pseudocode;
4. compare those steps with the Python implementation;
5. identify the first mismatch;
6. correct the appropriate artifact; and
7. retest before changing anything else.

If coding reveals a design error, revise the graded pseudocode first and then bring the optional implementation back into alignment.

## 6. Check Your Work

- [ ] The optional program runs without a Python error.
- [ ] I checked valid and invalid bound behavior.
- [ ] I checked out-of-range guess behavior.
- [ ] I checked too-low and too-high valid guesses.
- [ ] I checked a correct guess.
- [ ] I checked repeated guessing before success.
- [ ] My program behavior remains consistent with my pseudocode.
- [ ] If a test failed, I corrected the cause rather than modifying the provided test.
- [ ] If I changed the graded pseudocode, I reviewed it again against the official rubric.

## Help and Support

If you have difficulty:

- Review the [SRS behavior verification cases](../analysis/hilow_game_srs.md#4-behavior-verification-cases).
- Review [Construct](../src/README.md) for syntax, indentation, and incremental-development guidance.
- See the [Module Four Assignment Wiki](https://github.com/GC-STEM/it140-m4-assignment/wiki) for supplemental testing and debugging explanations.
- Use [GitHub Discussions](https://github.com/GC-STEM/it140-m4-assignment/discussions) for questions about optional practice tools.
- Use [GitHub Issues](https://github.com/GC-STEM/it140-m4-assignment/issues) to report a technical problem with the provided test file or repository checks.
- Contact your instructor through D2L Brightspace for assignment requirements, grading, or feedback.

## Next Step

Return to [Submit Your Assignment](../README.md#3-submit-your-assignment). Only `design/hilow_game.pseudo` is required for the Module Four submission.

<!-- Artifact Metadata

* Course: IT 140 - Introduction to Scripting
* Artifact Title: Module Four Assignment | Test Phase
* Artifact Type: Optional Python testing-practice guidance
* Artifact Purpose: Help students test and debug the optional Higher/Lower Game implementation while keeping testing outside the graded Module Four requirements.
* Artifact Version: {{semantic version number}}
* Artifact Date: {{artifact date in YYYY-MM-DD format}}
* Development Status: {{development status}}

-->
