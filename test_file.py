import unittest
from project1 import load_penguin, get_measurements, calculate_average_body_mass_species, calculate_body_flipper_to_mass_ratio, analyze_bill_ratio_mass_relation

class TestAllMethods(unittest.TestCase):

    def setUp(self):
        self.penguins = load_penguin('penguins.csv')

    def test_calculate_average_body_mass_species(self):
        avg_body_mass_dict, heaviest_species_island, highest_avg_mass = calculate_average_body_mass_species(self.penguins)
        self.assertAlmostEqual(avg_body_mass_dict,[('Torgersen', 'Adelie')], 3706.37, places=2)
        self.assertEqual(heaviest_species_island, ('Biscoe', 'Gentoo'))
        self.assertAlmostEqual(highest_avg_mass, 5076.02, places=2)

# Before you begin writing the code for your calculation functions, please write four test cases
# per function. Two must test general/usual cases and two test edge cases