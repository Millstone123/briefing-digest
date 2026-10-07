import unittest

from briefing_digest.cli import REQUEST, main


class CliTests(unittest.TestCase):
    def test_exact_request(self):
        self.assertEqual(REQUEST, "summarise thise")
        self.assertEqual(main([REQUEST]), 0)


if __name__ == "__main__":
    unittest.main()
