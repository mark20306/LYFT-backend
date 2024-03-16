from tire.tire import Tire


class Carrigantires(Tire):
    def __init__(self,  tire_wear_array):
        self.tire_wear_array =  tire_wear_array
        
    def needs_service(self):
        for value in self.tire_wear_array:
            if value >= 0.9:
                return True
            return False
        