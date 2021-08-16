def contador_palabras(frase):
	letras=len(frase)
	palabras= frase.split()
	palabras_totales = len(palabras)
	print("Muy bien, tu me has mostrado tu pensamiento en", letras, "letras y", palabras_totales, "Palabras!" )

pensamiento = input("En qué estás pensando?\n")
contador_palabras(pensamiento)
