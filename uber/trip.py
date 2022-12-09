from car import Car
from acount_driver import driver
from acoun_User import User
from Route import Route
from payment import Pago

class Trip (Car, driver, User, Route, Pago): 
    id_trip = int
    def __init__(self, placa, ao, color, conductor, driver , id_trip):
        super().__init__(placa, ao, color, conductor, driver)
        self.id_trip = id_trip
        

