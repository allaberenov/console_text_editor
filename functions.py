import tkinter as tk
from tkinter import messagebox, filedialog
from graph_interface import root, text_fild, file_menu, main_menu

FILE_PATH = ""
FILE_OPENED = False


def notepad_exit():
    """
    Закрывает окно проверяя требуется ли сохранение или нет
    
    Параметры:
        ---
    Возращаемое значение:
        ---
    """

    ans = messagebox.askyesnocancel('Сохранение файла', 'Требуется ли сохранить файл?')
    if ans:
        if FILE_OPENED:
            save_opened_file()
        else:
            save_as()
        answer = messagebox.askokcancel('Выход', 'Вы точно хотите выйти?')
        if answer:
            root.destroy()
            exit()
    elif not ans:
        answer = messagebox.askokcancel('Выход', 'Вы точно хотите выйти?')
        if answer:
            root.destroy()
            exit()


def open_file():
    """
    Открывет файл указанный в диалоговом окне
    
    Параметры:
        ---
    Возращаемое значение:
        ---
    """

    file_path = filedialog.askopenfilename(title='Выбор файла',
                                           filetypes=(('Текстовые документы (*.txt)', '*.txt'), ('Все файлы', '*.*')))
    if file_path:
        text_fild.delete('1.0', tk.END)
        text_fild.insert('1.0', open(file_path, encoding='utf-8').read())

        global FILE_OPENED
        FILE_OPENED = True
        global FILE_PATH
        FILE_PATH = file_path


def save_as():
    """
    Вызывает диалоговое окно, где можно указать путь и формат охраняемого файла
    
    Параметры:
        ---
    Возращаемое значение:
        ---
    """

    file_path = filedialog.asksaveasfilename(filetypes=(('Текстовые документы (*.txt)', '*.txt'), ('Все файлы', '*.*')))
    print(file_path)
    if file_path == ():
        pass
    else:
        f = open(file_path, 'w', encoding='utf-8')
        global FILE_PATH, FILE_OPENED
        FILE_OPENED = True
        FILE_PATH = file_path
        text = text_fild.get('1.0', tk.END)
        f.write(text)
        f.close()


def save_opened_file():
    """
    Сохраняет уже ранее открывавший файл
    
    Параметры:
        ---
    Возращаемое значение:
        ---
    """

    f = open(FILE_PATH, 'w', encoding='utf-8')
    text = text_fild.get('1.0', tk.END)
    f.write(text)
    f.close()


def key_pressed(*args):
    """
    Вызывает соответствующую функцию по обработке нажатия клавиши
    
    Параметры:
        *args - информация о нажатой кнопке
    Возвращаемое значение:
        ---
    
    """
    save_as()


def save_file():
    """
    Если был открыт существующий файл, то сохраняет всё в уже открытом файле
    Если же открыт несуществующий файл, то сохраняет его  как новый файл
    
    Параметры:
        *args- 
    Возращаемое значение:
        ---
    """

    if not FILE_OPENED:
        save_as()
    else:
        save_opened_file()


# Добавление элементов в меню
file_menu.add_command(label='Открыть', command=open_file)
file_menu.add_command(label='Сохранить', command=save_file)
file_menu.add_command(label='Сохранить как', command=save_as)
file_menu.add_command(label='Закрыть', command=notepad_exit)
root.config(menu=file_menu)

main_menu.add_cascade(label='Файл', menu=file_menu)
root.config(menu=main_menu)
