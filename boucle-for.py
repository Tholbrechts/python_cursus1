
# blacklist
blacklist = ["fati@hotmail.com"]
# for each pour chaque valeur d'une liste données
emails = ["toto@hotmail.com", "jp@hotmail.com", "fati@hotmail.com"]
for email in emails:
    if email in blacklist:
        print("email {} interdit! envoi impossible...".format(email))
        continue
    print("email envoyé à: ", email)
