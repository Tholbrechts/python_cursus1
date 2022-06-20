def main():
    # valeur du wallet
    wallet = int(input('valeur du wallet'))
    # valeur du produit
    produit = 50
    # calculer la diofference
    result = (wallet) - produit
    # afficher le resulta

    if wallet < produit:
        print('vous navez pas dargen')
    else:
        print('le reste est de  ' + str(result))


if __name__ == '__main__':
    main()