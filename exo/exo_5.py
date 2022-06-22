
def get_vowels_numbers(word):
    nb_vowels = 0

    for letter in word:
        if letter in ['a',  "e", "i", "o", "u", "y"]:
            nb_vowels += 1


    return nb_vowels

word = input("entre un mot")
vowels_count = get_vowels_numbers(word)
print("il ya", vowels_count, "voyelles dans le mot ", word)