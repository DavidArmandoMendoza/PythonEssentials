import misModulos,modulo_clave,modulo_1,modulo_2,modulos_lsts

menuprincipal=int(input(''' Elija una opción para la demostración:\n
1) Ejercicio 1 parte 1 Tipos de datos\n 
2) Ejercicio 1 parte 2 Programa que identifica el tipo de dato de un valor ingresado por el usuario\n                  
3) Ejercicio 2 parte 1 \nConsiderando la siguiente tupla\n Datos_2021 = [1, 2, 3, ,4, 5, 6, 7,100,91,110,900,21,33,32, 2, 4,8,10,13,13,16,15,1302]
Codifique un programa que permita separar los números pares e impares. Identifique también los posibles valores que considere atípicos a ese arreglo.\n
4) Ejercicio 2 parte 2 Validación de una contraseña\n
5) Ejercicio 3 Programa para encontrar valores máximos y mínimos dentro de un diccionrio\n
6) Salir\n'''))
while menuprincipal !=6:
    
    if menuprincipal==1:
            print('Ejercicio 1 parte 1')
            a=modulo_1.tipos()
            print(a)
            
    elif menuprincipal==2:
            print('Ejercicio 1 parte 2\n')
            print('Programa que identifica el tipo de dato de un valor ingresado por el usuario')
            print('Primera Interacción, ingrese un valor cualquiera:')
            numero1=input()
            print('Este tipo de dato en Python es:')
            modulo_2.verifica(numero1)
            print('Segunda Interacción, ingrese un valor cualquiera:')
            numero1=input()
            print('Este tipo de dato en Python es:')
            modulo_2.verifica(numero1)
            print('Tercera Interacción, ingrese un valor cualquiera:')
            numero1=input()
            print('Este tipo de dato en Python es:')
            modulo_2.verifica(numero1)
            print('Cuarta Interacción, ingrese un valor cualquiera:')
            numero1=input()
            print('Este tipo de dato en Python es:')
            modulo_2.verifica(numero1)
            print('Quinta Interacción, ingrese un valor cualquiera:')
            numero1=input()
            print('Este tipo de dato en Python es:')
            modulo_2.verifica(numero1)
        
    elif menuprincipal==3:
            print('Ejercicio 2 parte 1')
            lista1=[1,2,3,' ',4,5,6,7,100,91,110,900,21,33,32,2,4,8,10,13,13,16,15,1302]
            print('Datos_2021=', lista1)
            lista1.remove(' ')
            tupla=tuple(lista1)

            par=misModulos.num_par(tupla)
            impar=misModulos.num_impar(tupla)
            atip=misModulos.atp(tupla)

            print('Números pares: ', par)
            print('Números impares: ',impar)
            print('Números atipicos: ',sorted(atip))
    
    elif menuprincipal==4:
            print('Ejercicio 2 parte 2')  
            text = input("Ingrese una contraseña con los siguientes requisitos: \n 1. Debe contener al menos una letra minúscula entre las letras: a,b,c,d,e,f,g,h,i,j \n 2. Debe contener al menos una letra mayúscula entre las letras: K,L,M,N,O,P,Q,R,S,T \n 3. Debe contener al menos un número entre 0 y 9 \n 4. Debe contener un símbolo especial entre: $,%,*,@ \n 5. Tamaño mínimo de 5 caracteres y máximo de 15 \n")
            vc=modulo_clave.validarclave(text)
            print (vc)    
    
    elif menuprincipal==5:
            print('Ejercicio 3')
            lista_1={('Raul',34),('Paula', 19),('Jorge', 43),('Richard', 10),('Diana', 3),('Isabel', 76),('Gustavo', 12),('Diego', 37)}
            lista_2=[(4,-12,56,-34,98,102), (9,0,1,10,-3,14), (87,12,56,987,-61)]
            lista_3={('val1',-12.5),('val2', 12.5),('val3', 83),('val4', 2.1),('val5', 23),('val6', 100),('val7', 13.4),('val8', 92)}
            lista_4=[[4,6,-12,56,-9,5.7,33,100],[9,0,81,-2,-56,],[12,31,87,1,0,4,-11]]

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
            			ordenar = modulos_lsts.getValueList(lista_1)
            			lista_order = modulos_lsts.orderList(ordenar)
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
            			ordenar = modulos_lsts.getValueList(lista_3)
            			lista_order = modulos_lsts.orderList(ordenar)
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
            				lista_order = modulos_lsts.orderList(list(lista_unica))
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
            				lista_order = modulos_lsts.orderList(list(lista_unica))
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
            
    else:
        print('Seleccione una opción correcta\n')
    menuprincipal=int(input(''' Elija una opción para la demostración:\n
    1) Ejercicio 1 parte 1 Tipos de datos\n 
    2) Ejercicio 1 parte 2 Programa que identifica el tipo de dato de un valor ingresado por el usuario\n                  
    3) Ejercicio 2 parte 1 \nConsiderando la siguiente tupla\n Datos_2021 = [1, 2, 3, ,4, 5, 6, 7,100,91,110,900,21,33,32, 2, 4,8,10,13,13,16,15,1302]
    Codifique un programa que permita separar los números pares e impares. Identifique también los posibles valores que considere atípicos a ese arreglo.\n
    4) Ejercicio 2 parte 2 Validación de una contraseña\n
    5) Ejercicio 3 Programa para encontrar valores máximos y mínimos dentro de un diccionrio\n
    6) Salir\n'''))



