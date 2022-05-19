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
    if palabra == cadena:
        print("{0} Es palindromo".format(palabra))
    else:
        print("{0} No es palindromo".format(palabra))
    

palindromo("anai")

