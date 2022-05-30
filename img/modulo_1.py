
def tipos():

    print('Empezando a trabajar con Python') # Se utiliza la funcion print para mostrar en pantalla el respectivo texto
    print('Realizado por: "David Mendoza"\n')
    print('Consultando los tipos de valores:')
    print('El tipo de dato de 875 es')
    print(type(875)) #se procede a anidar funciones con la  funcion type se identifica el dato y con la funcion print se muestra en pantalla el tipo de dato
    print('El tipo de dato de 4.89 es')
    print(type(4.89))
    print('El tipo de dato del texto: Now is better than never. es:')
    print(type('Now is better than never.'))
    print('El tipo de dato de 1.32 es')
    print(type(1.32))
    print('¿El valor 5+8i corresponde a un valor entero?')
    print(isinstance(5+8j,int)) #se procede a anidar funciones con la función isisntance comparamos el valor 5+8i con un valor entero y el resultado se imprime en pantalla mediate la función print 
    print('¿El valor 8.2 corresponde a un valor entero?') #se procede a anidar funciones con la función isisntance comparamos el valor 8.2 con un valor entero y el resultado se imprime en pantalla mediate la función print 
    print(isinstance(8.2,int))
    print('¿El Texto: Readability counts.corresponde a un string?')#se procede a anidar funciones con la función isisntance comparamos el texto Readability counts con un string y el resultado se imprime en pantalla mediate la función print 
    print(isinstance('Readability counts',str))

    return 


