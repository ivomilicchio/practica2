import string
from collections import Counter
frase= input ('Ingrese una frase: ').lower()
punct = string.punctuation
for i in punct:
		frase= frase.replace(i, " ")
frase= frase.split()
string= input ('Ingrese una palabra: ').lower()
print ('Palabra: ' + string)
print ('Resultado: ' + str(frase.count(string)))
