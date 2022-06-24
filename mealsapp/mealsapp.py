from tkinter import  *
window = Tk()
window.title('my meal app')
window.geometry('1080x720')
window.minsize(500, 500)
window.maxsize(1000, 700)
window.config(background="#F79489")
import os
import random

def meal_gen():
    if os.path.exists("../mealsapp/meals.txt"):
        with open("../mealsapp/meals.txt", "r+") as file:
            meals_liste = file.readlines()
            meal_random_choice = random.choice((meals_liste))
            file.close()
            meal_entry.delete(0, END)
            meal_entry.insert(0, meal_random_choice)
    else:
        print("le document n'existe pas")
# cree la frame
frame = Frame(window, bg="#F79489")
# creation de l'image
width = 300
height = 300
image = PhotoImage(file="images/meal.png").zoom(10).subsample(70)
canvas = Canvas(frame, width=width, height=height, bg="#F79489", bd=0, highlightthickness=0)
canvas.create_image(width/2, height/2, image=image)
canvas.grid(row=0, column=0, sticky=W)
# creer une sous boite
right_frame = Frame(frame, bg="#F79489")
# creer un titre
label_title = Label(right_frame, text="Votres plats aleatoire", font=("Helvetica", 20), bg="#F79489", fg="white")
label_title.pack()
#sous boite a droite de la frame principal
right_frame.grid(row=0, column=1, sticky=W)
frame.pack(expand=YES)
# creer un input
meal_entry = Entry(right_frame, font=("Helvetica", 20), bg="#F79489", fg="white", bd=1, highlightthickness=0)
meal_entry.pack(pady=5)
# creer un bouton
meal_generate_button = Button(right_frame, text="bouton", font=("Helvetica", 20), bg="white", fg="#F79489", bd=0, highlightthickness=0, command=meal_gen)
meal_generate_button.pack(pady=5, fill=X)





window.mainloop()