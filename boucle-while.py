
# un youtubeur "toto", 2500 abonés
sucribercount = 2500
# il gagne 10% d'audience suipplementaire par mois
months = 0
# on souhaite estimer, combien aura t'il d'abonnés, apres 2 ans sois 24 mois
while months <= 24:
    #augmenter l'audience
    sucribercount *= 1.10
    #afficher le nombre d'abonnés
    print("Vous avez {} abonnés !".format(sucribercount))
    months += 1