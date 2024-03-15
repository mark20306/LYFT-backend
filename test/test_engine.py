import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine

class TestEngine(unittest.TestCase):
    def setUp(self) -> None:
        current_mileage = 70000
        last_service_mileage = 0
        warning_light_is_on = True
        self.capulet = CapuletEngine(current_mileage, last_service_mileage)
        self.sternman = SternmanEngine(warning_light_is_on)
        self.willoughby = WilloughbyEngine(current_mileage, last_service_mileage)

    def test_engine_needs_service(self):
        self.assertTrue(self.capulet.needs_service())
        self.assertTrue(self.sternman.needs_service())
        self.assertTrue(self.willoughby.needs_service())

    def test_engine_not_needs_service(self):
        current_mileage = 7000
        last_service_mileage = 0
        warning_light_is_on = False
        self.capulet = CapuletEngine(current_mileage, last_service_mileage)
        self.sternman = SternmanEngine(warning_light_is_on)
        self.willoughby = WilloughbyEngine(current_mileage, last_service_mileage)

        self.assertFalse(self.capulet.needs_service())
        self.assertFalse(self.sternman.needs_service())
        self.assertFalse(self.willoughby.needs_service())

if __name__ == '__main__':
    unittest.main()





