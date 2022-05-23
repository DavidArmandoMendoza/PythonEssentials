def verifica(num1):
    if '.' in num1:
        print("Decimal")
    elif  'j' in num1:
        print("Complejo")
    else: 
        num1=int(num1)
    
    if type(num1)==int:
        print('Entero')

    
print('Programa que identifica el tipo de dato de un valor ingresado por el usuario')
print('Primera Interacción, ingrese un valor cualquiera:')
numero1=input()
print('Este tipo de dato en Python es:')
verifica(numero1)
print('Segunda Interacción, ingrese un valor cualquiera:')
numero1=input()
print('Este tipo de dato en Python es:')
verifica(numero1)
print('Tercera Interacción, ingrese un valor cualquiera:')
numero1=input()
print('Este tipo de dato en Python es:')
verifica(numero1)
print('Cuarta Interacción, ingrese un valor cualquiera:')
numero1=input()
print('Este tipo de dato en Python es:')
print('Quinta Interacción, ingrese un valor cualquiera:')
numero1=input()
print('Este tipo de dato en Python es:')
verifica(numero1)