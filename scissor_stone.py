import random
choix=['C','P','PI']
cpu=random.choice(choix)
joueur=str(input("C:ciseau , P:papier , PI:pierre?")).capitalize()
if joueur==cpu:
    print("égalite!")
elif joueur=='PI':
        if cpu=='P':
            print("vous perdez, le papier couvre la pierre")
        elif cpu=='C':
            print("vous gagner, la pierre casse les ciseaux")

elif joueur=='P':
        if cpu=='C':
            print("vous perdez, les ciseaux coupe le papier")
        elif cpu=='PI':
            print("vous gagner, le papier couvre la pierre")

elif joueur=='C':
        if cpu=='P':
            print("vous gangez, les ciseaux coupe le papier")
        elif cpu=='PI':
            print("vous perder, la pierre casse les ciseaux")
