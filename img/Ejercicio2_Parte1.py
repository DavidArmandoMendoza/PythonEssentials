lista1=[1,2,3,' ',4,5,6,7,100,91,110,900,21,33,32,2,4,8,10,13,13,16,15,1302]
print('Datos_2021=', lista1)
lista1.remove(' ')
tupla=tuple(lista1)

def num_par(numeros):
    pares=[]
    
    for n in numeros:
        if n%2==0:
            pares.append(n)
    return pares

def num_impar(numeros):
    impares=[]
    
    for n in numeros:
        if n%2!=0:
            impares.append(n)
    return impares

def atp(numeros):
    
    atipico=[]
    
    for n in numeros:
        if n>77:
            atipico.append(n)
    return atipico 

par= num_par(tupla)
impar=num_impar(tupla)
atip=atp(tupla)
print('Números pares: ', par)
print('Números impares: ',impar)
print('Números atipicos: ',sorted(atip))