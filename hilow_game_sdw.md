# Software Development Worksheet (SDW)

- **Course**: IT 140 - Introduction to Scripting
- **Activity**: Module Four Assignment
- **Program**: Higher/Lower Game
- **Purpose**: Optional working notes for moving through the full SDLC

> [!NOTE]
> This worksheet is a learning aid. It is **not a graded deliverable** and should not be submitted unless your instructor specifically asks for it. Keep your answers brief. The graded work belongs in `design/hilow_game.pseudo`.

## SDLC Progress

> **Analyze → Design → Construct → Test**

For this assignment, **pseudocode in the Design phase is graded**. Construct and Test are included as optional practice so you can experience the complete sequence.

---

## 1. Analyze

Use the Module Four Assignment Guidelines and Rubric, the Higher/Lower Game Sample Output, and [`analysis/hilow_game_srs.md`](analysis/hilow_game_srs.md).

### 1.1 Purpose in Your Own Words

In one or two sentences, describe what the higher/lower game needs to accomplish.

**Your notes:**

TODO: Write your own summary here.

### 1.2 Inputs

What information must the program receive from the player?

**Your notes:**

- TODO: Identify the range inputs.
- TODO: Identify the repeated game input.

### 1.3 Validation Rules

What makes a pair of bounds valid? What makes a guess valid?

**Your notes:**

- TODO: Bound validation rule
- TODO: Guess validation rule
- TODO: What the program should do when input does not satisfy each rule

### 1.4 Processing and Decisions

What information must the program generate, and what comparisons determine the feedback shown to the player?

**Your notes:**

- TODO: Random value the program needs
- TODO: Decision outcomes the design must distinguish

### 1.5 Repetition

What work must repeat, and what condition causes each loop to stop?

**Your notes:**

- TODO: Bounds-validation repetition
- TODO: Guessing-game repetition

### 1.6 Outputs

What kinds of information must the program communicate to the player?

**Your notes:**

TODO: Identify the required categories of output without choosing exact wording yet.

### Analyze Checkpoint

Before continuing, verify that you can explain:

- [ ] Why the lower bound must be less than the upper bound
- [ ] What value the program generates after valid bounds are established
- [ ] What makes a guess valid
- [ ] What happens when a guess is too low
- [ ] What happens when a guess is too high
- [ ] What happens when a guess is correct
- [ ] Why the guessing process needs a loop

---

## 2. Design

The pseudocode file is the **graded deliverable**. Use this section only to plan before editing it.

### 2.1 Sequence Plan

List the major stages of the game in order without writing the completed pseudocode here.

**Your notes:**

1. TODO
2. TODO
3. TODO
4. TODO
5. TODO

### 2.2 Loop Plan

For each repeated part of the program, identify:

- What begins the repetition
- What condition is checked
- What changes during each repetition
- What causes the repetition to stop

**Your notes:**

TODO: Summarize the loop structure in words.

### 2.3 Branch Plan

What outcomes must the guess comparison distinguish?

**Your notes:**

TODO: Identify the outcomes without writing the completed branch statements.

### 2.4 Design Review

After completing the graded pseudocode, verify:

- [ ] Valid bounds are established before the secret number is generated.
- [ ] Invalid bounds cause the program to obtain bounds again.
- [ ] The random number is generated from the selected range.
- [ ] A guess is obtained and checked against the selected range.
- [ ] Out-of-range guesses are handled through validation.
- [ ] Too-low and too-high guesses produce appropriate feedback.
- [ ] The player can guess again after an incorrect valid guess.
- [ ] A correct guess ends the guessing loop.
- [ ] Indentation makes the branch and loop structure clear.

---

## 3. Construct — Optional Practice

Complete this section only if you choose to implement your pseudocode in Python.

Open [`src/README.md`](src/README.md), then use your **own completed pseudocode** to complete `src/hilow_game.py`.

### 3.1 Design-to-Code Mapping

As you code, note how your pseudocode maps to Python concepts.

| Design idea | Python concept you used |
| --- | --- |
| User input | TODO |
| Bound validation | TODO |
| Random number | TODO |
| Guess validation | TODO |
| Decision branching | TODO |
| Repetition | TODO |
| Output | TODO |

### 3.2 Construction Checkpoint

- [ ] I completed the graded pseudocode before coding.
- [ ] My Python program follows my pseudocode.
- [ ] I used loops for repeated behavior instead of copying the same statements many times.
- [ ] My program runs without a syntax error for a normal input sequence.

---

## 4. Test — Optional Practice

Complete this section only if you constructed the optional Python program.

Open [`tests/README.md`](tests/README.md).

### 4.1 Manual Test Notes

Include normal, invalid-bound, out-of-range-guess, too-low, too-high, and correct-guess behavior across your tests.

| Scenario | Test input or condition | Expected result | Actual result | Pass? |
| --- | --- | --- | --- | :---: |
| TODO | TODO | TODO | TODO | TODO |
| TODO | TODO | TODO | TODO | TODO |
| TODO | TODO | TODO | TODO | TODO |

### 4.2 Debugging Notes

If a test did not pass, what did you change?

**Your notes:**

TODO: Record a brief debugging note, or write `No changes needed`.

### 4.3 Final SDLC Check

- [ ] Analyze: I understand the requirements and sample behavior.
- [ ] Design: My pseudocode meets the assignment rubric.
- [ ] Construct (optional): My code follows my pseudocode.
- [ ] Test (optional): I checked the code with multiple paths and invalid-input cases.

Return to the [top-level README](README.md#submit-your-assignment) for submission instructions.
