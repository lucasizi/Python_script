import tkinter as tk
import random
from tkinter import messagebox
import webbrowser

def move_button_1(e):
    if abs(e.x - button_1.winfo_x()) < 50 and abs(e.y - button_1.winfo_y()) < 40:
        x = random.randint(0, root.winfo_width() - button_1.winfo_width())
        y = random.randint(0, root.winfo_height() - button_1.winfo_height())
        button_1.place(x=x, y=y)

def reset_button_1(e):
    button_1.place(x=250, y=300)

def accepted():
    messagebox.showinfo('amigo(a) ', 'Eu te amo , quero 10 conto no pix <3')

def denied(e):
    messagebox.showinfo('amigo(a)', 'Tente de novo,seu vacilão')
    webbrowser.reload()

root = tk.Tk()
root.title('aceitas?')
root.geometry('600x600')
text_id = tk.Label(root, bg='#B0E0E6', text='ser humilde paga um lanche pra mim?', fg='#590d22', font=('Montserrat', 24, 'bold'))
root.configure(background='#F0F8FF')



margin = tk.Canvas(root, width=500, bg='#F0F8FF', height=100, bd=0, highlightthickness=0, relief='ridge')
margin.pack()

text_id = tk.Label(root, bg='#F0F8FF', text='ser humilde paga um lanche pra mim?', fg='#590d22', font=('Montserrat', 24, 'bold'))
text_id.pack()

button_1 = tk.Button(root, text='Não', bg='#F0F8FF', relief=tk.RIDGE, bd=3, font=('Montserrat', 8, 'bold'))
button_1.place(x=250, y=300)

root.bind('<Motion>', move_button_1)
button_1.bind('<Leave>', reset_button_1)
button_1.bind('<Button-1>', denied)

button_2 = tk.Button(root, text='Sim', bg='#F0F8FF', relief=tk.RIDGE, bd=3, command=accepted, font=('Montserrat', 14, 'bold'))
button_2.place(x=250, y=350)

root.mainloop()

pyinstaller -onefile -noconsole 
