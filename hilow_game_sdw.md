<!-- To see this file in a clean, formatted view, right-click on the filename and choose "Open Preview." -->

# Software Development Worksheet (SDW)

- **Course:** IT 140 - *Introduction to Scripting*
- **Activity:** Module Four Assignment
- **Program:** Higher/Lower Game

> Use this worksheet as optional working notes while you move through the **Analyze** and **Design** phases of the simplified Software Development Life Cycle (SDLC).
>
> Your notes do not need to be formal or polished. Keep answers brief and write them in your own words. The purpose of the SDW is to help you understand the requirements and plan your own graded pseudocode.
>
> Look for **TODO** prompts. Replace them with your own answers if you use this worksheet.
>
> **This worksheet is not a graded deliverable.** Do not submit it in D2L Brightspace unless your instructor specifically asks for it.

## How to Use This Worksheet

The worksheet uses the same pattern throughout:

- **Where to look** tells you where to find the information you need.
- **Prompt** tells you what to think about or answer.
- Your response goes immediately after the prompt.

The worksheet intentionally asks questions instead of supplying the completed Higher/Lower Game algorithm. Your graded `design/hilow_game.pseudo` should contain **your** design.

# Analyze Phase

## 1. Describe the Problem

**Where to look:** Module Four Assignment Guidelines and Rubric → Overview, Scenario, and Prompt.

**Prompt:** In one or two sentences, describe what the program needs to accomplish for Maria and Bella.

**Your notes:**

TODO: Summarize the program purpose in your own words.

## 2. Identify Inputs and Outputs

**Where to look:** Guidelines and Rubric → Prompt; Higher/Lower Game Sample Output; SRS FR-1, FR-5, and FR-9.

**Prompt:** What information must come from the player, and what categories of information must the program communicate?

**Inputs:**

- TODO: Identify the range inputs.
- TODO: Identify the repeated game input.

**Outputs:**

- TODO: Identify the required categories of output.

Do not choose exact message wording yet unless it helps you reason about the behavior.

## 3. Identify Validation Requirements

**Where to look:** Guidelines and Rubric → Prompt; SRS FR-2, FR-3, FR-6, and FR-7.

**Prompt:** Describe each input-validation rule in plain language and what should happen when the rule is not satisfied.

**Your notes:**

- TODO: Bounds validation rule and response.
- TODO: Guess validation rule and response.

## 4. Identify Processing and Decisions

**Where to look:** Guidelines and Rubric → Prompt; SRS FR-4, FR-8, and FR-9.

**Prompt:** What value must the program generate, and what possible relationships between a valid guess and that value must the design distinguish?

**Your notes:**

- TODO: Generated value.
- TODO: Required valid-guess outcomes.

## 5. Identify Repeated Behavior

**Where to look:** Guidelines and Rubric → Prompt; SRS FR-3, FR-7, FR-10, and FR-11.

**Prompt:** What work can repeat? For each repeated part, what condition causes repetition and what condition lets the program continue or stop?

**Your notes:**

- TODO: Bounds-related repetition.
- TODO: Guess-validation repetition.
- TODO: Game repetition and stopping condition.

## 6. Distinguish Requirements From Extra Features

**Where to look:** SRS → Out of Scope Unless Your Instructor Adds a Requirement.

**Prompt:** List one or two features you might be tempted to add that are not required by the assignment.

**Your notes:**

- TODO: Optional feature that should not become a graded requirement.
- TODO: Another optional feature, or delete this line.

## 7. Analyze Checkpoint

Before moving to Design:

- [ ] I can explain the game's purpose in my own words.
- [ ] I identified the required player inputs.
- [ ] I identified the required categories of output.
- [ ] I can explain both validation requirements.
- [ ] I know when the random number is generated.
- [ ] I can explain the too-low, too-high, and correct outcomes.
- [ ] I can identify the repeated behaviors and their stopping conditions.
- [ ] I did not turn optional features into assignment requirements.

# Design Phase

## 8. Plan the Major Stages

**Where to look:** Your Analyze notes, SRS, and `design/hilow_game_sdd.md`.

**Prompt:** List the major stages of the game in order without writing the completed pseudocode here.

**Your notes:**

1. TODO
2. TODO
3. TODO
4. TODO
5. TODO

## 9. Plan Validation Before Detailed Pseudocode

**Where to look:** Your Analyze notes and SDD → Validation and Decision Branching.

**Prompt:** For each validation requirement, explain what information is checked and how the program can eventually receive acceptable input.

**Your notes:**

- TODO: Bounds-validation plan.
- TODO: Guess-validation plan.

## 10. Plan Repetition

**Where to look:** Your Analyze notes and SDD → Repetition and Stopping Conditions.

For each repeated section, answer:

- What condition is checked?
- What happens during one repetition?
- What information can change?
- What stops the repetition?

**Your notes:**

TODO: Summarize the loop structure in words without writing the completed pseudocode.

## 11. Plan Decision Branching

**Where to look:** SRS FR-8 and FR-9.

**Prompt:** What outcomes must the valid-guess comparison distinguish, and what should happen after each outcome?

**Your notes:**

TODO: Identify the required outcomes without writing completed branch statements.

## 12. Requirements-to-Design Traceability

After drafting `design/hilow_game.pseudo`, locate where your design addresses each requirement group.

| Requirement group | Where it appears in your pseudocode |
| --- | --- |
| Bounds input and validation | TODO |
| Random-number generation | TODO |
| Guess input and validation | TODO |
| Too-low / too-high / correct decisions | TODO |
| Repetition until correct | TODO |
| Required outputs | TODO |

If a required behavior has no corresponding design step, revise the pseudocode.

## 13. Trace a Behavior by Hand

**Where to look:** SRS → Behavior Verification Cases and the official Sample Output.

Choose one scenario that includes repetition or validation. Follow your pseudocode one statement at a time.

**Scenario:** TODO

**Trace notes:**

TODO: Record the path through your pseudocode and what causes each branch or loop decision.

## 14. Rubric Review

### Logical Steps — 35%

- [ ] My design logically outlines the complete required program.
- [ ] Another programmer could follow the order of the steps.
- [ ] I represented all required functionality.

### Input/Output — 30%

- [ ] I represented both bound inputs.
- [ ] I represented guess input.
- [ ] I represented required feedback and success output.

### Program Flow — 35%

- [ ] I used decision branching for the valid-guess outcomes.
- [ ] I used loops for required repeated behavior.
- [ ] Each loop has an understandable stopping condition.
- [ ] Indentation shows which statements belong inside branches and loops.

## 15. Design Checkpoint

- [ ] Valid bounds are established before the target number is generated.
- [ ] Invalid bounds can lead to new bound input.
- [ ] A guess is validated against the selected range.
- [ ] An invalid guess can lead to another guess.
- [ ] Too-low and too-high valid guesses allow play to continue.
- [ ] A correct guess ends the guessing process.
- [ ] No starter `TODO:` prompts remain in the graded pseudocode.

## 16. Ready to Submit

Before submission:

- [ ] I reviewed the current Module Four Assignment Guidelines and Rubric.
- [ ] I reviewed the official Higher/Lower Game Sample Output.
- [ ] I traced multiple required behaviors through my pseudocode.
- [ ] I saved the graded file as `design/hilow_game.pseudo`.
- [ ] I understand that only the `.pseudo` file is required for submission.

# Optional Construct and Test Notes

Complete the remaining sections only if you choose the optional Python practice after your graded pseudocode is ready.

## 17. Construct Notes — Optional

Open [`src/README.md`](src/README.md) and translate **your own completed pseudocode** into `src/hilow_game.py`.

| Design idea | Python concept you used |
| --- | --- |
| User input | TODO |
| Bounds validation | TODO |
| Random number | TODO |
| Guess validation | TODO |
| Decision branching | TODO |
| Repetition | TODO |
| Output | TODO |

## 18. Test Notes — Optional

Open [`tests/README.md`](tests/README.md).

| Scenario | Expected behavior | Actual behavior | Pass? |
| --- | --- | --- | :---: |
| TODO | TODO | TODO | TODO |
| TODO | TODO | TODO | TODO |
| TODO | TODO | TODO | TODO |

If testing exposes a design problem, revise the graded pseudocode first and then update the optional Python implementation.
