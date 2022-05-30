import unittest
from models.city import City

class TestCity(unittest.TestCase):

    def setUp(self):
        self.city1 = City("Rome", "Italy", True)
        self.city2 = City("Berlin", "Germany", False)

    def test_city_has_name(self):
        self.assertEqual("Rome", self.city1.name)
        self.assertEqual("Berlin", self.city2.name)

    def test_city_has_country(self):
        self.assertEqual("Italy", self.city1.country)

    def test_city_has_been_visited(self):
        self.assertEqual(True, self.city1.visited)
        
    def test_city_can_be_marked_as_visited(self):
        self.city2.mark_visited()
        self.assertEqual(True, self.city2.visited)