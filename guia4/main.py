from secuenciaADN import SecuenciaADN


def main():
    vec1 = SecuenciaADN()
    vec1.set_ADN("ACGTCAGTAATACAACGTACTAGCTACATCATGC")


    print("La cadena es: ",vec1.get_ADN())
    print("La longitud de la cadena es: ", end="")
    vec1.set_longitud(vec1.get_ADN())

   vec1.set_complemento_inverso(vec1.get_ADN())



if __name__ == "__main__":
    main()