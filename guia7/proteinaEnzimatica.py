from proteina import Proteina

class ProteinaEnzimatica(Proteina):
    def __init__(self, nombre, descripcion, secuencia, substrato):
        super().__init__(nombre, descripcion, secuencia)
        self.__substrato = substrato

    def mostrarSubtrato(self):
        print(f"El substrato de {self.get_nombre()} es {self.__substrato}")

    def get_substrato(self):
        return self.__substrato

    def set_substrato(self, substrato):
        if isinstance(substrato, str):
            self.__substrato = substrato
    