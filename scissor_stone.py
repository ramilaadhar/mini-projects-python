import random
choix=['C','P','Pi']
score_cpu=0
score_joueur=0

while True:
   cpu = random.choice(choix)
   joueur = str(input("C:ciseau , P:papier , PI:pierre? Pour quiter taper Fin ")).capitalize()
   if joueur==cpu:
    print("égalite!")
   elif joueur=='Pi':
        if cpu=='P':
            print("vous perdez, le papier couvre la pierre")
            score_cpu+=1
   elif cpu=='C':
            print("vous gagner, la pierre casse les ciseaux")
            score_joueur+=1

   elif joueur=='P':
        if cpu=='C':
            print("vous perdez, les ciseaux coupe le papier")
            score_cpu+=1
        elif cpu=='Pi':
            print("vous gagner, le papier couvre la pierre")
            score_joueur+=1

   elif joueur=='C':
        if cpu=='P':
            print("vous gangez, les ciseaux coupe le papier")
            score_joueur+=1
        elif cpu=='Pi':
            print("vous perder, la pierre casse les ciseaux")
            score_cpu+=1
   elif joueur=='Fin':
    print("resultat:")
    print(f"cpu= {score_cpu}")
    print(f"joueur= {score_joueur}")
    break
   else:
    print("je n'est pas comprit: verifier l'orthographe")