def main():
    #recolter une premiere note
    note1 = int(input('entre la premiere note'))
    #recolter la deuxioeme note
    note2 = int(input("entrer la seconde note"))
    #recolter la derniere note
    note3 = int(input('entrer la derniere note'))
    #calculer le moyenne
    result = (note1 + note2 + note3) / 3
    #affficher le resulta
    print('la moyenne de jp est de ' + str(result))


if __name__ == '__main__':
    main()