"""Validate the intentional starter state of the Module Four assignment."""

from __future__ import annotations

import ast
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
SOURCE_PATH = REPO_ROOT / "src/hilow_game.py"
TEST_PATH = REPO_ROOT / "tests/test_hilow_game.py"
PSEUDOCODE_PATH = REPO_ROOT / "design/hilow_game.pseudo"

SOURCE_TODO_MARKERS = (
    "TODO: Replace with a one-line summary",
    "TODO: Identify the major user inputs.",
    (
        "TODO: Summarize validation, random selection, decisions, "
        "and repetition"
    ),
    "TODO: Identify the major categories of console output.",
    "TODO: Obtain and validate the lower and upper bounds.",
    "TODO: Generate a random number from the valid range using randint.",
    "TODO: Obtain and validate the player's first guess.",
    "TODO: Repeat until the player guesses the random number.",
    "TODO: Display a success message after the correct guess.",
)

PSEUDOCODE_TODO_MARKERS = (
    "TODO: Obtain the lower and upper bounds.",
    (
        "TODO: Use repetition and validation so the lower bound is less "
        "than the upper bound."
    ),
    "TODO: Generate the required random number from the valid range.",
    (
        "TODO: Obtain and validate a guess so it is within the selected "
        "range."
    ),
    (
        "TODO: Use a loop so guessing continues until the correct number "
        "is guessed."
    ),
    (
        "TODO: Use decision branching to handle a valid guess that is "
        "too low."
    ),
    "TODO: Handle a valid guess that is too high.",
    "TODO: Handle a correct guess.",
    (
        "TODO: Obtain and validate another guess when the game should "
        "continue."
    ),
)

EXPECTED_TEST_CASES = {
    "test_valid_bounds_are_used_for_random_number": (
        (10, 20, 17),
        17,
    ),
    "test_invalid_bounds_are_replaced_before_random_number": (
        (10, 5, 10, 20, 17),
        17,
    ),
    "test_incorrect_guesses_repeat_until_correct_guess": (
        (10, 20, 15, 19, 17),
        17,
    ),
}


class StarterChecks:
    """Collect starter validation failures."""

    def __init__(self) -> None:
        self.errors: list[str] = []

    def error(self, message: str) -> None:
        """Record a failing starter check."""
        self.errors.append(message)

    def finish(self) -> None:
        """Print results and exit nonzero when starter checks fail."""
        if not self.errors:
            print("PASS: Course starter state is intentionally incomplete.")
            print("PASS: Graded pseudocode template is intact.")
            print("PASS: Optional Python practice scaffolding is intact.")
            print("PASS: Optional practice-test definitions are intact.")
            return

        print("Course starter checks failed:", file=sys.stderr)
        for error in self.errors:
            print(f"- {error}", file=sys.stderr)
        raise SystemExit(1)


def is_docstring_statement(node: ast.stmt) -> bool:
    """Return True if a statement is a string-expression docstring."""
    return (
        isinstance(node, ast.Expr)
        and isinstance(node.value, ast.Constant)
        and isinstance(node.value.value, str)
    )


def check_source(checks: StarterChecks) -> None:
    """Verify the optional source stays a valid, incomplete starter."""
    text = SOURCE_PATH.read_text(encoding="utf-8")
    try:
        tree = ast.parse(text, filename=str(SOURCE_PATH))
    except SyntaxError as exc:
        checks.error(f"Optional starter source is not valid Python: {exc}")
        return

    for marker in SOURCE_TODO_MARKERS:
        if marker not in text:
            checks.error(f"Optional source is missing marker: {marker!r}")

    randint_imports = [
        node
        for node in tree.body
        if isinstance(node, ast.ImportFrom)
        and node.module == "random"
        and any(alias.name == "randint" for alias in node.names)
    ]
    if len(randint_imports) != 1:
        checks.error(
            "Optional starter must keep 'from random import randint'."
        )

    main_functions = [
        node
        for node in tree.body
        if isinstance(node, ast.FunctionDef) and node.name == "main"
    ]
    if len(main_functions) != 1:
        checks.error(
            "Optional starter must contain exactly one main() function."
        )
    else:
        body = main_functions[0].body
        if len(body) != 1 or not is_docstring_statement(body[0]):
            checks.error(
                "Optional starter main() must remain intentionally incomplete; "
                "only its docstring should be executable."
            )

    guards = [
        node
        for node in tree.body
        if isinstance(node, ast.If)
        and "__name__" in ast.unparse(node.test)
        and "__main__" in ast.unparse(node.test)
    ]
    if len(guards) != 1:
        checks.error("Optional starter must contain one __main__ guard.")
    else:
        calls_main = any(
            isinstance(node, ast.Expr)
            and isinstance(node.value, ast.Call)
            and isinstance(node.value.func, ast.Name)
            and node.value.func.id == "main"
            for node in guards[0].body
        )
        if not calls_main:
            checks.error("The __main__ guard must call main().")


def check_pseudocode(checks: StarterChecks) -> None:
    """Verify the graded pseudocode template markers remain intact."""
    text = PSEUDOCODE_PATH.read_text(encoding="utf-8")
    if "START hilow_game" not in text or "END hilow_game" not in text:
        checks.error(
            "Pseudocode starter must keep START and END hilow_game."
        )

    for marker in PSEUDOCODE_TODO_MARKERS:
        if marker not in text:
            checks.error(
                f"Pseudocode starter is missing marker: {marker!r}"
            )


def run_game_case(
    function: ast.FunctionDef,
) -> tuple[tuple[int, ...], int] | None:
    """Return the controlled input and secret passed to self.run_game()."""
    for node in ast.walk(function):
        if not isinstance(node, ast.Call):
            continue
        if not isinstance(node.func, ast.Attribute):
            continue
        if node.func.attr != "run_game" or not node.args:
            continue

        try:
            inputs = tuple(ast.literal_eval(node.args[0]))
        except (ValueError, TypeError):
            continue

        secret = None
        for keyword in node.keywords:
            if keyword.arg != "secret":
                continue
            try:
                secret = ast.literal_eval(keyword.value)
            except (ValueError, TypeError):
                secret = None
            break

        if secret is not None:
            return inputs, secret

    return None


def check_tests(checks: StarterChecks) -> None:
    """Verify the optional practice-test suite still has three cases."""
    text = TEST_PATH.read_text(encoding="utf-8")
    try:
        tree = ast.parse(text, filename=str(TEST_PATH))
    except SyntaxError as exc:
        checks.error(f"Practice-test file is not valid Python: {exc}")
        return

    test_class = next(
        (
            node
            for node in tree.body
            if isinstance(node, ast.ClassDef)
            and node.name == "HigherLowerGamePracticeTests"
        ),
        None,
    )
    if test_class is None:
        checks.error(
            "Practice-test class HigherLowerGamePracticeTests missing."
        )
        return

    test_functions = {
        node.name: node
        for node in test_class.body
        if isinstance(node, ast.FunctionDef)
        and node.name.startswith("test_")
    }

    actual = set(test_functions)
    expected = set(EXPECTED_TEST_CASES)
    if actual != expected:
        missing = sorted(expected - actual)
        extra = sorted(actual - expected)
        if missing:
            checks.error(f"Practice tests are missing: {', '.join(missing)}")
        if extra:
            checks.error(
                f"Unexpected practice tests found: {', '.join(extra)}"
            )

    for test_name, expected_case in EXPECTED_TEST_CASES.items():
        function = test_functions.get(test_name)
        if function is None:
            continue

        actual_case = run_game_case(function)
        if actual_case != expected_case:
            checks.error(
                f"Controlled practice case changed in {test_name}; "
                f"expected {expected_case}."
            )

    required_markers = (
        'PROJECT_ROOT / "src" / "hilow_game.py"',
        '"builtins.input"',
        'patch.object(',
        '"randint"',
    )
    for marker in required_markers:
        if marker not in text:
            checks.error(
                f"Practice-test scaffolding is missing marker: {marker!r}"
            )


def main() -> None:
    """Run all course-starter checks."""
    checks = StarterChecks()
    check_source(checks)
    check_pseudocode(checks)
    check_tests(checks)
    checks.finish()


if __name__ == "__main__":
    main()
