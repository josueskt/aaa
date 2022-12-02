from padre import persona
class doc(persona): 
    titulo      = str
    edad        = int
    experiencia_p = int
    experiencia_D = int
    def __init__(self, nombre, apellido , titulo , edad , experiencia_p, experiencia_D):
        super().__init__(nombre, apellido) 
        self.titulo = titulo
        self.edad  = edad
        self.experiencia_D = experiencia_D
        self.experiencia_p = experiencia_p
        
    def welcome (self):
        print( "hola "+ self.nombre +" " + self.apellido + "expreciencia total " + str(self.experiencia_D + self.experiencia_p))
        
docente1 = doc("dayan" , "tafur ", "estudiante" , 32 , 2,1)
docente1.welcome()