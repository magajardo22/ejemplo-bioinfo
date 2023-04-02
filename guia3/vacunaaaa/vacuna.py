class Vacuna:
    def __init__(self, nombre, laboratorio):
        self.nombre = nombre
        self.laboratorio = laboratorio
        self.efectos_secundarios = []

    def agregar_efecto_secundario(self, efecto):
        self.efectos_secundarios.append(efecto)

    def mostrar_efectos_secundarios(self):
        for efecto in self.efectos_secundarios:
            print(efecto)