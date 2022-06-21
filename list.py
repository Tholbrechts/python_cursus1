
text = input("entrer une chaine de la forme (email pseudo motdepasse)").split(" ")

print(text)

print("salut {}, ton email est {}  et ton mdp est {}".format(text[1], text[0], text[2]))