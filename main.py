from tkinter import *
from tkinter import filedialog, messagebox
from tkinter.ttk import Notebook

import PIL
from PIL import ImageTk, Image, ImageOps, ImageFilter
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
        file_menu.add_command(label='Save', command=save_current_image)
        file_menu.add_command(label='Save as', command=save_image)
        file_menu.add_command(label='Close Image', command=close_image)
        file_menu.add_separator() # Полоска разделитель
        file_menu.add_command(label='Close', command=close)
        menuu_bar.add_cascade(label='File', menu=file_menu)

        # Функции для поворота картинки в окне Rotation
        edit_menu = Menu(menuu_bar, tearoff=0)

        rotate_menu = Menu(edit_menu, tearoff=0)
        rotate_menu.add_command(label='Rotate left by 90', command= lambda: rotate_image(90))
        rotate_menu.add_command(label='Rotate right by 90', command=lambda: rotate_image(-90))

        flip_menu = Menu(edit_menu, tearoff=0)
        flip_menu.add_command(label='Flip horisontally', command=lambda: flip_image('horisontally'))
        flip_menu.add_command(label='Flip vertically', command=lambda: flip_image('vertically'))

        resize_menu = Menu(edit_menu, tearoff=0)
        resize_menu.add_command(label='25% of original size', command=lambda : resize_image(25))
        resize_menu.add_command(label='50% of original size', command=lambda : resize_image(50))
        resize_menu.add_command(label='70% of original size', command=lambda : resize_image(70))
        resize_menu.add_command(label='120% of original size', command=lambda : resize_image(120))
        resize_menu.add_command(label='150% of original size', command=lambda : resize_image(150))

        filter_menu = Menu(edit_menu, tearoff=0)
        filter_menu.add_command(label='Blur', command=lambda : apply_filter(ImageFilter.BLUR))
        filter_menu.add_command(label='Contrast', command=lambda : apply_filter(ImageFilter.SHARPEN))
        filter_menu.add_command(label='Detail', command=lambda : apply_filter(ImageFilter.DETAIL))
        filter_menu.add_command(label='Smooth', command=lambda : apply_filter(ImageFilter.SMOOTH))
        filter_menu.add_command(label='Contour', command=lambda : apply_filter(ImageFilter.CONTOUR))
        filter_menu.add_command(label='Emboss', command=lambda : apply_filter(ImageFilter.EMBOSS))

        crop_menu = Menu(edit_menu, tearoff=0)
        crop_menu.add_command(label='Start selection', command=lambda : selection_area())
        crop_menu.add_command(label='Stop selection', command=lambda : stop_area_selection())

        edit_menu.add_cascade(label='Rotation', menu=rotate_menu)
        edit_menu.add_cascade(label='Flip image', menu=flip_menu)
        edit_menu.add_cascade(label='Resize', menu=resize_menu)
        edit_menu.add_cascade(label='Filters', menu=filter_menu)
        edit_menu.add_cascade(label='Crop', menu=crop_menu)

        menuu_bar.add_cascade(label='Edit', menu=edit_menu)

        root.configure(menu=menuu_bar)

    def add_pictute():
        """
        добавление картинки
        """
        image_path = filedialog.askopenfilename(filetypes=(('Images', '*.jpg;*.png;*.jpg'), )) # Принимает путь картинки
        image = Image.open(image_path) # Открывает картинку как pillow
        image_tk = ImageTk.PhotoImage(image) # Открывает картинку как tkinter
        opened_images.append([image_path, image]) # Добавляем в список открытых картинок
        image_tab = Frame(image_tabes) # Создаем рабочую область на добавленной вкладке  ??? change black area

        # Создаем холст и размещаем на нем картинку
        image_panel = Canvas(image_tab, width=image_tk.width(), height=image_tk.height(), bd=0, highlightthickness=0)
        image_panel.image = image_tk
        image_panel.create_image(0, 0, image=image_tk, anchor='nw')
        image_panel.pack(expand='yes')

        # Добавляем новую вкладку и ее название-название картинки
        image_tabes.add(image_tab, text=image_path.split('/')[-1])
        image_tabes.select(image_tab)

    def open_picture_after_saving(image_path):
        """
        Повторное открытие картинки, после ее сохранения
        """
        #image_path = filedialog.askopenfilename(filetypes=(('Images', '*.jpg;*.png;*.jpg'), )) # Принимает путь картинки
        image = Image.open(image_path)
        image_tk = ImageTk.PhotoImage(image)
        opened_images.append([image_path, image])
        image_tab = Frame(image_tabes)

        image_panel = Canvas(image_tab, width=image_tk.width(), height=image_tk.height(), bd=0, highlightthickness=0)
        image_panel.image = image_tk
        image_panel.create_image(0, 0, image=image_tk, anchor='nw')
        image_panel.pack(expand='yes')

        image_tabes.add(image_tab, text=image_path.split('/')[-1])
        image_tabes.select(image_tab)

    def get_current_data():
        '''
        Возврашяет три параметра - (current_tab, image, path) открытую вкладку, картинку, путь до картинки
        '''
        current_tab = image_tabes.select()  # Получаем открытую в данный момент вкладку
        if not current_tab:  # Если не выделена никакая вкладка, то выходим из метода
            return None, None, None

        tab_number = image_tabes.index(current_tab)  # Индекс открытой вкладки
        path, image = opened_images[tab_number] # Путь и картинка активной вкладки
        return current_tab, path, image

    def save_image():
        '''
        Функция сохранения фотографии
        '''
        current_tab, path, image = get_current_data()
        if not current_tab: # Если не выделена никакая вкладка, то выходим из метода
            return

        tab_number = image_tabes.index(current_tab) # Индекс открытой вкладки
        old_path, old_ext = os.path.splitext(path)  # Адрес откуды была открвта картинка, разрешение которое имела картинка
        new_path = filedialog.asksaveasfilename(initialdir=old_path, filetypes=(('Images', '*.jpg;*.png;*.jpg'), )) # Путь в какую папку в которую будем сохранять

        if not new_path: # Если путь не изменен, сохраняем
            return

        new_path, new_ext = os.path.splitext(new_path) # Берем новый путь и проверяем установленное расширение
        if not new_ext: # Если расширение не изменилось сохраняем
            new_ext = old_ext
        elif new_ext != old_ext: # Возвращает ошибку, если расширение не разрешенное
            messagebox.showerror('Неправильное разрешение картинки', f'Ваше расширение должно совпадать с изначальным. Изначальное расширение: {old_ext}, вы передали {new_ext}')
            return

        image.save(new_path + new_ext) # Сохраняем
        image.close() # Закрываем

        del opened_images[tab_number] # Удаляем картинку из открытых
        image_tabes.forget(current_tab) # Удаляем вкладку с сохраненной картинкой

        open_picture_after_saving(new_path + new_ext) # Открываем ее заново, уже с новым именем

    def save_current_image():
        '''
        Сохранение текущей картинки без запроса путя - замена картинки на новый вариант
        '''
        current_tab, path, image = get_current_data()
        if not current_tab:
            return

        tab_number = image_tabes.index(current_tab)
        path, image = opened_images[tab_number]
        opened_images[tab_number][0] = path
        image.save(path)

    def close(event=None):
        '''
        Функция закрытия программы
        '''
        root.quit()

    def close_image(event=None):
        '''
        Функция закрытия картинки
        '''
        current_tab, path, image = get_current_data()
        if not current_tab:
            return
        tab_number = image_tabes.index(current_tab)
        del opened_images[tab_number] # Удаляем картинку из списка открытых
        image_tabes.forget(current_tab) # Удаляем вкладку

    def update_image_inside_app(current_tab, image):
        '''
        Обновление картинки после какого-то изменения
        '''
        tab_number = image_tabes.index(current_tab)  # Индекс открытой вкладки
        tab_frame = image_tabes.children[current_tab[current_tab.rfind('!'):]]
        canvas = tab_frame.children['!canvas']
        opened_images[tab_number][1] = image  # записываем новую картинку

        image_tk = ImageTk.PhotoImage(image)
        canvas.delete("all")
        canvas.image = image_tk
        canvas.configure(width=image_tk.width(), height=image_tk.height())
        canvas.create_image(0, 0, image=image_tk, anchor="nw")
    def rotate_image(degrees):
        '''
        Поворот картинки
        '''
        current_tab, path, image = get_current_data()
        if not current_tab:
            return

        image = image.rotate(degrees) # поворачиваем на градусы = degrees
        update_image_inside_app(current_tab, image)

    def flip_image(flip_type):
        '''
        Отзеркаливание картинки
        '''
        current_tab, path, image = get_current_data()
        if not current_tab:
            return

        if flip_type == 'horisontally':
            image = ImageOps.mirror(image)
        if flip_type == 'vertically':
            image = ImageOps.flip(image)
        update_image_inside_app(current_tab, image)

    def resize_image(persents):
        '''
        Изменение размера картинки
        '''
        current_tab, path, image = get_current_data()
        if not current_tab:
            return

        width, hight = image.size
        new_width = (width * persents) // 100
        new_higth = (hight * persents) // 100

        image = image.resize((new_width, new_higth), PIL.Image.LANCZOS)
        update_image_inside_app(current_tab, image)

    def apply_filter(filter_type):
        '''
        Фильтры
        '''
        current_tab, path, image = get_current_data()
        if not current_tab:
            return
        image = image.filter(filter_type)
        update_image_inside_app(current_tab, image)
    def selection_area():
        '''
        Выделение произвольной области
        '''
        current_tab = image_tabes.select()
        if not current_tab:
            return
        tab_frame = image_tabes.children[current_tab[current_tab.rfind('!'):]]
        canvas = tab_frame.children['!canvas']

        global canvas_for_selection, selection_rect
        canvas_for_selection = canvas
        selection_rect = canvas.create_rectangle(selection_top_x, selection_bottom_x, selection_top_y, selection_bottom_y,
                                                 dash=(10,10), fil='', outline='white', width=2)

        canvas.bind("<Button-1>", get_selection_start_pos) # Событие - нажатие левой кнопки мыши
        canvas.bind("<B1-Motion>", update_selection_and_pos) # Событие - передвижение курсора

    def get_selection_start_pos(event):
        '''
        Получение коорлинат начала области выделения при нажатии левой кнопки мыши
        '''
        global selection_top_x, selection_top_y
        selection_top_x, selection_top_y = event.x, event.y
    def update_selection_and_pos(event):
        '''
        Получение выделенной области по координатам
        '''
        global selection_bottom_x, selection_bottom_y, canvas_for_selection, selection_rect
        selection_bottom_x, selection_bottom_y = event.x, event.y
        if canvas_for_selection is not None and selection_rect is not None:
            canvas_for_selection.coords(selection_rect, selection_top_x, selection_top_y, selection_bottom_x, selection_bottom_y)
    def stop_area_selection():
        '''
        Обрезание картинки удаление данных по области выделения
        '''
        global canvas_for_selection, selection_rect, selection_top_x, selection_top_y, selection_bottom_x, selection_bottom_y
        canvas_for_selection.unbind("<Button-1>")
        canvas_for_selection.unbind("<B1-Motion>")

        canvas_for_selection.delete(selection_rect)
        crop_image()

        selection_rect = None
        canvas_for_selection = None
        selection_top_x, selection_top_y, selection_bottom_x, selection_bottom_y =0, 0, 0, 0
    def crop_image():
        '''
        Обрезание картинки
        '''
        current_tab, path, image = get_current_data()
        if not current_tab:
            return
        image = image.crop((selection_top_x, selection_top_y, selection_bottom_x, selection_bottom_y))
        update_image_inside_app(current_tab, image)

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

    # Координаты квадрата для выделения области
    global selection_top_x
    selection_top_x = 0
    global selection_top_y
    selection_top_y = 0
    global selection_bottom_x
    selection_bottom_x = 0
    global selection_bottom_y
    selection_bottom_y = 0
    global canvas_for_selection
    canvas_for_selection = None
    global selection_rect # Выделенный прямоугольник
    selection_rect = None

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
