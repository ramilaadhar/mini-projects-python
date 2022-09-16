text =str(input("donner une chaine de caractere: "))

def gen_accro(chaine):
    mots = chaine.split()
    accro = ''
    for i in mots:
     accro = accro + str(i[0]).upper()
    return accro

resultat=gen_accro(text)

print(f"voici l'accronyme {resultat}")