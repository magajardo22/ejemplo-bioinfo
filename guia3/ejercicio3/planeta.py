class Planeta:
    def __init__(self, masa, densidad, diametro, distancia_sol, id, nombre):
        self.__masa = masa
        self.__densidad = densidad
        self.__diametro = diametro
        self.__distancia_sol = distancia_sol
        self.id = id
        self.nombre = nombre

    def __str__(self):
        return f"{self.nombre} ({self.id}): Masa = {self.__masa} kg, Densidad = {self.__densidad} kg/m^3, Diámetro = {self.__diametro} km, Distancia al sol = {self.__distancia_sol} km"
    
class Sistema:
    def __init__(self, planetas):
        self.planetas = planetas

    def set_menu(self):
        print(" ")
        print("Información de los planetas del sistema solar:")
        print(" ")
        for planeta in self.planetas:
            print(f"{planeta.id}. {planeta.nombre}")
    
    def set_planeta(self, seleccion):
        for planeta in self.planetas:
            if planeta.id == seleccion:
                print(planeta)
                break
        else:
            print("Planeta no encontrado")



"""

class Planeta():

    def __init__(self, nombre, id, masa, densidad, diametro, distancia_sol):
        self.__nombre = nombre
        self.__id = id
        self.__masa = masa
        self.__densidad = densidad
        self.__diametro = diametro
        self.__distancia_sol = distancia_sol


    def get_info(self):
        print(f"Nombre: {self.__nombre}")
        print(f"ID: {self.__id}")
        print(f"Masa: {self.__masa} kg")
        print(f"Densidad: {self.__densidad} kg/m^3")
        print(f"Diametro: {self.__diametro} km")
        print(f"Distancia al Sol: {self.__distancia_sol} km")
        
class Sistema:
    def __init__(self, planetas=[]):
        self.__planetas = planetas
    
    def get_planeta(self):
        for planeta in self.__planetas:
            planeta.get_info()
            print()

    def set_planeta(self, planeta):
        self.__planetas.append(planeta)

"""

"""
    def get_nombre(self):
        return self.__nombre
    
    def set_nombre(self, nombre):
        if isinstance(nombre, str):
            self.__nombre = nombre
        else:
            print("El tipo de dato no es String")

    def get_id(self):
        return self.__id
    
    def set_id(self, id):
        if isinstance(id, int):
            self.__id = id
        else:
            print("El tipo de dato no es Int")

    def get_masa(self):
        return self.__masa
    
    def set_masa(self, masa):
        if isinstance(masa, str):
            self.__masa = masa
        else:
            print("El tipo de dato no es String")

    def get_densidad(self):
        return self.__densidad
    
    def set_densidad(self, densidad):
        if isinstance(densidad, float):
            self.__densidad = densidad
        else:
            print("El tipo de dato no es Float")

    def get_diametro(self):
        return self.__diametro
    
    def set_diametro(self, diametro):
        if isinstance(diametro, float):
            self.__diametro = diametro
        else:
            print("El tipo de dato no es Float")    

    def get_distancia_sol(self):
        return self.__distancia_sol
    
    def set_distancia_sol(self, distancia_sol):
        if isinstance(distancia_sol, int):
            self.__distancia_sol = distancia_sol
        else:
            print("El tipo de dato no es Int")  

"""     