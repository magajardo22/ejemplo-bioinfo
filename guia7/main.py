from proteinaEnzimatica import ProteinaEnzimatica
from proteinaEstructural import ProteinaEstructural
from proteina import Proteina
import random

def main():

    proteina1 = Proteina("6E4R", "desc1", "")
    proteina2 = ProteinaEnzimatica("7Y9C", "desc2","" ,"subs1")
    proteina3 = ProteinaEstructural("8R5D", "desc3", "", False) ##True:fibrosa/False:globular
    
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
    
    proteina1.set_secuencia(sec)
    
    print(proteina1.get_nombre(), proteina1.get_descripcion())
   
    print(proteina2.get_nombre(), proteina2.get_descripcion()) 
    proteina2.mostrarSubtrato()

    print(proteina3.get_nombre(), proteina3.get_descripcion())
    proteina3.mostrarTipo()
    
    print("seuencia proteina: ",proteina1.get_secuencia())

if __name__ == "__main__":
    main()