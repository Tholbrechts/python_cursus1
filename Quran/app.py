import quran_random

from tkinter import *

window = Tk()
window.title('quran random')
window.geometry('1080x720')
window.minsize(500, 500)

window.config(background="#F79489")
frame = Frame(window, bg="black")
right_frame = Frame(frame, bg="black")
right_frame.grid(row=0, column=1, sticky=W)

# creation de l'image
width = 300
height = 300
image = PhotoImage(file="images/logoi.png").zoom(10).subsample(70)
canvas = Canvas(frame, width=width, height=height, bg="#F79489", bd=0, highlightthickness=0)
canvas.create_image(width / 2, height / 2, image=image)
canvas.grid(row=0, column=0, sticky=W)


def button():
    Label(window, text=quran_random.quran()).pack()
    A = B.get()
    return A
B = StringVar()
C = ""

Submit = Button(window, text="Submit", command=button)
Submit.pack()

window.mainloop()
