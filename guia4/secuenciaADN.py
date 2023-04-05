class SecuenciaADN():
    def __init__(self):
        self.__ADN = None
        self.__longitud = None
        self.__inverso = None

    def get_ADN(self):
        return self.__ADN

    def set_ADN(self, ADN):
        if isinstance(ADN, str):
            self.__ADN = ADN
        else:
            print("El tipo de dato no es String")

    def get_longitud(self):
        return self.__longitud

    def set_longitud(self, longitud):
        if isinstance(longitud, str):
            total = len(longitud)
            print(total)

    def get_complemento_inverso(self):
        return self.__inverso

    def set_complemento_inverso(self, complemento):
        if isinstance(complemento, str):
            inverso = ""
            inverso_dict = { " A " : " T " , " T " : " A " , " G " : " C " , " C " : " G " }
            for i in range(total)
                let = complemento[total-1-i]
                inverso = inverso + inverso_dict.get(let, let)
            print(inverso)
