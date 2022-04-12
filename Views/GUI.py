from tkinter import ttk, Label, Frame, Entry
from ttkbootstrap import Style, Button
from Controllers.DownloadController import DownloadController


class GUI(Frame):
    container = Frame()
    container2 = Frame(container)
    text = Label(container2, text="URI: ", font=("Monospace", 14))
    text.grid(row=0, column=0)
    box = Entry(container2, font=("Monospace", 14), width=50)
    text_get = box.get()
    box.grid(row=0, column=1, pady=10, padx=10)
    download = DownloadController(text_get)
    btn = Button(container2, bootstyle="info", text="Baixar", padding=10, command=download.makeDownloadNow)
    btn.grid(row=5, column=1)
    container2.pack()
    container.pack()


if __name__ == '__main__':
    style = Style('litera')
    master = style.master
    master.title('Playlist Download')
    master.geometry('625x140')
    gui = GUI(master)
    gui.mainloop()
