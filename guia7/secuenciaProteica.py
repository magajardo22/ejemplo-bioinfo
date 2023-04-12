from proteinaEnzimatica import ProteinaEnzimatica
from proteinaEstructural import ProteinaEstructural
from proteina import Proteina
import random
class SecuenciaProteica(Proteina):
    def __init__(self, nombre, secuencia):
        super().__init__(nombre, secuencia)


        """
        lista = [{"HIS":"H","ARG":"R","LYS":"K","GLU":"E","ASP":"D","GLN":"Q","ASG":"N","TRE":"T","CYS":"C","SER":"S","TRP":"W","TRY":"Y","PHE":"F","PRO":"P","MET":"M","ILE":"I","LEU":"L","VAL":"V","ALA":"A","GLI":"G"}]
        self.__lista = lista
        """
    def mostrarSecuencia(self):
        sec =""
        count = 0
        L = ["HIS","ARG","LYS","GLU","ASP","GLN","ASG","TRE","CYS","SER","TRP",
            "TRY","PHE","PRO","MET","ILE","LEU","VAL","ALA","GLI"]
        amount = random.randint(1,100)

        for i in range(amount):
            count = count + 1
            sec = sec + random.choice(L)
            if count != amount:
                sec = sec + ","

        print(f"la secuencia es: {sec}")
    