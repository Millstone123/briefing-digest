import unittest

from briefing_digest.cli import main


class CliTests(unittest.TestCase):
    def test_summarise_this_workflow(self):
        self.assertEqual(main(["summarise", "this"]), 0)


if __name__ == "__main__":
    unittest.main()
