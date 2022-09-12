import random
#Ask the user to give the password length
longpass=int(input("donner la longueur du mot de passe"))
s="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!%&\()*+,-./:;<=>?@[]^_{|}~"
#Group the randomly selected characteristics into a single word
password="".join(random.sample(s,longpass))
print(password)