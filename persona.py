class Persona():
    def __init__(self, nombre = "pepe", apellido = "anastasio", dni = 454645646):
        self.__nombre__ = nombre
        self.__apellido__ = apellido
        self.__dni__ = dni
    
    def mostar_datos(self):
        print(f"Mis datos son nombre: {self.__nombre__}, apellido: {self.__apellido__}, dni: {self.__dni__}")