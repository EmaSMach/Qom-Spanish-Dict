from tkinter import END
import gc

from pubsub import pub

from views import MainWindow
from models import Word
from db import session
from forms import WordForm


class Controller:
    def __init__(self, model, view, *args, **kwargs):
        self.model = model
        self.view = view()
        pub.subscribe(self.search, "btn_search_clicked")
        pub.subscribe(self.update_table, "key_released")
        pub.subscribe(self.update_table, "letter_inserted")
        pub.subscribe(self.show_word_details, "item_dclicked")
        self.show_all()

    def show_all(self):
        self.view.clear_table()
        objs = session.query(self.model).all()
        for obj in objs:
            elements = [el if el else '' for el in obj.to_list()]
            self.view.table.insert(index=END, parent='', values=elements)

    def run(self):
        self.view.show()

    def search(self, data):
        objs = session.query(self.model).filter(self.model.qom.like(f"{data}%")).limit(100)
        self.view.update_table([el if el else '' for el in obj.to_list()] for obj in objs)
        # TODO add pagination

    def update_table(self, data):
        if data:
            self.search(data)
        else:
            self.show_all()

    def show_word_details(self, word_id):
        word = session.query(self.model).filter_by(id=word_id).first()
        form = WordForm(word=word)
        gc.collect()


def main():
    controller = Controller(Word, MainWindow)
    controller.run()


if __name__ == '__main__':
    main()
