from tkinter import font
from tkinter import *
from tkinter.filedialog import *
import inspect
from PIL import ImageTk, Image


root = Tk()
root.title('photo_editor')
width, length = 650, 600
root.geometry(f"{length}x{width}")
control = Frame(root, height=int(width * 0.35), width=length, bg='#b900b7')
photo = Frame(root, height=int(width * 0.65), width=length, bg='#ffc7ff')
control.pack(side='bottom')
photo.pack(side='top')
pht = Canvas(photo, height=int(width * 0.65), width=length, bg='#ffc7ff')
ctrl = Canvas(control, height=int(width * 0.35), width=length, bg='#b900b7')
ctrl.create_line(length // 2, 0, length // 2, int(width * 0.35))


def add_pictute():
    global pht
    f = PhotoImage(file="lp.gif")

    img = Label(pht, image=f)
    print(img)
    img.place()
    pht.create_image(100, 100, image=f)


def cut():
    pass


def contrast():
    pass


def light():
    pass


def filters():
    pass


ctrl.pack()
pht.pack()

font_btn = font.Font(family="Arial", size=13, weight="normal")
btn_cut = Button(control, width=15, height=2, font=font_btn, text='Обрезка фото', fg='black', bg='white', command=cut)
btn_filters = Button(control, width=15, height=2, font=font_btn, text='Фильтры', fg='black', bg='white', command=filters)
btn_light = Button(control, width=15, height=2, font=font_btn, text='Свет', fg='black', bg='white', command=light)
btn_contrast = Button(control, width=15, height=2, font=font_btn, text='Контраст', fg='black', bg='white', command=contrast)

btn_cut.place(x=length // 4 - 60, y=int(width * 0.35) // 4 - 20)
btn_filters.place(x=length // 4 - 60, y=int(width * 0.35) // 4 * 3 - 20)
btn_light.place(x=length // 4 * 3 - 60, y=int(width * 0.35) // 4 - 20)
btn_contrast.place(x=length // 4 * 3 - 60, y=int(width * 0.35) // 4 * 3 - 20)

btn_photo = Button(photo, width=15, height=2, font=font_btn, text='Добавить фото', fg='black', bg='white', command=add_pictute)
btn_photo.place(x=length // 2 - 70, y=int(width * 0.55) - 10)

root.mainloop()