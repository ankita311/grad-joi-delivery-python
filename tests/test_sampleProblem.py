import unittest
from problems.sampleProblem import SampleProblem


class TestSampleProblem(unittest.TestCase):
    def setUp(self):
        self.sample = SampleProblem()

    def test_calculate_cost_base(self):
        self.assertEqual(self.sample.calculate_cost(3), 50.0)
        self.assertEqual(self.sample.calculate_cost(5), 50.0)

    def test_calculate_cost_invalid(self):
        with self.assertRaises(ValueError):
            self.sample.calculate_cost(0)
        with self.assertRaises(ValueError):
            self.sample.calculate_cost(-2)
