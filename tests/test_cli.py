import unittest
from unittest.mock import patch

from briefing_digest.cli import REQUEST, main


class CliTests(unittest.TestCase):
    def test_exact_request(self):
        self.assertEqual(REQUEST, "summarise this")
        with patch("briefing_digest.cli.open_review_surface") as review:
            self.assertEqual(main([REQUEST]), 0)
        review.assert_called_once_with()

    def test_typo_is_rejected(self):
        with self.assertRaises(SystemExit):
            main(["summarise that"])


if __name__ == "__main__":
    unittest.main()
