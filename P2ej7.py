import string
frase= input('Ingrese una frase o palabra: ').lower()
pun= string.punctuation + string.digits
for i in pun:
		frase= frase.replace(i, "")
frase= frase.replace(" ", "")
cont= 0
heterograma= True
while cont < len(frase)-1 and heterograma== True:
		if frase.count(frase[cont]) > 1:
				heterograma= False
		else:
				cont= cont +1
if heterograma == True:
		print ("Es un heterograma");
else:
	print ("No es un heterograma");
