# Test Phase | Optional Practice

**SDLC progress:** [Start Here](../README.md) → [1 Analyze](../analysis/README.md) → [2 Design](../design/README.md) → [3 Construct (Practice)](../src/README.md) → **4 Test (Practice)** → [Submit](../README.md#submit-your-assignment)

## Purpose

Testing checks whether a constructed program behaves as its requirements and design say it should.

For the Module Four Assignment, testing Python code is **optional practice**. You do not submit the test file or optional Python program for grading.

## Before You Test

Complete this phase only if you chose to complete `src/hilow_game.py`.

First confirm that:

- Your graded pseudocode is complete.
- Your optional Python program runs for at least one normal input sequence.
- Your program behavior is intended to match your pseudocode.

## 1. Test Manually

Run the program:

```bash
python3 src/hilow_game.py
```

Use the official Higher/Lower Game Sample Output and the acceptance conditions in [`../analysis/hilow_game_srs.md`](../analysis/hilow_game_srs.md).

Across several runs, check:

- Valid lower and upper bounds
- Invalid bounds followed by valid bounds
- A guess below the selected range
- A guess above the selected range
- A valid guess below the random number
- A valid guess above the random number
- A correct guess
- Several guesses before the correct guess

Because the secret number is random, you may need more than one run to exercise every path.

## 2. Run the Optional Practice Tests

The provided [`test_hilow_game.py`](test_hilow_game.py) script uses controlled test input and a controlled secret number so several paths can be checked repeatably.

From the repository root:

```bash
python3 tests/test_hilow_game.py
```

The practice tests are intentionally limited. They check important structural behavior without requiring one exact set of prompt or output sentences.

They assume you use the provided `randint` import in `src/hilow_game.py`. If you intentionally change that starter structure, use manual testing instead.

## 3. Debug One Problem at a Time

If a test fails:

1. Read the failing case.
2. Run your program manually with a similar sequence.
3. Compare the behavior with the SRS and your pseudocode.
4. Identify the first step where they differ.
5. Make one small correction.
6. Run the test again.

If coding reveals a design error, revise the graded pseudocode so the design and optional implementation remain consistent.

## Check Your Work

- [ ] Invalid bounds cause another pair of bounds to be obtained.
- [ ] Valid bounds are used to generate the secret number.
- [ ] Out-of-range guesses are handled through validation.
- [ ] Too-low and too-high valid guesses allow the game to continue.
- [ ] A correct guess ends the guessing loop.
- [ ] The program behavior still matches the pseudocode.

## Next Step

Return to [Submit Your Assignment](../README.md#submit-your-assignment). Only the `.pseudo` file is required as the Module Four Assignment deliverable.
