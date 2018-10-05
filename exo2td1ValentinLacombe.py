def valeur(lettre):
    score_caractere = ['"','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    indice = 0
    while indice < 27 and lettre != score_caractere[indice]:
        indice += 1
    if indice < 27:
        return indice
    else:
        return False

def solve():
    noms = []
    fichier = open("p022_names.txt", "r")
    for ligne in fichier :
        noms += ligne.split(",")
    trier = sorted(noms)
    n = len(trier)
    score_total = 0
    for k in range(n):
        prenom = trier[k]
        nprenom = len(prenom)
        score_du_prenom = 0
        for i in range(nprenom):
            score_du_prenom += valeur(prenom[i])
        score_total += score_du_prenom * (k+1)
    return score_total

print(solve())