numero = 2

if numero > 1:
    for i in range(2, int(numero/2)+1):
         if (numero % i) == 0:
            print("El numero {0} no es primo".format(numero))
            break
    else:
        print("El numero {0} es primo".format(numero))

else:
    print("El numero {0} no es primo".format(numero))

