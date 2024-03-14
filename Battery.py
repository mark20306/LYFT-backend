from abc import ABC, abstractmethod
from datetime import date

class Battery(ABC):
    @abstractmethod
    def needs_service(self, last_service_date: date, current_date: date) -> bool:
        pass