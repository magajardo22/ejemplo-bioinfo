from proteinaEnzimatica import ProteinaEnzimatica
from proteinaEstructural import ProteinaEstructural
from proteinaMutante import ProteinaMutante
from proteina import Proteina

class AnalizadorProteico(Proteina):
    def __init__(self, nombre):
        super().__init__(nombre)
    
    def calcularPorcentaje(self):
        pass
