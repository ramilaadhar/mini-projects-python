import random
while True:
   x=int(input("cliquer sur un bouton "))
   if x==0:
      print('byeA la prochaine')
      break
   elif x==1:
      print(random.randint(1,6))

#roll the dice