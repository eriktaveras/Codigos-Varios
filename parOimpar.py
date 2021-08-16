def paroimpar(num):
    if num % 2 == 0:
        print('ese numero es un numero par\n')
    else:
        print('ese numero es un numero impar\n')

    return num
while 1 < 10:
	num = int(input("Ingrese el numero para analizar:\n"))
	paroimpar(num)
