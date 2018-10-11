def renverse(l):
    n = len(l)
    renverser = [0]*n
    for k in range(n):
        renverser[k] = l[n-k]
    return renverser

def from_int_to_list(int):
    indice = 0
    while int//(10**indice) != 0 :
        indice += 1
    indice += -1
    list = [0]*indice
    for k in range(indice):
        list[indice-k-1] = int % 10 # on commence par la fin
        int = int//10
    return l

def from_list_to_int(list):
    n = len(list)
    somme = 0
    for i in range(n):
        somme += liste[i]*10**i
    return somme
        

def est_palyndrome(nombre):
    liste = from_int_to_list(nombre)
    return list == renverse(liste)

def iteration_de_somme(nombre):
    return nombre + from_list_to_int(renverse(from_int_to_list(nombre)))

def solve(nombre_max):
    compteur = 0 
    for k in range(1,nombre_max+1):
        nombre_tester = k
        nbr-test-k = 0
        while not est_palyndrome(k) and nbr-test-k < 50:
            nombre_tester = iteration_de_somme(nombre_tester)
            nbr-test-k +=1
        if nbr-test-k == 50:
            compteur += 1
    return compteur

print(solve(10000))
        
    
