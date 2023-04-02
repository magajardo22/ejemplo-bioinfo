from vacunas import Vacunas

def main():
    vacuna1 = Vacunas()
    vacuna1.set_nombre("CoronaVac")
    vacuna2 = Vacunas()
    vacuna2.set_nombre("NVX")
    vacuna3 = Vacunas()
    vacuna3.set_nombre("Pfizer")
    lab1 = Vacunas()
    lab1.set_lab("Sinovac")
    lab2 = Vacunas()
    lab2.set_lab("Novavax")
    lab3 = Vacunas()
    lab3.set_lab("Comirnaty")



    print("")
    print ("\t1 - Listado de Vacunas/Laboratorios")
    print ("\t2 - Lista Efectos Secundarios de Vacunas")
    print ("\t3 - Agregar Efectos Secundarios")
    print ("\t9 - salir")

    while True:


        opcionMenu = input(">> ")
        if opcionMenu=="1":
            print("1.-",vacuna1.get_nombre(), lab1.get_lab(), sep=" ")
            print("2.-",vacuna2.get_nombre(), lab2.get_lab(), sep=" ")
            print("3.-",vacuna3.get_nombre(), lab3.get_lab(), sep=" ")
            input("pulsa enter continuar")
            main()
        


        elif opcionMenu=="9":
            break
        else:
            input("No has pulsado ninguna opción correcta...\npulsa enter continuar")
            main()
        break

if __name__ == "__main__":
    main()