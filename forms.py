from tkinter import *
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText


class WordForm(Toplevel):
    def __init__(self, *args, word, **kwargs):
        super().__init__(*args, **kwargs)
        #self.pack(expand=YES, fill=BOTH)
        self.word = word
        self.title(f"Palabra - {self.word.qom.capitalize()}")
        self.geometry('600x500')
        self.columnconfigure(1, weight=1)
        self.rowconfigure(1, weight=1)
        self.make_widgets()
        self.fill_widgets()
        self.add_style()
        self.add_optional_style()
        self.grab_set()
        self.transient(self.master)
        self.focus()
        self.wait_window(self)

    def add_optional_style(self):
        for child in self.winfo_children():
            if isinstance(child, ttk.Entry):
                child.configure(state='readonly')
                child.configure(font=('Cambria', 22, 'italic'))
            self.txt_dfs.config(font=('Cambria', 18))
            self.txt_dfs.configure(state='disabled')

    def add_style(self):
        self.style = ttk.Style(self)
        self.style.configure("self.TLabel", font=('Calibri', 22, 'italic'))
        # self.style.configure("this.TButton", font=('Calibri', 22, 'italic'))

    def make_widgets(self):
        self.lbl_qom = ttk.Label(self, text='Qom:', anchor='w')
        self.lbl_qom.grid(row=0, column=0, sticky='ew')
        self.ent_qom = ttk.Entry(self)
        self.ent_qom.grid(row=0, column=1, sticky='ew')
        self.lbl_dfs = ttk.Label(self, text='Definición:', anchor='w')
        self.lbl_dfs.grid(row=1, column=0, sticky='n')
        self.txt_dfs = ScrolledText(self, wrap='word')
        self.txt_dfs.grid(row=1, column=1, sticky='nsew')
        self.lbl_syn = ttk.Label(self, text='Sinónimo:', anchor='w')
        self.lbl_syn.grid(row=2, column=0, sticky='ew')
        self.ent_syn = ttk.Entry(self)
        self.ent_syn.grid(row=2, column=1, sticky='ew')
        #self.lbl_var = ttk.Label(self, text='Variante:')
        #self.lbl_var.grid(row=3, column=0)
        #self.ent_var = ttk.Entry(self)
        #self.ent_var.grid(row=3, column=1, sticky='ew')
        self.lbl_see = ttk.Label(self, text='Ver:', anchor='w')
        self.lbl_see.grid(row=4, column=0, sticky='ew')
        self.ent_see = ttk.Entry(self)
        self.ent_see.grid(row=4, column=1, sticky='ew')

    def fill_widgets(self):
        self.ent_qom.insert(0, self.word.qom.capitalize() if self.word.qom else '')
        dfs_full = (self.word.dfs.capitalize() if self.word.dfs else '') + \
                   '\n' + \
                   ('Variante: ' + self.word.var.capitalize() if self.word.var else '')
        self.txt_dfs.insert(0.0, dfs_full)
        self.ent_syn.insert(0, self.word.syn.capitalize() if self.word.syn else '')
        #self.ent_var.insert(0, self.word.var if self.word.var else '')
        self.ent_see.insert(0, self.word.see.capitalize() if self.word.see else '')


def test():
    from db import session
    from models import Word
    root = Tk()
    wd = session.query(Word).first()
    w = WordForm(root, word=wd)
    root.mainloop()


def gettin():
    # function to correct some fields in the database (not needed actually)
    # do not run
    from db import session
    from models import Word
    # objs = session.query(self.model).filter(self.model.qom.like(f"{data}%")).limit(100)
    palabras = session.query(Word).filter(Word.var.like("(%"))
    for p in palabras:
        p.dfs += "\nVariante:" + p.var
        p.var = None
        print(p, "VAR:", p.var)
        print(p, "DFS:", p.dfs)
        input()


if __name__ == '__main__':
    test()
