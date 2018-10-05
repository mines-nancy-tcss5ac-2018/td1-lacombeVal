def solve(n):
    nombre = 2**n
    somme = 0
    while nombre>1 :
        somme += nombre % 10
        nombre = nombre // 10
    return somme

assert solve(15) == 26
print(solve(15))