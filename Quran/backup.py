from tkinter import  *
import quran_random
window = Tk()
window.title('my meal app')
window.geometry('1080x720')
window.minsize(500, 500)
window.maxsize(1000, 700)
window.config(background="#F79489")
# cree la frame
frame = Frame(window, bg="#F79489")
# creer une sous boite
right_frame = Frame(frame, bg="red")
right_frame.grid(row=0, column=1, sticky=W)

frame.pack(expand=YES)

def button():
    label = Label(right_frame, text=quran_random.quran())
    label.pack()

    A = B.get()
    return A
B = StringVar()
C = ""

Submit = Button(right_frame, text="Submit", command=button)
Submit.pack()

window.mainloop()



