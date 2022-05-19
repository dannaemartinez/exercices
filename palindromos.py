def inverso(cadena):
    invertido= ""
    cont = len(cadena)
    i = -1
    while cont > 0:
        invertido+= cadena[i]
        i = i +(-1)
        cont -= 1
    return invertido

def palindromo(cadena):
    palabra = inverso(cadena)
    i = 0
    cont = 0
    for i in range(len(cadena)):
        if palabra[i]== cadena[i]:
            i += 1
            cont += 1
        else:
            print("{palabra} No es palindromo")
    if cont == len(cadena):
        print("La palabra: {palabra} Es palindromo")

