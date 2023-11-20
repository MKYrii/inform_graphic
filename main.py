from tkinter import *


def main_window():
    """
    окно
    """
    root = Tk()
    root.title('photo_editor')
    width, length = 650, 600
    root.geometry(f"{length}x{width}")
    control = Frame(root, height=int(width * 0.35), width=length, bg='#b900b7')
    photo = Frame(root, height=int(width * 0.65), width=length, bg='#ffc7ff')
    control.pack(side='bottom')
    photo.pack(side='top')
    ctrl = Canvas(control, height=int(width * 0.35), width=length, bg='#b900b7')
    ctrl.create_line(length // 2, 0, length // 2, int(width * 0.35))

    btn_cut = Button(control, width=18, height=3, text='Обрезка фото', fg='black', bg='white', command=cut)
    btn_filters = Button(control, width=18, height=3, text='Фильтры', fg='black', bg='white', command=filters)
    btn_light = Button(control, width=18, height=3, text='Свет', fg='black', bg='white', command=light)
    btn_contrast = Button(control, width=18, height=3, text='Контраст', fg='black', bg='white', command=contrast)

    btn_cut.place(x=length // 4 - 60, y=int(width * 0.35) // 4 - 20)
    btn_filters.place(x=length // 4 - 60, y=int(width * 0.35) // 4 * 3 - 20)
    btn_light.place(x=length // 4 * 3 - 60, y=int(width * 0.35) // 4 - 20)
    btn_contrast.place(x=length // 4 * 3 - 60, y=int(width * 0.35) // 4 * 3 - 20)

    ctrl.pack()
    root.mainloop()


def add_pictute(link):
    """
    добавление картинки
    """


def cut():
    pass


def contrast():
    pass


def light():
    pass


def filters():
    pass


main_window()
