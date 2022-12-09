from acount_driver import driver
class Car : 
    placa = str
    ao = int
    color = str
    conducor = str
    def __init__(self , placa , ao , color , conductor , driver):
        super().__init__ 
        self.placa = placa
        self.ao= ao
        self.color = color 
        self.conducor = conductor 
        self.driver = driver
        
    