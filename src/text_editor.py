import functions as func

from graph_interface import root

root.bind('<Control-s>', func.key_pressed)

root.bind('<Control-S>', func.key_pressed)

root.protocol("WM_DELETE_WINDOW", func.notepad_exit)

root.mainloop()
