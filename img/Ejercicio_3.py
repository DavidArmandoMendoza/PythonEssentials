lista_1={('Raul',34),('Paula', 19),('Jorge', 43),('Richard', 10),('Diana', 3),('Isabel', 76),('Gustavo', 12),('Diego', 37)}
lista_2=[(4,-12,56,-34,98,102), (9,0,1,10,-3,14), (87,12,56,987,-61)]
lista_3={('val1',-12.5),('val2', 12.5),('val3', 83),('val4', 2.1),('val5', 23),('val6', 100),('val7', 13.4),('val8', 92)}
lista_4=[[4,6,-12,56,-9,5.7,33,100],[9,0,81,-2,-56,],[12,31,87,1,0,4,-11]]

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

def bucle_program():
	salir = 1
	while salir:
		option = input("Elija una opción:\n 1) Demostración del cálculo de máximos y mínimos en diccionarios.\n 2) Salir.\n")
		if option == '1' or option == '2':		
			salir=0
		else:
			print("Error: Seleccione una opción válida \n\n")
		
	if option == '2':
		salir = 0
		option = 20
		return 20
	else: 
		salir = 1
		
	while salir:
		option = input("Elija un diccionario para la demostración:\n 1) {Raul:34,Paula:19,Jorge:43,Richard:10,Diana:3,Isabel:76,Gustavo:12,Diego:37} \n 2) {tplA:(4,-12,56,-34,98,102),tplB:(9,0,1,10,-3,14),tlpC:(87,12,56,987,-61)} \n 3) {val1:-12.5,val2:12.5,val3:83,val4:2.1,val5:23,val6:100,val7:13.4,val8:92} \n 4) {lst1:[4,6,-12,56,-9,5.7,33,100],lst2:[9,0,81,-2,-56,],lst3:[12,31,87,1,0,4,-11]} \n")	
		if option == '1' or option == '2' or option == '3' or option == '4':		
			salir=0		
		else:
			print("Error: Seleccione una opción válida \n\n")
		
	if option == '1' or option == '2' or option == '3' or option == '4':
		maximos=0
		minimos=0
		while 1:
			while 1:
				try:
					maximos = int(input("Digite el número de máximos que desea mostrar:"))
					break
				except:
					print("Ingrese un número válido")
					
			while 1:
				try:
					minimos = int(input("Digite el número de mínimos que desea mostrar:"))
					break
				except:
					print("Ingrese un número válido")
				
			tamano = maximos + minimos
			print(tamano)
			if option == '1':
				print(len(lista_1))
				if tamano <= len(lista_1):
					break
				else:
					print("Error: Máximos y mínimos supera longitud listas \n\n")
			
			if option == '2':			
				list_ok_tamano=0
				
				for sub in lista_2:
					if tamano <= len(sub):
						list_ok_tamano+=1				
						
				print(list_ok_tamano)
				
				if list_ok_tamano == len(lista_2):
					break
				else:
					print("Error: Máximos y mínimos supera longitud tuplas internas en las listas \n\n")
			
			if option == '3':
				print(len(lista_3))
				if tamano <= len(lista_3):
					break
				else:
					print("Error: Máximos y mínimos supera longitud listas \n\n")
					
					
			if option == '4':			
				list_ok_tamano=0
				
				for sub in lista_4:
					if tamano <= len(sub):
						list_ok_tamano+=1				
														
				if list_ok_tamano == len(lista_4):		
					break
				else:
					print("Error: Máximos y mínimos supera longitud tuplas internas en las listas \n\n")				
																		
		#Validar el resultado
		if option == '1':
			ordenar = getValueList(lista_1)
			lista_order = orderList(ordenar)
			max_list=[]
			min_list=[]
			inversa_maximos = len(lista_order) - maximos
			
			for x in range(minimos):
				min_list.append(lista_order[x])
				
			for x in range(len(lista_order)):
				if x >= inversa_maximos:
					max_list.append(lista_order[x])
					
			print("Valores Mínimos: \n")
			print('Formato LISTA:',min_list)
			print('Formato TUPLA:',tuple(min_list))
			print("Valores Máximos: \n")
			print('Formato LISTA:',max_list)
			print('Formato TUPLA:',tuple(max_list))
			
		if option == '3':
			ordenar = getValueList(lista_3)
			lista_order = orderList(ordenar)
			max_list=[]
			min_list=[]
			inversa_maximos = len(lista_order) - maximos
			
			for x in range(minimos):
				min_list.append(lista_order[x])
				
			print(inversa_maximos)
				
			for x in range(len(lista_order)):
				if x >= inversa_maximos:
					max_list.append(lista_order[x])
					
			print("Valores Mínimos: \n")
			print('Formato LISTA:',min_list)
			print('Formato TUPLA:',tuple(min_list))
			print("\n\n")
			print("Valores Máximos: \n")
			print('Formato LISTA:',max_list)
			print('Formato TUPLA:',tuple(max_list))
			print("\n\n")
				
				
		if option == '2':	
			list_maximos=[]
			list_minimos=[]
			for lista_unica in lista_2:			
				lista_order = orderList(list(lista_unica))
				max_list=[]
				min_list=[]
				inversa_maximos = len(lista_order) - maximos
				
				for x in range(minimos):
					min_list.append(lista_order[x])				
					
				for x in range(len(lista_order)):
					if x >= inversa_maximos:
						max_list.append(lista_order[x])
				
				list_maximos.append(tuple(max_list))
				list_minimos.append(tuple(min_list))			
				
			print("Valores Mínimos: \n")
			print ('Formato LISTA:',list_minimos)
			print ('Formato TUPLA:',tuple(list_minimos))
			print("\n\n")
			
			print("Valores Máximos: \n")
			print('Formato LISTA:',list_maximos)
			print('Formato TUPLA:',tuple(list_maximos))
			print("\n\n")
			
		if option == '4':	
			list_maximos=[]
			list_minimos=[]
			for lista_unica in lista_4:			
				lista_order = orderList(list(lista_unica))
				max_list=[]
				min_list=[]
				inversa_maximos = len(lista_order) - maximos
				
				for x in range(minimos):
					min_list.append(lista_order[x])					
					
				for x in range(len(lista_order)):
					if x >= inversa_maximos:
						max_list.append(lista_order[x])
				
				list_maximos.append(tuple(max_list))
				list_minimos.append(tuple(min_list))			
				
			print("Valores Mínimos: \n")
			print ('Formato LISTA:',list_minimos)
			print ('Formato TUPLA:',tuple(list_minimos))
			print("\n\n")
			
			print("Valores Máximos: \n")
			print('Formato LISTA:',list_maximos)
			print('Formato TUPLA:',tuple(list_maximos))
			print("\n\n")
		
		return 1
	

while 1:
	salir = bucle_program()
	if salir == 20:
		break
	else:
		print("\n\n\n")
	
print("================== Programa Finalizado =======================")
