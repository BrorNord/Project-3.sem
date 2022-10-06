from tkinter import *
from tkinter import messagebox
import pyqrcode

# Setting names and config for the tkinter popup
ws = Tk()
ws.title("")
ws.config(bg='#ff8200')
ws.geometry("400x400")

# Defines the destination of the QR code
site = "http://127.0.0.1:1880/#flow/5cdc29b3ac187387"


def generate_QR():
    global qr, img
    # Opens the QR code
    qr = pyqrcode.create(site)
    # Set the size of the qrcode
    img = BitmapImage(data=qr.xbm(scale=6))
    display_code()


def display_code():
    img_lbl.config(image=img)


button = Button(
    ws,
    text="generate_QR",
    width=15,
    command=generate_QR
)
button.pack(
    pady=20)  # Sets the amount of padding around the button. creates a blank bubble around the button essentially

img_lbl = Label(
    ws,
    bg='#20c1c9')  # sets the background of the QR code
img_lbl.pack()
output = Label(
    ws,
    text="",
    # You can put text, so you have to set this to be the same as the background, otherwise you end up with a random white bar
    bg='#20c1c9'
)
output.pack()

ws.mainloop()