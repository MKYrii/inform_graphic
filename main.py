from tkinter import *
from tkinter import filedialog
from PIL import ImageTk, Image


def main_window():
    """
    окно
    """

    def add_pictute(root):
        """
        добавление картинки
        """
        image_path = filedialog.askopenfilename(filetypes=(('Images', '*.jpg;*.png;*.jpg'), ))
        image = ImageTk.PhotoImage((Image.open(image_path)).resize((500, 375)))
        image_panel = Label(root, image=image)
        image_panel.image = image
        image_panel.pack()

    root = Tk()
    root.title('photo_editor')
    width, length = 650, 600
    root.geometry(f"{length}x{width}")
    control = Frame(root, height=int(width * 0.35), width=length, bg='#b900b7')
    photo = Frame(root, height=int(width * 0.65), width=length, bg='#ffc7ff')
    control.pack(side='bottom')
    #photo.pack(side='top')
    ctrl = Canvas(control, height=int(width * 0.35), width=length, bg='#b900b7')
    ctrl.create_line(length // 2, 0, length // 2, int(width * 0.35))

    btn_cut = Button(control, width=18, height=3, text='Обрезка фото', fg='black', bg='white', command=cut)
    btn_filters = Button(control, width=18, height=3, text='Фильтры', fg='black', bg='white', command=filters)
    btn_light = Button(control, width=18, height=3, text='Свет', fg='black', bg='white', command=light)
    btn_contrast = Button(control, width=18, height=3, text='Контраст', fg='black', bg='white', command=contrast)
    btn_add_file = Button(width=5, height=3, text='file', fg='black', bg='white', command=lambda: add_pictute(root))
    btn_add_file.pack()

    btn_cut.place(x=length // 4 - 60, y=int(width * 0.35) // 4 - 20)
    btn_filters.place(x=length // 4 - 60, y=int(width * 0.35) // 4 * 3 - 20)
    btn_light.place(x=length // 4 * 3 - 60, y=int(width * 0.35) // 4 - 20)
    btn_contrast.place(x=length // 4 * 3 - 60, y=int(width * 0.35) // 4 * 3 - 20)
    btn_add_file.place(x=length // 60, y=int(width * 0.7))

    ctrl.pack()
    root.mainloop()


def cut():
    pass


def contrast():
    pass


def light():
    pass


def filters():
    pass


main_window()
