from datetime import date
from car import Car
from engine.capulet_engine import CapuletEngine
from engine.nubbin_battery import NubbinBattery
from engine.spindler_battery import SpindlerBattery
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine

class CarFactory:
    @staticmethod
    def create_calliope(last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        return Car(CapuletEngine(), SpindlerBattery(), last_service_date)
    
    @staticmethod
    def create_glissade(last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        return Car(WilloughbyEngine(), SpindlerBattery(), last_service_date)
    
    @staticmethod
    def create_palindrome(last_service_date: date, warning_light_is_on: bool) -> Car:
        return Car(SternmanEngine(), SpindlerBattery(), last_service_date)
    
    @staticmethod
    def create_rorschach(last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        return Car(WilloughbyEngine(), NubbinBattery(), last_service_date)
    
    @staticmethod
    def create_thovex(last_service_date: date, current_mileage: int, last_service_mileage: int) -> Car:
        return Car(CapuletEngine(), NubbinBattery(), last_service_date)

