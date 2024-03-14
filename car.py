'''from abc import ABC, abstractmethod


class Car(ABC):
    def __init__(self, last_service_date):
        self.last_service_date = last_service_date

    @abstractmethod
    def needs_service(self):
        pass'''

from datetime import date
from Engine import Engine
from Battery import Battery

class Car:
    def __init__(self, engine: Engine, battery: Battery, last_service_date: date):
        self.engine = engine
        self.battery = battery
        self.last_service_date = last_service_date

    def needs_service(self, current_date: date, current_mileage: int, last_service_mileage: int, warning_light_is_on: bool = False) -> bool:
        return self.engine.needs_service(self.last_service_date, current_date, current_mileage, last_service_mileage, warning_light_is_on) or \
               self.battery.needs_service(self.last_service_date, current_date)