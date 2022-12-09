from payment import Pago
class Transfer(Pago): 
    cuenta =  int
    banco = str
    datost = []
    
    
    def __init__(self, id, fecha, valor):
        super().__init__(id, fecha, valor)