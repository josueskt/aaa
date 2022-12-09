from acount import Cuenta
from acount_driver import driver
from acoun_User import User
from car import Car
from payment import Pago
from transfer import Transfer
from Route import Route
from trip import Trip
from uberfx import uberx
from ubercomfort import  ubercomfort
from uberX import uberx 


if __name__ == "__main__" : 
    usuario_1 = User(1, "romeo", "masculino", 22222 , 999)
    user_2 = User("josue", "homero", 1212121 , 233222 , 999)
    carro_1 = Car("xlxx", "2000","red" ,  driver("homero", "masculino",100, 233222 , 999 , 9998))
    ubercomf = ubercomfort("xlxx", "2000","red" , 10, driver("jhon", "masculino",100, 233222 , 999 , 9998))
    print (vars(ubercomf))
    print (vars(ubercomf.Drive))
    
    print (vars(carro_1))
    print (vars(carro_1.Drive)) 
    