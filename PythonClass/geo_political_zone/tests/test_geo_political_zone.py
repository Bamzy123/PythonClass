import unittest
from gps.political_zone import GeoPolitical


class TestGeoPoliticalZone(unittest.TestCase):
    def test_north_central_states(self):
        self.assertEqual(
            GeoPolitical.get_political_zone("Benue"),
            "North Central"
        )
        self.assertEqual(
            GeoPolitical.get_political_zone("Fct"),
            "North Central"
        )

    def test_north_east_states(self):
        self.assertEqual(
            GeoPolitical.get_political_zone("Bauchi"),
            "North East",
        )

    def test_north_west_states(self):
        self.assertEqual(
            GeoPolitical.get_political_zone("Kano"),
            "North West",
        )

    def test_south_east_states(self):
        self.assertEqual(
            GeoPolitical.get_political_zone("Anambra"),
            "South East",
        )

    def test_south_south_states(self):
        self.assertEqual(
            GeoPolitical.get_political_zone("Edo"),
            "South South",
        )

    def test_south_west_states(self):
        self.assertEqual(
            GeoPolitical.get_political_zone("Lagos"),
            "South West",
        )

    def test_unrecognized_state(self):
        self.assertIsNone(
            GeoPolitical.get_political_zone("InvalidState"),
        )

if __name__ == '__main__':
    unittest.main()
