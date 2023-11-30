from tkinter import *
from tkinter import filedialog, messagebox
from tkinter.ttk import Notebook
from PIL import ImageTk, Image
import os


def main_window():
    """
    окно
    """
    def small_manu(root):
        '''
        Небольшое открываеющееся меню с лева сверху. Имеет название File
        '''
        menuu_bar = Menu(root)
        file_menu = Menu(menuu_bar, tearoff=0)
        # Кнопочки открывающиеся в файле
        file_menu.add_command(label='Open', command=add_pictute)
        file_menu.add_command(label='Save', command=save_image)
        file_menu.add_command(label='Close Image', command=close_image)
        file_menu.add_separator() # Полоска разделитель
        file_menu.add_command(label='Close', command=close)
        menuu_bar.add_cascade(label='File', menu=file_menu)

        root.configure(menu=menuu_bar)

    def add_pictute():
        """
        добавление картинки
        """
        image_path = filedialog.askopenfilename(filetypes=(('Images', '*.jpg;*.png;*.jpg'), )) # Принимает путь картинки
        image = Image.open(image_path) # Открывает картинку как pillow
        image_tk = ImageTk.PhotoImage(image.resize((300, 225))) # Открывает картинку как tkinter
        opened_images.append([image_path, image]) # Добавляем в список открытых картинок

        image_tab = Frame(image_tabes)
        image_label = Label(image_tab, image=image_tk)
        image_label.image = image_tk
        image_label.pack()

        image_tabes.add(image_tab, text=image_path.split('/')[-1])
        image_tabes.select(image_tab)

    def open_picture_after_saving(image_path):
        """
        Повторное открытие картинки, после ее сохранения
        """
        #image_path = filedialog.askopenfilename(filetypes=(('Images', '*.jpg;*.png;*.jpg'), )) # Принимает путь картинки
        image = Image.open(image_path) # Открывает картинку как pillow
        image_tk = ImageTk.PhotoImage(image.resize((300, 225))) # Открывает картинку как tkinter
        opened_images.append([image_path, image]) # Добавляем в список открытых картинок

        image_tab = Frame(image_tabes)
        image_label = Label(image_tab, image=image_tk)
        image_label.image = image_tk
        image_label.pack()

        image_tabes.add(image_tab, text=image_path.split('/')[-1])
        image_tabes.select(image_tab)

    def save_image():
        '''
        Функция сохранения фотографии
        '''
        current_tab = image_tabes.select() # Получаем открытую в данный момент вкладку

        if not current_tab: # Если не выделена никакая вкладка, то выходим из метода
            return

        tab_number = image_tabes.index(current_tab) # Индекс открытой вкладки
        old_path, old_ext = os.path.splitext(opened_images[tab_number][0])  # Адрес откуды была открвта картинка, разрешение которое имела картинка
        new_path = filedialog.asksaveasfilename(initialdir=old_path, filetypes=(('Images', '*.jpg;*.png;*.jpg'), )) # Путь в какую папку будем сохранять

        if not new_path: # Если путь не изменен, сохраняем
            return

        new_path, new_ext = os.path.splitext(new_path) # Берем новый путь и проверяем установленное расширение
        if not new_ext: # Если расширение не изменилось сохраняем
            new_ext = old_ext
        elif new_ext != old_ext: # Возвращает ошибку, если расширение не разрешенное
            messagebox.showerror('Неправильное разрешение картинки', f'Ваше расширение должно совпадать с изначальным. Изначальное расширение: {old_ext}, вы передали {new_ext}')
            return

        image = opened_images[tab_number][1] # Получаем картинку для сохранения
        image.save(new_path + new_ext) # Сохраняем
        image.close() # Закрываем

        del opened_images[tab_number] # Удаляем картинку из открытых
        image_tabes.forget(current_tab) # Удаляем вкладку с сохраненной картинкой

        open_picture_after_saving(new_path + new_ext) # Открываем ее заново, уже с новым именем

    def close(event=None):
        '''
        Функция закрытия программы
        '''
        root.quit()

    def close_image(event=None):
        '''
        Функция закрытия картинки
        '''
        currunt_tab = image_tabes.select() # Получаем открытую в данный момент вкладку
        if not currunt_tab: # Если не выделена никакая вкладка, то выходим из метода
            return
        tab_number = image_tabes.index(currunt_tab)  # Индекс открытой вкладки
        del opened_images[tab_number] # Удаляем картинку из списка открытых
        image_tabes.forget(currunt_tab) # Удаляем вкладку с сохраненной картинкой


    root = Tk()
    root.title('photo_editor')
    width, length = 650, 600
    root.geometry(f"{length}x{width}")
    control = Frame(root, height=int(width * 0.35), width=length, bg='#b900b7')
    #photo = Frame(root, height=int(width * 0.65), width=length, bg='#ffc7ff')
    control.pack(side='bottom')
    #photo.pack(side='top')
    ctrl = Canvas(control, height=int(width * 0.35), width=length, bg='#b900b7')
    ctrl.create_line(length // 2, 0, length // 2, int(width * 0.35))
    image_tabes = Notebook(root) # Создаем панель для работы со вкладками
    image_tabes.enable_traversal() # Отвечает зя клавиши для переключения между вкладками
    opened_images = [] # Список с открытыми изображениями

    btn_cut = Button(control, width=18, height=3, text='Обрезка фото', fg='black', bg='white', command=cut)
    btn_filters = Button(control, width=18, height=3, text='Фильтры', fg='black', bg='white', command=filters)
    btn_light = Button(control, width=18, height=3, text='Свет', fg='black', bg='white', command=light)
    btn_contrast = Button(control, width=18, height=3, text='Контраст', fg='black', bg='white', command=contrast)

    btn_cut.place(x=length // 4 - 60, y=int(width * 0.35) // 4 - 20)
    btn_filters.place(x=length // 4 - 60, y=int(width * 0.35) // 4 * 3 - 20)
    btn_light.place(x=length // 4 * 3 - 60, y=int(width * 0.35) // 4 - 20)
    btn_contrast.place(x=length // 4 * 3 - 60, y=int(width * 0.35) // 4 * 3 - 20)

    root.bind("<Escape>", close(root))
    ctrl.pack()
    small_manu(root)
    image_tabes.pack(fill='both', expand=1) # Вкладки с картинками
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
