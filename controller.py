from views import MainWindow
from models import Word
from db import session
from tkinter import END
from pubsub import pub


class Controller:
    def __init__(self, model, view, *args, **kwargs):
        self.model = model
        self.view = view()
        pub.subscribe(self.search, "btn_search_clicked")
        pub.subscribe(self.update_table, "key_released")
        pub.subscribe(self.update_table, "letter_inserted")
        self.show_all()

    def show_all(self):
        objs = session.query(self.model).all()
        for obj in objs:
            elements = [el if el else '' for el in obj.to_list()]
            self.view.table.insert(index=END, parent='', values=elements)

    def run(self):
        self.view.show()

    def search(self, data):
        objs = session.query(self.model).filter(self.model.qom.like(f"{data}%")).all()
        self.view.update_table(obj.to_list() for obj in objs)

    def update_table(self, data):
        self.search(data)


def main():
    controller = Controller(Word, MainWindow)
    controller.run()


if __name__ == '__main__':
    main()
