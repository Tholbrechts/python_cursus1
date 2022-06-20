
# code
wallet = 5000
computer_price = 5000

# prix de l'ordi inferieur a 1000 euro

if   computer_price <= wallet or computer_price > 1000:
    print("l'achat est possible")
    wallet = wallet - computer_price
else:
    print("l'achat est immpossible vous n'avez que {} euro".format(wallet))

print(wallet)