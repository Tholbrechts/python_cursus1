import string
from random import randint, choice
from tkinter import *
bck = '#F79489'

def generate_password():
    password_min = 18
    password_max = 24
    all_chars = string.ascii_letters + string.punctuation + string.digits

    password = "".join(choice(all_chars) for x in range(randint(password_min, password_max)))
    password_entry.delete(0, END)
    password_entry.insert(0, password)

# creer la fenetre
window = Tk()
window.title("Générateur de mot passe")
window.geometry("720x480")
window.config(background=bck)
window.iconbitmap("refresh.ico")

# creer la frame principale
frame = Frame(window, bg=bck)

# creation de l'image
width = 300
height = 300
image = PhotoImage(file="refresh.png").zoom(20).subsample(50)
canvas = Canvas(frame, width=width, height=height, bg=bck, bd=0, highlightthickness=0)
canvas.create_image(width/2, height/2, image=image)
canvas.grid(row=0, column=0, sticky=W)

# creer une sous boite
right_frame = Frame(frame, bg=bck )

# creer un titre
label_title = Label(right_frame, text="Mot de passe", font=("Helvetica", 20), bg=bck, fg="white")
label_title.pack()

# creer un input
password_entry = Entry(right_frame, font=("Helvetica", 20), bg=bck, fg="white", bd=1, highlightthickness=0)
password_entry.pack(pady=5)

# creer un bouton
generate_password_button = Button(right_frame, text="Générer un mot de passe", font=("Helvetica", 20), bg="red", fg=bck, bd=0, highlightthickness=0, command=generate_password)
generate_password_button.pack(pady=5, fill=X)

#sous boite a droite de la frame principal
right_frame.grid(row=0, column=1, sticky=W)

frame.pack(expand=YES)

# creation d'une barre de menu
menu_bar = Menu(window)
# crée un premier menu
file_menu = Menu (menu_bar, tearoff=0)
file_menu.add_command(label="Nouveau", command=generate_password)
file_menu.add_command(label="Quitter", command=window.quit)
menu_bar.add_cascade(label='Fichier', menu=file_menu)

#configurer ,otre fentere menu

window.config(menu=menu_bar)

#afficher la fenetre
window.mainloop()