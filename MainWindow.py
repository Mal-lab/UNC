import sys
from PySide2.QtWidgets import QApplication, QWidget, QTreeWidget, QHBoxLayout, QVBoxLayout, QTableWidget, QTreeWidgetItem, QTableWidgetItem
from categories import Categories #Содержит словарь для заполнения дерева
from PySide2 import QtCore
from PySide2.QtCore import QObject, Signal

class Communicate(QObject):
    update_table = Signal(str)

class DataTable(QTableWidget):
    def __init__(self):
        super().__init__()
        self.initTable()
    def initTable(self):
        self.setColumnCount(1)
        self.setRowCount(1)
        self.setItem(1, 1, QTableWidgetItem('empty'))

    def update_table(self, item):
        table = Categories().tables
        self.setColumnCount(len(table[item][0]))
        self.setRowCount(len(table[item]))
        for i in range(len(table[item])):
            for j in range(len(table[item][i])):
                self.setItem(i, j, QTableWidgetItem(table[item][i][j]))


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        def treeItems(): #Заполнение дерева
            categories = Categories().data
            for key in categories:
                parent = QTreeWidgetItem(tree)
                parent.setText(0, key)
                for item in categories[key]:
                    child = QTreeWidgetItem(parent)
                    child.setText(0, item)
        vbox = QVBoxLayout(self)
        hbox = QHBoxLayout(self)
        tree = QTreeWidget(self)
        tree.setHeaderHidden(True)
        self.setGeometry(300, 300, 1000, 700)
        self.setWindowTitle('УНЦ ПБЭ')
        self.c = Communicate()
        self.wid = DataTable()
        self.c.update_table.connect(self.wid.update_table)
        tree.itemClicked.connect(self.onItemClicked)
        hbox.addWidget(tree)
        hbox.addWidget(self.wid)
        table = QTableWidget(self)
        vbox.addLayout(hbox)
        vbox.addWidget(table)
        treeItems() #Заполнить дерево

        self.show()


    def onItemClicked(self, it, col):
        item = it.text(col)
        self.c.update_table.emit(item)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    categories = Categories()

    ex = Window()
    sys.exit(app.exec_())
