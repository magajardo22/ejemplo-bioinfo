class Vacunas():
    def __init__(self):
        self.__nombre = None
        self.__lab = None
        self.__efectos = []

    def get_nombre(self):
        return self.__nombre

    def set_nombre(self, nombre):
        if isinstance(nombre, str):
            self.__nombre = nombre
        else:
            print("El tipo de dato no es String")

    def get_lab(self):
        return self.__lab

    def set_lab(self, lab):
        if isinstance(lab, str):
            self.__lab = lab
        else:
            print("El tipo de dato no es String")

    def set_efecto_secundario(self, efecto):
        self.__efectos.append(efecto)

    def get_efectos_secundarios(self):
        for efecto in self.__efectos:
            print(efecto)