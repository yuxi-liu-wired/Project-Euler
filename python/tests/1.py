import sys
import os

# Add the root directory of the project to sys.path
root_dir = os.path.join(os.path.dirname(__file__), "..")
sys.path.append(root_dir)

import unittest
from solution_1 import answer


class TestPrime(unittest.TestCase):
    def test_answer(self):
        self.assertEqual(answer(1000), 233168)


if __name__ == "__main__":
    unittest.main()
