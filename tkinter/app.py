# importation
from tkinter import *
import webbrowser

window = Tk()

# funct pour lien
def open_browser():
    webbrowser.open_new("https://i.pinimg.com/originals/cf/ba/e8/cfbae8dd039d0e73b2ab5597611d78d7.jpg")


# quelque personalisation
window.title("my app")  # renomme le titre
window.geometry("720x480")  # size par defaut
window.minsize(500, 500)  # taille minimum
window.maxsize(1080, 720)  # taille maximum
window.iconbitmap("logoi.ico")  # mettre un logo dans la barre (pas sur mac)
window.config(background='#F79489')  # mettre un background

# creé la frame
frame = Frame(window, bg="#F79489")

# 1er texte
label_title = Label(frame, text='Bienvenue Voyageur !', font=('Helvetica', 40), bg="#F79489",
                    fg='#F9F1F0')  # variable qui contient un texte et sa personalisation
label_title.pack()  # permet d'afficher le precedent text
# 2eme texte
label_subtitle = Label(frame, text="Je m'appelle Thomas", font=('Helvetica', 25), bg="#F79489",
                       fg='#F9F1F0')  # variable qui contient un texte et sa personalisation
label_subtitle.pack()  # permet d'afficher le precedent text

# ajouter un bouton
ytbutton = Button(frame, bd=0, text="Appuie sur moi", font=('Helvetica', 25), bg="#F9F1F0", fg='#F79489', command=open_browser)
ytbutton.pack(pady=25, fill=X)

# ajouter un element
frame.pack(expand=YES)

window.mainloop()
