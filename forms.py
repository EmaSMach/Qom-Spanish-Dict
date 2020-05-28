from tkinter import *


class WordForm(Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.make_widgets()

    def make_widgets(self):
        self.lbl_qom = Label(self, text='Qom:')
        self.lbl_qom.grid(row=0, column=0)


def main():
    root = Tk()
    w = WordForm(root)
    w.pack()
    root.mainloop()


if __name__ == '__main__':
    main()
