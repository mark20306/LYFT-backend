from tire.tire import Tire


class Octoprimetires(Tire):
    def __init__(self,  tire_wear_array):
        self.tire_wear_array =  tire_wear_array
        
    def needs_service(self):
        if sum(self.tire_wear_array) >= 3:
            return True
        return False