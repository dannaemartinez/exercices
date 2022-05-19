def fibo(numero):
    array =[0,1]
  
    for i in range(2, numero, 1):
        array.append(array[i - 1] + array[i - 2])
    
    resultado = array[numero -1]
    print(array)
    print("El numero {0} en la serie de fibonacci es {1}" .format(numero, resultado))

fibo(20)
