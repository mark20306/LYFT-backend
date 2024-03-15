from datetime import datetime
import unittest
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from battery.nubbin_battery import NubbinBattery
from battery.spindler_battery import SpindlerBattery

class TestBattery(unittest.TestCase):
    def setUp(self) -> None:
        current_date = datetime(2024, 3, 15)
        last_service_date = datetime(2019, 3, 15)
        self.nubbin = NubbinBattery(current_date, last_service_date)
        self.spindler = SpindlerBattery(current_date, last_service_date)

    def test_battery_needs_service(self):
        self.assertTrue(self.nubbin.needs_service())
        self.assertTrue(self.spindler.needs_service())

    def test_battery_not_needs_service(self):
        current_date = datetime(2024, 3, 15)
        last_service_date = datetime(2023, 3, 15)
        self.nubbin = NubbinBattery(current_date, last_service_date)
        self.spindler = SpindlerBattery(current_date, last_service_date)

        self.assertFalse(self.nubbin.needs_service())
        self.assertFalse(self.spindler.needs_service())

if __name__ == '__main__':
    unittest.main()
