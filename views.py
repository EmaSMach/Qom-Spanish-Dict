from tkinter import *
from tkinter import ttk

from pubsub import pub


class MainWindow(Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.master.title("Diccionario Qom - Español")
        self.master.state('zoomed')
        self.pack(expand=YES, fill=BOTH)
        self.table = ttk.Treeview(self)
        self.make_widgets()
        self.make_flowable()

    def make_widgets(self):
        self.lbl_search = ttk.Label(self, text="Búsqueda:")
        self.en_serch = ttk.Entry(self)
        self.en_serch.bind("<KeyRelease>", self.on_key_release)
        self.en_serch.focus()
        self.btn_y = ttk.Button(self, text='ỹ', width=3, command=self.on_btn_y_click)
        self.btn_search = ttk.Button(self, text='Buscar', command=self.on_btn_search_click)
        # binding
        self.bind_all("<Alt-KeyRelease-y>", self.on_btn_y_click)
        # placing
        self.lbl_search.grid(row=0, column=0)
        self.en_serch.grid(row=0, column=1, sticky='nsew')
        self.btn_y.grid(row=0, column=2)
        self.btn_search.grid(row=0, column=3)
        # table
        self.make_treeview()
        self.subscribe()

    def make_treeview(self):
        self.vsb = ttk.Scrollbar(self)
        self.vsb.config(command=self.table.yview)
        self.table.config(yscrollcommand=self.vsb.set)
        self.vsb.grid(row=1, column=4, sticky='ns')
        self.table.grid(row=1, column=0, columnspan=4, sticky='nsew')
        columns = ('id', 'qom', 'dfs', 'syn', 'var', 'see',)
        self.table.config(columns=columns, show='headings')
        # columns configs
        self.table.column('id', width=4)
        # headings configs
        self.table.heading('id', text='Id')
        self.table.heading('qom', text='Qom')
        self.table.heading('dfs', text='Definición')
        self.table.heading('syn', text='Sinónimos')
        self.table.heading('var', text='Variante / Variación ')
        self.table.heading('see', text='Ver')

    def make_flowable(self):
        self.rowconfigure(1, weight=1)
        self.columnconfigure(1, weight=1)

    def on_key_release(self, event=None):
        data = self.en_serch.get()
        pub.sendMessage("key_released", data=data)

    def on_btn_search_click(self):
        data = self.en_serch.get()
        pub.sendMessage("btn_search_clicked", data=data)

    def on_btn_y_click(self, event=None):
        pub.sendMessage("btn_y_clicked")

    def write_y_letter(self, event=None):
        data = self.en_serch.get()
        self.en_serch.insert(INSERT, 'ỹ')
        self.en_serch.focus()
        pub.sendMessage("letter_inserted", data=data)

    def subscribe(self):
        pub.subscribe(self.write_y_letter, "btn_y_clicked")

    def show(self):
        self.mainloop()

    def clear_table(self):
        self.table.delete(*self.table.get_children())

    def update_table(self, data):
        self.clear_table()
        for register in data:
            self.table.insert(index=END, parent='', values=register)


def main():
    w = MainWindow()
    w.show()


if __name__ == '__main__':
    main()
