# recolter age de la personne demander l'age
# si la personne est mineur -> 7 euro
# si la personne est majeur -> 12 euro
# souhaiter vous du pop corn
# si oui 5 euro
# afficher ce pti tottal a payer
mineur = 7
majeur = 12
popcorn = 5
age = input("quel est ton age ? ")
print(age)
if int(age) < 18:
    print("vous devez payer 7 euro")
else:
    print("vous devez payer 12 euro")
pop = input("souhaitez vous du popcorn? ")
if pop == "oui" and int(age) < 18:
    print("vous dever payer " + (mineur+popcorn) + " euro")
elif pop == "non" and int(age) < 18:
    print("vous dever payer " + (mineur) + " euro")
if pop == "non" and int(age) > 18:
    print("vous dever payer " + (majeur) + " euro")
elif pop == "oui" and int(age) > 18:
    print("vous dever payer " + (majeur + popcorn) + " euro")