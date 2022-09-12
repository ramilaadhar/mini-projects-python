import random
print("1:l'ancer le dé 0:quiter le programme")
while True:
   #on demande a l'utilisateur de saisi un nombre
   x=int(input("cliquer sur un bouton "))
   if x==0:
      print('byeA la prochaine')
      break
   elif x==1:
      print(random.randint(1,6))
   else:
      print("je n'est pas comprit")


#roll the dice1
