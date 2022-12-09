from acount_driver import driver
class Car : 
    placa = str
    ao = int
    color = str
    Drive = driver("","","","","","")
   
    def __init__(self , placa , ao , color, driver):
        super().__init__ 
        self.placa = placa
        self.ao= ao
        self.color = color 
        
        self.Drive = driver
        
    