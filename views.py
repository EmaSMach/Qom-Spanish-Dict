from tkinter import *
from tkinter import ttk

from pubsub import pub

from forms import WordForm


class MainWindow(Frame):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.master.title("Diccionario Qom - Español")
        self.master.state('zoomed')
        self.pack(expand=YES, fill=BOTH)
        self.table = ttk.Treeview(self, style="mystyle.Treeview")
        self.make_widgets()
        self.make_flowable()

        style = ttk.Style()
        style.configure("mystyle.Treeview", highlightthickness=0, bd=0,
                        font=('Calibri', 14))  # Modify the font of the body
        style.configure("mystyle.Treeview.Heading", font=('Calibri', 13, 'bold'), background='black')  # Modify the font of the headings
        style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})])  # Remove the borders
        style.configure("mystyle.Treeview", rowheight=25)
        style.configure("mystyle.Treeview.Item", padding=0, indicatormargins=3, indicatorsize=50)
        style.configure("mystyle.Treeview.Cell", padding=1)
        style.configure("mystyle.Treeview", fieldbackground="red")

    def make_widgets(self):
        self.lbl_search = ttk.Label(self, text="Búsqueda:")
        self.en_search = ttk.Entry(self)
        self.en_search.bind("<KeyRelease>", self.on_key_release)
        self.en_search.focus()
        self.btn_y = ttk.Button(self, text='ỹ', width=3, command=self.on_btn_y_click)
        self.btn_search = ttk.Button(self, text='Buscar', command=self.on_btn_search_click)
        # binding
        self.bind_all("<Alt-KeyRelease-y>", lambda x: self.btn_y.invoke())
        self.subscribe()
        # placing
        self.lbl_search.grid(row=0, column=0)
        self.en_search.grid(row=0, column=1, sticky='nsew')
        self.btn_y.grid(row=0, column=2)
        self.btn_search.grid(row=0, column=3)
        # table
        self.make_treeview()

    def make_treeview(self):
        self.vsb = ttk.Scrollbar(self)
        self.vsb.config(command=self.table.yview)
        self.table.config(yscrollcommand=self.vsb.set)
        self.vsb.grid(row=1, column=4, sticky='ns')
        self.table.grid(row=1, column=0, columnspan=4, sticky='nsew')
        columns = ('id', 'qom', 'dfs', 'syn', 'var', 'see',)
        self.table.config(columns=columns, show='headings')
        # columns configs
        self.table.column('id', width=2)
        self.table.column('see', width=2)
        # self.table.column('var', width=2)
        # self.table.column('qom', width=4)
        self.table.column('dfs', width=200)
        # headings configs
        self.table.heading('id', text='Id')
        self.table.heading('qom', text='Qom')
        self.table.heading('dfs', text='Definición')
        self.table.heading('syn', text='Sinónimos')
        self.table.heading('var', text='Variante / Variación ')
        self.table.heading('see', text='Ver')
        # binding tree actions
        self.table.bind('<<TreeviewOpen>>', self.on_item_dclick)
        self.table.bind('<<TreeviewClose>>', self.on_item_dclick)

    def make_flowable(self):
        self.rowconfigure(1, weight=1)
        self.columnconfigure(1, weight=1)

    def on_key_release(self, event=None):
        data = self.en_search.get()
        pub.sendMessage("key_released", data=data)

    def on_btn_search_click(self):
        data = self.en_search.get()
        pub.sendMessage("btn_search_clicked", data=data)

    def on_btn_y_click(self, event=None):
        pub.sendMessage("btn_y_clicked")

    def write_y_letter(self):  # event=None):
        self.en_search.insert(INSERT, 'ỹ')
        self.en_search.focus()
        data = self.en_search.get()
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

    def on_item_dclick(self, event=None):
        selected_id = self.table.item(self.table.selection()[0])['values'][0]
        pub.sendMessage("item_dclicked", word_id=selected_id)


def main():
    w = MainWindow()
    w.show()


if __name__ == '__main__':
    main()
