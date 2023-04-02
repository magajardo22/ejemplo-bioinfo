from time import sleep
from perro import Perro

fufu = Perro()
sofy = Perro()
fufu.set_nombre("Fufu")
sofy.set_nombre("Sofy")

print ("Elige tu perro")
print ("\t1 - Fufu")
print ("\t2 - Sofy")


while True:

    opcionMenu = input(">> ")
    if opcionMenu=="1":
        sel=fufu.get_nombre()
        print ("")
        print("Has seleccionado a ", sel)

        break
    elif opcionMenu=="2":
        sel=sofy.get_nombre()
        print ("")
        print("Has seleccionado a ", sel)

        break
    else:
        print ("")
        input("No has pulsado ninguna opción correcta...\npulsa una tecla para continuar")


def main():

    print("")
    print ("Selecciona una opción para", sel)
    print ("\t1 - Pasear")
    print ("\t2 - Parar de pasear")
    print ("\t3 - Tomar agua")
    print ("\t9 - salir")
 
 
    while True:

        opcionMenu = input(">> ")

        if opcionMenu=="1":
            if sel == fufu.get_nombre():
                fufu.pasear()
                print(fufu.get_nombre(), end=" ")
                fufu.get_pasear()
                fufu.set_hora_toma_agua(1)
                print(fufu.get_hora_toma_agua())
            elif sel == sofy.get_nombre():
                sofy.pasear()
                print(sofy.get_nombre(), end=" ")
                sofy.get_pasear()
                sofy.set_hora_toma_agua(1)
                print(sofy.get_hora_toma_agua())
            input("pulsa una tecla para continuar")
            main()
        elif opcionMenu=="2":
            if sel == fufu.get_nombre():
                print(fufu.get_nombre(), end=" ")
                fufu.para()
            elif sel == sofy.get_nombre():
                print(sofy.get_nombre(), end=" ")
                sofy.para()
            input("pulsa una tecla para continuar")
            main()
        elif opcionMenu=="3":
            if sel == fufu.get_nombre():
                fufu.tomar_agua()
            elif sel == sofy.get_nombre():
                sofy.tomar_agua()

            input("pulsa una tecla para continuar")
            main()

        elif opcionMenu=="9":
            break
        else:
            input("pulsa una tecla para continuar")
            main()
        break

if __name__ == "__main__":
    main()

"""

def main():
    toby = Perro()
    toby.set_nombre("Toby")
    print(toby.get_nombre()) #Toby

    while True:
        for i in range(1, 3):
            toby.set_hora_toma_agua(1)
            sleep(1)
            print(toby.get_hora_toma_agua()) #1,2
        toby.tomar_agua() #esta tomando agua
        print(toby.get_hora_toma_agua()) #0
        print(toby.get_nombre(), " puede pasear") #toby puede pasear
        toby.pasear() #pasea
        if toby.get_pasear():
            print(toby.get_nombre(), " pasea") #toby pasea
        toby.set_hora_toma_agua(1)
        toby.tomar_agua() # no puede tomar agua
        print(toby.get_hora_toma_agua()) #1
        toby.para() #paro
        toby.set_hora_toma_agua(1)
        toby.tomar_agua() #esta tomando agua
        print(toby.get_hora_toma_agua()) #0

        break

if __name__ == "__main__":
    main()

"""

