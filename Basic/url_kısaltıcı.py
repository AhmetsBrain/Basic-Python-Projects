import pyperclip
import pyshorteners
from tkinter import *

root = Tk()
root.geometry("400x200")
root.title("Link Kısaltıcı")
root.configure(bg = "#49A")
url = StringVar()
url_adress = StringVar()

def urlshortener():
    urladress = url.get()
    url_short = pyshorteners.Shortener().tinyurl.short(urladress)
    url_adress.set(url_short)

def copyurl():
    url_short = url.adress.get()
    pyperclip.copy(url_short)

Label(root, text = "Ahmet'in Link Kısaltıcısı", font="poppins").pack(pady=10)
Entry(root, textvariable = url).pack(pady=5)
Button(root, text="Kısaltılmış Bir Link oluştur", command=urlshortener).pack(pady=7)
Entry(root, textvariable= url_adress).pack(pady=5)
Button(root, text= "Linki Kopyala", command = copyurl).pack(pady=5)


root.mainloop()