class persona: 
    nombre = str
    apellido = str
    def __init__(self , nombre , apellido):
        self.nombre = nombre
        self.apellido = apellido
    def imprimir (self):
        print(self.nombre)
x = persona ("alex ", "flore")
x.imprimir()

class estudiante(persona):
    pass

y = estudiante("adasdas","asdsad")
y.imprimir()
# herencia simnple de python
class student(persona):
    edad = int
    
    def __init__(self, nombre, apellido , edad):
        persona.__init__( self,nombre, apellido)
        self.edad = edad
        
estudiante1 = student("asdasd","asdasd",30)
estudiante1.imprimir()

#metodos 
class Studen( persona):
    edad     = int
    semestre =str
    
    def __init__(self, nombre, apellido , edad , semestre):
        super().__init__(nombre, apellido)
        
        self.edad     = edad
        self.semestre = semestre
    def bienvenido (self):
        
        print("hola" + self.apellido + "asdasd" + str(self.edad) + "años")
        
        
ps = Studen("hola" , "adasd", 30 , "asdasd")
ps.bienvenido()
     

        
 