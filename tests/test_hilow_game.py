"""Optional practice tests for the Module Four higher/lower game.

Run from the repository root:
    python3 tests/test_hilow_game.py

These tests are practice tools. They do not grade the Module Four Assignment.

The tests assume the optional starter keeps:
    from random import randint
"""

from contextlib import redirect_stdout
from io import StringIO
from pathlib import Path
from unittest.mock import patch
import importlib.util
import unittest


PROJECT_ROOT = Path(__file__).resolve().parents[1]
PROGRAM_PATH = PROJECT_ROOT / "src" / "hilow_game.py"


def load_program():
    """Load the optional practice program as a module."""
    spec = importlib.util.spec_from_file_location("hilow_game", PROGRAM_PATH)
    if spec is None or spec.loader is None:
        raise RuntimeError("Could not load src/hilow_game.py")

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


class HigherLowerGamePracticeTests(unittest.TestCase):
    """Check several observable behaviors in the optional program."""

    def run_game(self, inputs, secret):
        """Run main() with controlled input and a controlled secret number."""
        module = load_program()

        if not hasattr(module, "randint"):
            self.fail(
                "Keep the provided 'from random import randint' starter import "
                "to use these optional automated tests."
            )

        fake_output = StringIO()

        with (
            patch(
                "builtins.input",
                side_effect=[str(value) for value in inputs],
            ) as fake_input,
            patch.object(
                module,
                "randint",
                return_value=secret,
            ) as fake_randint,
            redirect_stdout(fake_output),
        ):
            module.main()

        return fake_input, fake_randint, fake_output.getvalue()

    def test_valid_bounds_are_used_for_random_number(self):
        """A valid range should be passed to the provided random operation."""
        _, fake_randint, _ = self.run_game([10, 20, 17], secret=17)
        fake_randint.assert_called_once_with(10, 20)

    def test_invalid_bounds_are_replaced_before_random_number(self):
        """Invalid bounds should not be used to generate the secret number."""
        _, fake_randint, _ = self.run_game(
            [10, 5, 10, 20, 17],
            secret=17,
        )
        fake_randint.assert_called_once_with(10, 20)

    def test_incorrect_guesses_repeat_until_correct_guess(self):
        """Incorrect guesses should repeat until the correct guess."""
        fake_input, _, _ = self.run_game(
            [10, 20, 15, 19, 17],
            secret=17,
        )

        self.assertGreaterEqual(
            fake_input.call_count,
            5,
            msg=(
                "Expected the program to keep obtaining guesses after "
                "incorrect valid guesses."
            ),
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
