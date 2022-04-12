from ttkbootstrap import Style

from Views.GUI import GUI


if __name__ == '__main__':
    style = Style('litera')
    master = style.master
    master.title('Playlist Download')
    master.geometry('625x140')
    gui = GUI(master)
    gui.mainloop()