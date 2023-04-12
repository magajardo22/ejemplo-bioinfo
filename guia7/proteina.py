class Proteina():
    def __init__(self, nombre,descripcion, secuencia):
        self.__nombre = nombre
        self.__descripcion = descripcion
        self.__secuencia = secuencia

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        if isinstance(nombre, str):
            self.__nombre = nombre
        else:
            print("El nombre no ha sido posible de agregar")

    def get_descripcion(self):
        return self.__descripcion

    def set_descripcion(self, descripcion):
        if isinstance(descripcion, str):
            self.__descripcion = descripcion

    def get_secuencia(self):
        return self.__secuencia

    def set_secuencia(self, secuencia):
        if isinstance(secuencia, str):
            self.__secuencia = secuencia


