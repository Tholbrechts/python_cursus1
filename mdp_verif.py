
#systeme de vierification de mdp
password = input('entrer votre mot de passe')
passwordleng= len(password)

# verifier si le mot de passe est inferieu a x caractere
if passwordleng <= 8:
    print('mot de passe trop court')
elif passwordleng > 8 and passwordleng <12:
    print('mot de passe moyen')

else:
    print("mot de passe parfait")


print(passwordleng)
