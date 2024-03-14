from Battery import Battery
from datetime import date

class NubbinBattery(Battery):
    def needs_service(self, last_service_date: date, current_date: date) -> bool:
        service_threshold_date = last_service_date.replace(year=last_service_date.year + 4)
        return current_date >= service_threshold_date