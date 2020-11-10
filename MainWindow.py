import sys
from PySide2.QtWidgets import QApplication, QWidget, QTreeWidget, QHBoxLayout, QVBoxLayout, QTableWidget, QTreeWidgetItem, QTableWidgetItem

from categories import Categories #Содержит словарь для заполнения дерева

from PySide2.QtCore import QObject, Signal


class Communicate(QObject):
    update_table = Signal(str)
    update_main_table = Signal(str)

class DataTable(QTableWidget):
    def __init__(self):
        super().__init__()
        self.initTable()

    def initTable(self):
        self.setColumnCount(1)
        self.setRowCount(1)
        self.setItem(0, 0, QTableWidgetItem('<---'))

    def update_table(self, item):
        table = Categories().tables
        stylesheet = "::section{Background-color:rgb(176,224,230);border-radius:2px;}"
        self.setColumnCount(len(table[item][0]))
        self.setRowCount(len(table[item]) - 1)
        for i in range(len(table[item])):
            for j in range(len(table[item][i])):
                if i == 0:
                    self.setHorizontalHeaderItem(j,QTableWidgetItem(table[item][i][j]))
                    continue
                self.setItem(i-1, j, QTableWidgetItem(table[item][i][j]))
        self.horizontalHeader().setStyleSheet(stylesheet)
        self.resizeColumnsToContents()

class MainTable(QTableWidget):
    def __init__(self):
        super().__init__()
        self.initTable()

    def initTable(self):
        self.header = ['Составляющие затрат',
                       'Номер расценки',
                       'Единица измерения',
                       'Базовая величина затрат, тыс.руб./ед.изм.',
                       'Количество ед.',
                       'Коэффициент приведения затрат к уровню цен субъекта',
                       'Базовые затраты в уровнях цен субъекта РФ, тыс.руб.',
                       'Текущие затраты в уровнях цен субъекта РФ, тыс.руб.']
        self.row_position = 0
        self.setColumnCount(8)
        self.setRowCount(1)
        for i in range(0, len(self.header)):
            self.setHorizontalHeaderItem(i, QTableWidgetItem(self.header[i]))
        stylesheet = "::section{Background-color:rgb(176,224,230);border-radius:2px;}"
        self.horizontalHeader().setStyleSheet(stylesheet)
        self.resizeColumnsToContents()

    def update_table(self, item):
        self.setItem(self.row_position, 3, QTableWidgetItem(item))
        self.row_position += 1
        self.insertRow(self.row_position)



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
        self.c2 = Communicate()
        self.wid = DataTable()
        self.table = MainTable()
        self.c2.update_main_table.connect(self.table.update_table)
        self.c.update_table.connect(self.wid.update_table)
        tree.itemClicked.connect(self.onItemClicked)
        self.wid.itemClicked.connect(self.onTableItemClicked)

        hbox.addWidget(tree)
        hbox.addWidget(self.wid)

        vbox.addLayout(hbox)
        vbox.addWidget(self.table)
        treeItems() #Заполнить дерево

        self.show()


    def onItemClicked(self, it, col):
        item = it.text(col)
        self.c.update_table.emit(item)

    def onTableItemClicked(self, item):
        self.c2.update_main_table.emit(item.text())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    categories = Categories()

    ex = Window()
    sys.exit(app.exec_())
