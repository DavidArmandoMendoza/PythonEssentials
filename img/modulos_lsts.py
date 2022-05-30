#Obtener valores de una lista
def getValueList(lista) :
	lista_normal=[]
	for sub in lista:
		lista_normal.append(sub[1])
	return lista_normal

#Ordenar una lista numerica
def orderList(lista) :
	lista_order=[]
	min = 20000
	index_remove=0
	while len(lista) > 0 :
		for x in range(len(lista)):
			if min > lista[x]:
				min=lista[x]
				index_remove=x
						
		lista_order.append(min)
		lista.pop(index_remove)
		min=200000
		index_remove=0	
	return lista_order
