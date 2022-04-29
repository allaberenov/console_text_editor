# Консольный текстовый редактор

![](/images/index.png))
___


## Описание

Консольный те́кстовый реда́ктор  — самостоятельная компьютерная программа, предназначенная для создания и изменения текстовых данных в общем и текстовых файлов, в частности.

Консольный текстовой редактор предназначен для работы с текстовыми файлами в интерактивном режиме. Он позволяет просматривать содержимое текстовых файлов и производить над ними различные действия: вставку, удаление и копирование текста.

___
## ***Функционал***
* Возможность редактирования файла
* Перемещение по тексту при помощи “стрелок”
* Хоткеи для сохранения и выхода.
* Выделение текста
* Буфер обмена
* Подсветка
* Перемещение курсора: по словам, в начало/конец строки. 
* Удаление строк и
слов
* Меню и элементы интерфейса
___
## ***Использование***

После запуска приложения можно вводить текст. 
![](/images/printing.png)
После окончания ввода файл можно сохранить с помощью кнопок меню `Файл` ->`Сохранить` или же `Сохранить как` указав при этом его название сохраняемого файла  и его расширение(`.txt`-расширение по умолчанию) или комбинацией клавиш `Ctrl`+`S` и `Ctrl`+`s`.
Если создаётся новый файл то первое сохранение будет `Сохранить как`

![](/images/menu_saving.png)

Открытие уже существующего файл осуществляется с помощью кнопок на панели меню `Файл`->`Открыть`

Для завершения работы нажмите на кнопу :x: или через меню или же с помощью комбинации `Alt`+`F4`. При этом будет выполнен запрос на сохранение 

![](/images/ask_for_saving.png) 

и только после запрос на выход выход. 

![](/images/quit_file.png) 


___
## ***Утстановка***
Введите или скопируйте следуюшие команды в терминал для установки необходимых пакетов
```
git clone https://github.com/allaberenov/console_editor.git
pip install -r requirements.txt
pip install --upgrade pip
```
___
## ***Запуск программы***
Введите в терминале python 

```
cd console_editor
python text_editor.py
``` 
или

```
cd console_editor
python3 text_editor.py
``` 
___
## ***Детали о модулях***
* в разработке приложения использовался `Python` модуль `tkinter` (для более подробной информации о модуле: [tkinter](https://docs.python.org/3/library/tkinter.html, "Python 3.10.4 tkinter Documentation") )
* в модуле `functions.py` реализованы все необходимые функции для функционирования  приложения
* в модуле `graph_interface.py` реализована создание и корректировка графического и текстовых окон `tkinter`

Приложение разрабатывалась на версии [Python 3.8.10](https://www.python.org/downloads/release/python-3810/)

Почта для обратной связи: ```allaberenov.kerim.21@gmail.com```