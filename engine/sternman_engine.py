'''from abc import ABC

from car import Car


class SternmanEngine(Car, ABC):
    def __init__(self, last_service_date, warning_light_is_on):
        super().__init__(last_service_date)
        self.warning_light_is_on = warning_light_is_on

    def engine_should_be_serviced(self):
        if self.warning_light_is_on:
            return True
        else:
            return False'''

from Engine import Engine
from datetime import date

class SternmanEngine(Engine):
    def needs_service(self, last_service_date: date, current_date: date, current_mileage: int, last_service_mileage: int, warning_light_is_on: bool) -> bool:
        service_threshold_date = last_service_date.replace(year=last_service_date.year + 4)
        return service_threshold_date < current_date or warning_light_is_on
