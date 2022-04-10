buscaminas= [
		'-*-*-',
		'--*--',
		'----*',
		'*----',
]
tabla= buscaminas.copy()
res= []

for i in range(0, len(buscaminas)):
		tabla[i]= (tabla[i].replace ( '-' , '0'))
		res.append(list(tabla[i]))

def add_up(res, pos_list, pos_str):
		"Incrementa en uno la posicion de arriba si no es una bomba"
		if res[pos_list-1][pos_str] != '*':
				res[pos_list-1][pos_str]= chr(ord(res[pos_list-1][pos_str])+1)
		return res

def add_down(res, pos_list, pos_str):
		"Incrementa en uno la posicion de abajo si no es una bomba"
		if res[pos_list+1][pos_str]!= '*':
				res[pos_list+1][pos_str]= chr(ord(res[pos_list+1][pos_str])+1)
		return res
		
def add_left(res, pos_list, pos_str):
		"Incrementa en uno la posicion de la izquierda si no es una bomba"
		if res[pos_list][pos_str-1]!= '*':
				res[pos_list][pos_str-1]= chr(ord(res[pos_list][pos_str-1])+1)
		return res
		
def add_right(res, pos_list, pos_str):
		"Incrementa en uno la posicion de la derecha si no es una bomba"
		if res[pos_list][pos_str+1]!= '*':
				res[pos_list][pos_str+1]= chr(ord(res[pos_list][pos_str+1])+1)
		return res

def add_diag_up_left(res, pos_list, pos_str):
		"Incrementa en uno la posicion de arriba a la izquierda en direccion diagonal si no es una bomba"
		if res[pos_list-1][pos_str-1]!= '*':
				res[pos_list-1][pos_str-1]= 	chr(ord(res[pos_list-1][pos_str-1])+1)
		return res
		
def add_diag_up_right(res, pos_list, pos_str):
		"Incrementa en uno la posicion de arriba a la derecha en direccion diagonal si no es una bomba"
		if res[pos_list-1][pos_str+1]!= '*':
				res[pos_list-1][pos_str+1]= chr(ord(res[pos_list-1][pos_str+1])+1)
		return res
		
def add_diag_down_left(res, pos_list, pos_str):
		"Incrementa en uno la posicion de abajo a la izquierda en direccion diagonal si no es una bomba"
		if res[pos_list+1][pos_str-1]!= '*':
				res[pos_list+1][pos_str-1]= chr(ord(res[pos_list+1][pos_str-1])+1)
		return res
		
def add_diag_down_right(res, pos_list, pos_str):
		"Incrementa en uno la posicion de abajo a la derecha en direccion diagonal si no es una bomba"
		if res[pos_list+1][pos_str+1]!= '*':
				res[pos_list+1][pos_str+1]= 	chr(ord(res[pos_list+1][pos_str+1])+1)
		return res
					
for pos_list in range (0, len(res)): 
		for pos_str in range (0, len(res[i])):
				if res[pos_list][pos_str]== "*":
						if pos_list== 0:
								if pos_str== 0:
										add_right(res, pos_list, pos_str)
										add_diag_down_right(res, pos_list, pos_str)
										add_down(res, pos_list, pos_str)
								elif pos_str== len(buscaminas[0])-1:
										add_left(res, pos_list, pos_str)
										add_diag_down_left(res, pos_list, pos_str)
										add_down(res, pos_list, pos_str)
								else:
										add_left(res, pos_list, pos_str)
										add_diag_down_left(res, pos_list, pos_str)
										add_down(res, pos_list, pos_str)
										add_diag_down_right(res, pos_list, pos_str)
										add_right(res, pos_list, pos_str);
						elif pos_list== len(buscaminas)-1:
								if pos_str== 0:
										add_up(res, pos_list, pos_str)
										add_diag_up_right(res, pos_list, pos_str)
										add_right(res, pos_list, pos_str)
								elif pos_str== len(buscaminas[0])-1:
										add_up(res, pos_list, pos_str)
										add_diag_up_left(res, pos_list, pos_str)
										add_left(res, pos_list, pos_str)
								else:
										add_left(res, pos_list, pos_str)
										add_diag_up_left(res, pos_list, pos_str)
										add_up(res, pos_list, pos_str)
										add_diag_up_right(res, pos_list, pos_str)
										add_right(res, pos_list, pos_str)
						else :
								if pos_str== 0:
										add_up(res, pos_list, pos_str)
										add_diag_up_right(res, pos_list, pos_str)
										add_right(res, pos_list, pos_str)
										add_diag_down_right(res, pos_list, pos_str)
										add_down(res, pos_list, pos_str)
								elif pos_str==  len(buscaminas[0])-1:
										add_up(res, pos_list, pos_str)
										add_diag_up_left(res, pos_list, pos_str)
										add_left(res, pos_list, pos_str)
										add_diag_down_left(res, pos_list, pos_str)
										add_down(res, pos_list, pos_str)
								else:
										add_up(res, pos_list, pos_str)
										add_diag_up_right(res, pos_list, pos_str)
										add_right(res, pos_list, pos_str)
										add_diag_down_right(res, pos_list, pos_str)
										add_down(res, pos_list, pos_str)
										add_diag_down_left(res, pos_list, pos_str)
										add_left(res, pos_list, pos_str)
										add_diag_up_left(res, pos_list, pos_str)

for i in range(0, len(res)):
		print ((res[i]))
				

