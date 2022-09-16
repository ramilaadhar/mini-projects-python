import random
nombre_choisi=random.randint(1,6)
resultat=0
for i in range(3):
    nombre_proposer= int(input("saisir un nombre: "))
    if nombre_choisi == nombre_proposer:
        resultat=1
        break
        print("bravo c'est le bon numero")
    elif nombre_proposer > nombre_choisi :
            print("le nombre proposer est superieur au nombre choisi")
    elif nombre_proposer < nombre_choisi :
                print("le nombre proposer est inferieur au nombre choisi")
if resultat ==1:
        print("bravo bien joué")
        print(f"le bon numero est {nombre_choisi}")
else:
            print("vous perdez, le bon numéro était {nombre_choisi}")
