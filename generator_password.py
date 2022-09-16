import random
#Ask the user to give the password length
longpass=int(input("donner la longueur du mot de passe"))
s="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!%&\()*+,-./:;<=>?@[]^_{|}~"
#Group randomly selected characters into one word
password="".join(random.sample(s,longpass))
print(password)