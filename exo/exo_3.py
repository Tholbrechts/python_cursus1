# generateur de phrase
# demander en console une chaine de la forme "mot1/mot2/mot3/mot4"
# transformer cette chaine en une liste
# la melanger
# si le nombre d'element dans cette liste est inferieur a 10
# afficher les deux premier mots
# si le nombre est superieur ou egal a 10
# afficher les 3 derniers

from random import shuffle
text = input("entrer une chaine de la forme (mot1/mot2/mot3/mot4)").split("/")
shuffle(text)
texteleng = len(text)

if texteleng < 10:
    print(text[0], text[1])
else:
    print(text[-1], text[-2])
