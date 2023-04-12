from proteina import Proteina

class ProteinaEstructural(Proteina):
    def __init__(self, nombre, descripcion, secuencia, tipo):
        super().__init__(nombre, descripcion, secuencia)
        self.__tipo = tipo

    def mostrarTipo(self): #fibrosa o globular
        if self.__tipo == True:
            self.__tipo = "fibrosa"
            print(self.__tipo)
        else:
            self.__tipo = "globular"
            print(self.__tipo)
        
    def get_tipo(self):
        return self.__tipo

    def set_tipo(self, tipo):
        if isinstance(tipo, int):
            self.__tipo = tipo