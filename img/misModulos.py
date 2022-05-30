

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
