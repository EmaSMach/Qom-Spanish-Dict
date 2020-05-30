from tkinter import *
from tkinter import ttk


class WordForm(Frame):
    def __init__(self, *args, word, **kwargs):
        super().__init__(*args, **kwargs)
        self.pack(expand=YES, fill=BOTH)
        self.word = word
        self.master.title(f"Palabra - {self.word}")
        self.columnconfigure(1, weight=1)
        self.rowconfigure(1, weight=1)
        self.make_widgets()
        self.fill_widgets()
        self.master.transient()
        self.master.wait_window(self)

    def make_widgets(self):
        self.lbl_qom = ttk.Label(self, text='Qom:')
        self.lbl_qom.grid(row=0, column=0)
        self.ent_qom = ttk.Entry(self)
        self.ent_qom.grid(row=0, column=1, sticky='ew')
        self.lbl_dfs = ttk.Label(self, text='Definición:')
        self.lbl_dfs.grid(row=1, column=0)
        self.txt_dfs = Text(self, wrap='word')
        self.txt_dfs.grid(row=1, column=1, sticky='nsew')
        self.lbl_syn = ttk.Label(self, text='Sinónimo:')
        self.lbl_syn.grid(row=2, column=0)
        self.ent_syn = ttk.Entry(self)
        self.ent_syn.grid(row=2, column=1, sticky='ew')
        self.lbl_var = ttk.Label(self, text='Variante:')
        self.lbl_var.grid(row=3, column=0)
        self.ent_var = ttk.Entry(self)
        self.ent_var.grid(row=3, column=1, sticky='ew')
        self.lbl_see = ttk.Label(self, text='Ver:')
        self.lbl_see.grid(row=4, column=0)
        self.ent_see = ttk.Entry(self)
        self.ent_see.grid(row=4, column=1, sticky='ew')

    def fill_widgets(self):
        self.ent_qom.insert(0, self.word.qom if self.word.qom else '')
        self.txt_dfs.insert(0.0, self.word.dfs if self.word.dfs else '')
        self.ent_syn.insert(0, self.word.syn if self.word.syn else '')
        self.ent_var.insert(0, self.word.var if self.word.var else '')
        self.ent_see.insert(0, self.word.see if self.word.see else '')


def test():
    from db import session
    from models import Word
    root = Tk()
    wd = session.query(Word).first()
    w = WordForm(root, word=wd)
    root.mainloop()


if __name__ == '__main__':
    test()
