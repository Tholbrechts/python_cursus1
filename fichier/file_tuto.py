
import os
import random

if os.path.exists("../mealsapp/meals.txt"):
    with open("../mealsapp/meals.txt", "r+") as file:
        meals_liste = file.readlines()
        meal_random_choice = random.choice((meals_liste))
        print(meal_random_choice)
        file.close()
else:
    print("le document n'existe pas")