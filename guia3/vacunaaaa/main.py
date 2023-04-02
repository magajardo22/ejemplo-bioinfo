from vacuna import Vacuna


def main():
    # Crear objetos de tipo Vacuna
    vacuna1 = Vacuna("Pfizer-BioNTech", "Pfizer")
    vacuna2 = Vacuna("Moderna", "Moderna")
    vacuna3 = Vacuna("AstraZeneca", "AstraZeneca")

    # Agregar efectos secundarios a cada vacuna
    vacuna1.agregar_efecto_secundario("Dolor en el brazo donde se recibió la vacuna")
    vacuna1.agregar_efecto_secundario("Fiebre")
    vacuna1.agregar_efecto_secundario("Cansancio")
    vacuna2.agregar_efecto_secundario("Dolor de cabeza")
    vacuna2.agregar_efecto_secundario("Náuseas")
    vacuna2.agregar_efecto_secundario("Escalofríos")
    vacuna3.agregar_efecto_secundario("Dolor en el lugar de la inyección")
    vacuna3.agregar_efecto_secundario("Fatiga")
    vacuna3.agregar_efecto_secundario("Dolor de cabeza")

    # Mostrar los efectos secundarios de cada vacuna
    print("Efectos secundarios de la vacuna", vacuna1.nombre, "del laboratorio", vacuna1.laboratorio)
    vacuna1.mostrar_efectos_secundarios()

    print("Efectos secundarios de la vacuna", vacuna2.nombre, "del laboratorio", vacuna2.laboratorio)
    vacuna2.mostrar_efectos_secundarios()

    print("Efectos secundarios de la vacuna", vacuna3.nombre, "del laboratorio", vacuna3.laboratorio)
    vacuna3.mostrar_efectos_secundarios()

if __name__ == "__main__":
    main()