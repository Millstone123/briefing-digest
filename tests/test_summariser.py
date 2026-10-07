import unittest

from briefing_digest.summarizer import summarise


class SummariserTests(unittest.TestCase):
    def test_digest_is_deterministic(self):
        text = "One idea leads here. Two details support it. One idea leads here. Three conclusions follow."
        self.assertEqual(summarise(text, limit=2), summarise(text, limit=2))

    def test_empty_text_has_empty_digest(self):
        self.assertEqual(summarise("  "), "")


if __name__ == "__main__":
    unittest.main()
