from planeta import Planeta
from planeta import Sistema

def main():

    mercurio = Planeta(3.285e23, 5427, 4879, 57.91e6, "1", "Mercurio")
    venus = Planeta(4.867e24, 5243, 12104, 108.2e6, "2", "Venus")
    tierra = Planeta(5.97e24, 5514, 12756, 149.6e6, "3", "Tierra")
    marte = Planeta(6.39e23, 3933, 6792, 227.9e6, "4", "Marte")
    jupiter = Planeta(1.898e27, 1326, 142984, 778.3e6, "5", "Júpiter")
    saturno = Planeta(5.68e26, 687, 120536, 1427e6, "6", "Saturno")
    urano = Planeta(8.68e25, 1271, 51118, 2871e6, "7", "Urano")
    neptuno = Planeta(1.024e26, 1638, 49528, 4497e6, "8", "Neptuno")

    sistema_solar = Sistema([mercurio, venus, tierra, marte, jupiter, saturno, urano, neptuno])

    while True:
        sistema_solar.set_menu()
        print(" ")
        seleccion = input("Ingrese el número ('9' para salir)>> ")
        if seleccion.lower() == '9':
            break
        else:
            sistema_solar.set_planeta(seleccion)
            print(" ")
            input("pulsa una tecla para continuar")
            main()
        break

        




    """
    print("Sistema Solar")
    print("\t1 - Mercurio")
    print("\t2 - Venus")
    print("\t3 - Tierra")
    print("\t4 - Marte")
    print("\t5 - Jupiter")
    print("\t6 - Saturno")
    print("\t7 - Urano")
    print("\t8 - Neptuno")
    print("\t9 - Salir")


    while True:

        opcionMenu = input(">> ")

        if opcionMenu=="1":
            tierra = Planeta("Tierra", 1, 1111111,11111, 111111, 1111111)
            sistema = Sistema()
            sistema.set_planeta(tierra)
            sistema.get_planeta()
            input("pulsa una tecla para continuar")
            main()

        elif opcionMenu=="2":
            Venus = Planeta("Venus", 2, 22222, 2222, 2222, 22222)
            sistema = Sistema()
            sistema.set_planeta(Venus)
            sistema.get_planeta()
            input("pulsa una tecla para continuar")
            main()
        elif opcionMenu=="9":
            break
        else:
            input("pulsa una tecla para continuar")
            main()
        break
            
    """


    

    """
    mercurio = Planeta()
    mercurio.set_nombre("Mercurio")
    mercurio.set_id(1)
    mercurio.set_masa("3.285 x 10^23 kg")
    mercurio.set_densidad(5.43)
    mercurio.set_diametro(4879.4)
    mercurio.set_distancia_sol(58)


    print(  mercurio.get_nombre(), 
            mercurio.get_id(),
            mercurio.get_masa(),
            mercurio.get_densidad(),
            mercurio.get_diametro(),
            mercurio.get_distancia_sol())
    """

if __name__ == "__main__":
    main()