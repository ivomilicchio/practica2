import string
texto= "En Python las comillas dobles y las comillas simples son completamente equivalentes"
words= texto.lower().split()
texto.split()
letra= input ("Ingrese una letra: ")
letra.lower()
if letra.isalpha():
		for actual in words:
				if actual.startswith(letra):
						print (actual)
else:
		print ("Error: el caracter ingresado no es una letra")
		
