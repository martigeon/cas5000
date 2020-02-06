from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import csv
import numpy as np

from window import Ui_main

WORDS_PATH = './words/'
WORDS_FILES = ['L{}.txt'.format(i+1) for i in range(50)]

class Castellano(QMainWindow, Ui_main):
    def __init__(self, *args, **kwargs):
        super(Castellano, self).__init__(*args, **kwargs)
        self.setupUi(self)

        # Variables
        self.dict = {}
        self.i = 0
        self.active = []
        self.word_cache = []

        for f in WORDS_FILES:
            with open(WORDS_PATH + f, 'r') as read_file:
                self.dict[f.replace('.txt', '')] = np.asarray(list(csv.reader(read_file, delimiter='\t')))

        # Widgets
        for d in self.dict:
            self.word_lists.addItem(d)

        # Callbacks
        self.word_lists.activated.connect(self.select_list)
        self.answer_box.textChanged.connect(self.check_answer)
        self.prev_button.clicked.connect(self.prev_word)
        self.next_button.clicked.connect(self.next_word)
        self.restart.clicked.connect(self.reset)

        self.show()
        self.select_list(0)

    def check_answer(self, text):
        if len(self.active) == 0:
            return

        i = self.active[self.i]
        tupl = self.word_cache[i]
        if text == tupl[0]:
            self.answer_box.setText('')
            item = QTableWidgetItem(tupl[0])
            item.setBackground(QColor(200, 255, 200))
            self.word_table.setItem(i, 1, item)

            self.active = np.delete(self.active, self.i)
            if len(self.active) == 0:
                self.word_table.clearSelection()
                total = len(self.word_cache)
                self.word_count.setText('({} / {})'.format(total, total))
                self.english_label.setText('100 %')
                font = self.english_label.font()
                font.setPointSize(20)
                self.english_label.setFont(font)
                self.english_label.setAlignment(Qt.AlignCenter)
                return

            self.i = self.i % len(self.active)
            i = self.active[self.i]
            self.word_table.setCurrentCell(i, 1)
            self.english_label.setText(self.word_cache[i,1])
            total = len(self.word_cache)
            self.word_count.setText('({} / {})'
                .format(total-len(self.active), total))

    def prev_word(self):
        if len(self.active) == 0:
            return

        self.i = (self.i-1) % len(self.active)
        i = self.active[self.i]
        self.word_table.setCurrentCell(i, 1)
        self.english_label.setText(self.word_cache[i,1])
        self.answer_box.setText('')
        self.answer_box.setFocus()

    def next_word(self):
        if len(self.active) == 0:
            return

        self.i = (self.i+1) % len(self.active)
        i = self.active[self.i]
        self.word_table.setCurrentCell(i, 1)
        self.english_label.setText(self.word_cache[i,1])
        self.answer_box.setText('')
        self.answer_box.setFocus()

    def select_list(self, id):
        key = self.word_lists.itemText(id)
        self.word_cache = self.dict[key]
        np.random.shuffle(self.word_cache)

        for i in range(len(self.word_cache)):
            item = QTableWidgetItem(self.word_cache[i,1])
            item.setBackground(QColor(235, 235, 235))
            self.word_table.setItem(i, 0, item)
            self.word_table.setItem(i, 1, QTableWidgetItem(''))

        self.i = 0
        self.active = np.arange(len(self.word_cache))
        
        self.answer_box.setText('')
        self.word_count.setText('(0 / {})'.format(len(self.word_cache)))
        i = self.active[self.i]
        tupl = self.word_cache[i]
        self.word_table.setCurrentCell(i, 1)
        self.english_label.setText(tupl[1])

        font = self.english_label.font()
        font.setPointSize(12)
        self.english_label.setFont(font)
        self.english_label.setAlignment(Qt.AlignLeft|Qt.AlignVCenter)

    def reset(self):
        self.answer_box.setText('')
        if len(self.active) > 0:
            self.word_table.clearSelection()
            percent = 1 - len(self.active)/float(len(self.word_cache))
            self.english_label.setText('{0:.0f} %'.format(percent*100))
            
            font = self.english_label.font()
            font.setPointSize(20)
            self.english_label.setFont(font)
            self.english_label.setAlignment(Qt.AlignCenter)

            for i in self.active:
                item = QTableWidgetItem(self.word_cache[i,0])
                item.setBackground(QColor(255, 200, 200))
                self.word_table.setItem(i, 1, item)
            self.active = []
        else:
            self.select_list(self.word_lists.currentIndex())
            self.answer_box.setFocus()

if __name__ == '__main__':
    app = QApplication([])
    window = Castellano()
    app.exec_()