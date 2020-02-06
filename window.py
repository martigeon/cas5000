# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'window.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_main(object):
    def setupUi(self, main):
        main.setObjectName("main")
        main.resize(432, 622)
        self.answer_box = QtWidgets.QLineEdit(main)
        self.answer_box.setGeometry(QtCore.QRect(10, 90, 291, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.answer_box.setFont(font)
        self.answer_box.setText("")
        self.answer_box.setObjectName("answer_box")
        self.prev_button = QtWidgets.QPushButton(main)
        self.prev_button.setGeometry(QtCore.QRect(310, 90, 31, 31))
        self.prev_button.setObjectName("prev_button")
        self.next_button = QtWidgets.QPushButton(main)
        self.next_button.setGeometry(QtCore.QRect(350, 90, 31, 31))
        self.next_button.setObjectName("next_button")
        self.english_label = QtWidgets.QLabel(main)
        self.english_label.setGeometry(QtCore.QRect(10, 50, 411, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.english_label.setFont(font)
        self.english_label.setText("")
        self.english_label.setObjectName("english_label")
        self.word_lists = QtWidgets.QComboBox(main)
        self.word_lists.setGeometry(QtCore.QRect(10, 10, 291, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.word_lists.setFont(font)
        self.word_lists.setObjectName("word_lists")
        self.word_count = QtWidgets.QLabel(main)
        self.word_count.setGeometry(QtCore.QRect(310, 10, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.word_count.setFont(font)
        self.word_count.setText("")
        self.word_count.setAlignment(QtCore.Qt.AlignCenter)
        self.word_count.setObjectName("word_count")
        self.restart = QtWidgets.QPushButton(main)
        self.restart.setGeometry(QtCore.QRect(390, 90, 31, 31))
        self.restart.setObjectName("restart")
        self.word_table = QtWidgets.QTableWidget(main)
        self.word_table.setGeometry(QtCore.QRect(10, 130, 411, 481))
        self.word_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.word_table.setRowCount(100)
        self.word_table.setColumnCount(2)
        self.word_table.setObjectName("word_table")
        item = QtWidgets.QTableWidgetItem()
        self.word_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.word_table.setHorizontalHeaderItem(1, item)
        self.word_table.horizontalHeader().setVisible(True)
        self.word_table.horizontalHeader().setDefaultSectionSize(180)
        self.word_table.horizontalHeader().setHighlightSections(True)

        self.retranslateUi(main)
        QtCore.QMetaObject.connectSlotsByName(main)

    def retranslateUi(self, main):
        _translate = QtCore.QCoreApplication.translate
        main.setWindowTitle(_translate("main", "CAS 5000"))
        self.prev_button.setText(_translate("main", "<"))
        self.prev_button.setShortcut(_translate("main", "Up"))
        self.next_button.setText(_translate("main", ">"))
        self.next_button.setShortcut(_translate("main", "Return"))
        self.restart.setText(_translate("main", "C"))
        self.restart.setShortcut(_translate("main", "F1"))
        item = self.word_table.horizontalHeaderItem(0)
        item.setText(_translate("main", "English"))
        item = self.word_table.horizontalHeaderItem(1)
        item.setText(_translate("main", "Spanish"))

