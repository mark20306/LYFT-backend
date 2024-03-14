from abc import ABC, abstractmethod
from datetime import date

class Engine(ABC):
    @abstractmethod
    def needs_service(self, last_service_date: date, current_date: date, current_mileage: int, last_service_mileage: int) -> bool:
        pass
