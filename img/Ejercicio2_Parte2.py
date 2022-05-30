text = input("Ingrese una contraseña con los siguientes requisitos: \n 1. Debe contener al menos una letra minúscula entre las letras: a,b,c,d,e,f,g,h,i,j \n 2. Debe contener al menos una letra mayúscula entre las letras: K,L,M,N,O,P,Q,R,S,T \n 3. Debe contener al menos un número entre 0 y 9 \n 4. Debe contener un símbolo especial entre: $,%,*,@ \n 5. Tamaño mínimo de 5 caracteres y máximo de 15 \n")

def validarclave(text) :
	numero_validar = 0
	mayuscula_validar = 0
	minuscula_validar = 0
	especial_validar = 0
	tamano=0
	tamano_validado=0
	for each_char in text:
		tamano +=1
		if ord(each_char) >= 48 and ord(each_char) <=57 :
			numero_validar = 1
			tamano_validado+=1
		if ord(each_char) >= 97 and ord(each_char) <=106 :
			minuscula_validar = 1		
			tamano_validado+=1
		if ord(each_char) >= 75 and ord(each_char) <=84 :
			mayuscula_validar = 1				
			tamano_validado+=1
		if ord(each_char) == 42 or ord(each_char) ==36 or ord(each_char) ==37 or ord(each_char) ==64 :
			especial_validar = 1
			tamano_validado+=1
		
			
	if numero_validar == 1 and minuscula_validar == 1 and mayuscula_validar == 1 and especial_validar == 1 and tamano >= 5 and tamano <= 15 and tamano == tamano_validado:
		return "**************** Contraseña validada correctamente ****************"
	else: 
		if numero_validar == 0:
			return "Debe contener al menos un número entre 0 y 9"
		if minuscula_validar == 0:
			return "Debe contener al menos una letra minúscula entre las letras: a,b,c,d,e,f,g,h,i,j"		
		if mayuscula_validar == 0:
			return "Debe contener al menos una letra mayúscula entre las letras: K,L,M,N,O,P,Q,R,S,T"		
		if especial_validar == 0:
			return "Debe contener un símbolo especial entre: $,%,*,@"		
		if tamano < 5 or tamano > 15:
			return "Tamaño mínimo de 5 caracteres y máximo de 15"		
		if tamano != tamano_validado :
			return "Contraseña no valida no tiene caracteres permitidos"					

print (validarclave(text))