import tkinter as tk

from tkinter import Tk

root = Tk()
root.title('Текстовый редактор')
root.geometry('600x700')

WINDOW_BACKGROUND_COLOUR = 'darkblue'
LETER_COLOR = 'lime'
CURSOR_COLOR = 'white'

# Создание поле для ввода"
f_text = tk.Frame(root)
f_text.pack(fill=tk.BOTH, expand=1)
text_fild = tk.Text(f_text, background=WINDOW_BACKGROUND_COLOUR, insertbackground=CURSOR_COLOR, fg=LETER_COLOR,
                    font='Arial 14 bold')

# Установка элементов файлового меню
main_menu = tk.Menu(root)
file_menu = tk.Menu(main_menu, tearoff=0)

text_fild.pack(expand=1, fill=tk.BOTH, side=tk.LEFT)
