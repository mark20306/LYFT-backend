'''from abc import ABC

from car import Car


class WilloughbyEngine(Car, ABC):
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        super().__init__(last_service_date)
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def engine_should_be_serviced(self):
        return self.current_mileage - self.last_service_mileage > 60000'''

from Engine import Engine
from datetime import date

class WilloughbyEngine(Engine):
    def needs_service(self, last_service_date: date, current_date: date, current_mileage: int, last_service_mileage: int) -> bool:
        service_threshold_date = last_service_date.replace(year=last_service_date.year + 2)
        return service_threshold_date < current_date or current_mileage - last_service_mileage > 60000
