from proteina import Proteina

class ProteinaMutante(Proteina):
    def __init__(self, nombre, mutacion):
        super().__init__(nombre, mutacion)
        self.__mutacion = mutacion

    def mostrarMutacion(self):
        print(f"la mutacion de {self.get_nombre()} es {self.__mutacion}")

    def get_mutacion(self):
        return self.__mutacion

    def set_mutacion(self, mutacion):
        if isinstance(mutacion, str):
            self.__mutacion = mutacion