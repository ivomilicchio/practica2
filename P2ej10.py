archivo_nombres= open ('nombres_1.txt' , 'r', encoding="utf8")
archivo_eval1= open('eval1.txt', 'r' ,encoding="utf8")
archivo_eval2= open('eval2.txt', 'r', encoding="utf8")
lista_eval= []

for elem in archivo_nombres.readlines():
		lista_eval.append([(elem).strip("\n").strip(",").strip( " ' ")])

total= 0

for i in range(0, len(lista_eval)):
		nota1= archivo_eval1.readline()
		nota1= int (nota1.replace ("," , ""))
		nota2= archivo_eval2.readline()
		nota2= int(nota2.replace("," , ""))
		total= total + nota1 + nota2
		lista_eval[i].append(nota1 + nota2)
		
prom= total/len(lista_eval)

print(list(filter(lambda x: False if x[1]<prom else True, lista_eval)))
	
""""
strip() elimina los caracteres que pasas como argumento

replace() reeemplaza una "palabra" o subcadena adentro del string te permite introducir o sacar caracteres

help() funcion que permite ver la documentacion de un objeto en la terminal interactiva

en lugar de abrir el archivo y cerrarlo dentro de un try except o en la asignacion de una variable, pueden abrir el archivo con with y eso hace que al terminar de leer el archivo se cierre automaticamente

c = Counter(words_to_count)
print c.most_common()
"""
		
