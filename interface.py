import sys

from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtCore import QTimer
from PyQt6 import uic

from core import HobbyKit


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        uic.loadUi("interface.ui", self)
        self.setWindowIcon(QIcon('./icon.ico'))

        # Получаем данные рулетки
        self.kit = HobbyKit()

        # Создаём таймер для перелистываний
        self.timer = QTimer()
        self.timer.timeout.connect(self.roll_interface)
        self.count = 0

        # Вшитые хобби
        self.kit.add_hobby('Читать книгу')
        self.kit.add_hobby('Писать код')
        self.kit.add_hobby('Создавать посты для канала')
        self.kit.add_hobby('Смотреть фильм')
        self.kit.add_hobby('Играть в шахматы')
        self.kit.add_hobby('Заняться спортом')

        # Привязка кнопок
        self.roll_btn.clicked.connect(self.roll_interface)
        self.del_btn.clicked.connect(self.click_delete_hobby)
        self.add_btn.clicked.connect(self.click_add_hobby)

        self.draw_settings()

    def click_add_hobby(self):
        add_hobby_text = self.new_hobby.text().strip()
        if len(add_hobby_text) > 0 and add_hobby_text not in self.kit.hobby:
            self.kit.add_hobby(new_hobby=add_hobby_text)
            self.hobby_list.addItem(add_hobby_text)


    def click_delete_hobby(self):
        delete_elem = self.hobby_list.currentItem()
        text_delete_elem = delete_elem.text()
        index_delete = self.kit.hobby.index(text_delete_elem)
        if index_delete > -1:
            self.hobby_list.takeItem(index_delete)
            self.kit.delete_hobby(del_hobby=text_delete_elem)

    # Функция рандомной прокрутки
    def roll_interface(self):
        self.timer.start(100)
        self.roll_text.setStyleSheet('color: black;')
        if self.count <= 30:
            rand_elem = self.kit.get_random_hobby()
            self.roll_text.setText(rand_elem)
            self.count += 1
        else:
            self.roll_text.setStyleSheet('color: green;')
            self.timer.stop()
            self.count = 0

    def draw_settings(self):
        for item in self.kit.hobby:
            self.hobby_list.addItem(item)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
