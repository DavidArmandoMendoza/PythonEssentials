def verifica(num1):
    if '.' in num1:
        print("Decimal")
    elif  'j' in num1:
        print("Complejo")
    else: 
        num1=int(num1)
    
    if type(num1)==int:
        print('Entero')
    return


