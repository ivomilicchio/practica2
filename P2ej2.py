import collections
import string
readme= open ("README.md.txt")
lista_readme= readme.read().lower().split()
print (collections.Counter(lista_readme).most_common(1))
