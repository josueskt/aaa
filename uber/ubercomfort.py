from car import  Car
class uberxl(Car): 
    asientos = int
    
    def __init__(self, placa, ao, color, conductor, driver , asientos):
        super().__init__(placa, ao, color, conductor, driver)
        self.asientos = asientos