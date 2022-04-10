archivo_nombres_1= open("C:\\Users\\ivomi\\OneDrive\\Escritorio\\Seminario Python\\nombres_1.txt", 'r',  encoding= "utf8") 
archivo_nombres_2= open("C:\\Users\\ivomi\\OneDrive\\Escritorio\\Seminario Python\\nombres_2.txt", 'r', encoding= "utf8")
archivo_notas_1= open("C:\\Users\\ivomi\\OneDrive\\Escritorio\\Seminario Python\\eval1.txt", 'r', encoding= "utf8")
archivo_notas_2= open("C:\\Users\\ivomi\\OneDrive\\Escritorio\\Seminario Python\\eval2.txt", 'r', encoding= "utf8")
lista_nombres_1= []
lista_nombres_2= []
lista_comun= []
lista_eval_1= []
lista_eval_2= []

for elem in archivo_nombres_1:
    lista_nombres_1.append(elem.strip().replace("'," , "").replace("'", ""))

for elem in archivo_nombres_2:
    lista_nombres_2.append(elem.strip().replace("'," , "").replace("'", ""))

for elem in lista_nombres_1:
    if elem in lista_nombres_2:
        lista_comun.append(elem)

print("Nombres que se encuentran en ambas listas: " + str(lista_comun))

print (" ")

for elem in archivo_notas_1:
    lista_eval_1.append(elem.strip().replace(",", ""))
for elem in archivo_notas_2:
    lista_eval_2.append(elem.strip().replace(",", ""))

print ( "{:>12}".format("Nombre")  +  "{:>12}".format("Eval1") +  "{:>10}".format("Eval2") +  "{:>10}".format("Total"))

for i in range(0, len(lista_nombres_1)):
    print ("{:>5}".format(str(i)) + " " + "{:<15}".format(lista_nombres_1[i]) + "{:<10}".format(lista_eval_1[i]) + "{:<10}".format(lista_eval_2[i]) +  "{:<10}".format(str((int(lista_eval_1[i])+ int(lista_eval_2[i])))))

 