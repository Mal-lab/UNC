import sys
import math
from PySide2.QtWidgets import QApplication, QWidget, QTreeWidget, QHBoxLayout, QVBoxLayout, QTableWidget, QTreeWidgetItem, QTableWidgetItem, QPushButton, QDialog

from categories import Categories #Содержит словарь для заполнения дерева
from PySide2.QtGui import QColor, QFont
from PySide2.QtCore import QObject, Signal, QPoint


class Communicate(QObject):
    update_table = Signal(str)
    update_main_table = Signal(list)
    recalculation = Signal(list)

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
        #Формирование базовой таблицы
        self.header = ['Состовляющие затрат',
                       'Номер расценки',
                       'Единица измерения',
                       'Базовая величина затрат, тыс.руб./ед.изм.',
                       'Количество ед.',
                       'Коэффициент приведения затрат к уровню цен субъекта',
                       'Базовые затраты в уровнях цен субъекта РФ, тыс.руб.',
                       'Текущие затраты в уровне цен субъекта РФ, тыс.руб.',
                       'Del']
        self.setColumnCount(9)
        self.setRowCount(1)
        for i in range(0, len(self.header)):
            self.setHorizontalHeaderItem(i, QTableWidgetItem(self.header[i]))
        stylesheet = "::section{Background-color:rgb(176,224,230);border-radius:2px;}"
        self.horizontalHeader().setStyleSheet(stylesheet)
        self.resizeColumnsToContents()

        #Формирование сигналов
        self.cellClicked.connect(self.deleteClicked)

    #Добавление строк по клику
    def update_table(self, items):
        self.make_closebutton()
        text = self.make_numbertext(items)
        self.row = self.rowCount() - 1
        self.setItem(self.row, 3, QTableWidgetItem(items[0]))
        self.setItem(self.row, 4, QTableWidgetItem(items[3]))
        self.setItem(self.row, 5, QTableWidgetItem(items[4])) #Добавить критерии выбора региональных коэффициентов
        self.setItem(self.row, 6, QTableWidgetItem(self.calculate(items)[0]))
        self.setItem(self.row, 7, QTableWidgetItem(self.calculate(items)[1]))
        self.setItem(self.row, 1, QTableWidgetItem(text))
        self.setItem(self.row, 8, self.closebut)
        self.insertRow(self.row + 1)

    #Пересчет при изменении значений
    def recalculation(self, data):
        for i in range(len(data[0])):
            cost = float(data[0][i])
            count = float(data[1][i])
            koef = float(data[2][i])
            calc = str(round(cost*count*koef,1))
            self.setItem(i, 6, QTableWidgetItem(calc.replace('.', ',')))
            self.setItem(i, 7, QTableWidgetItem(str(round(float(calc)*1.2, 1)).replace('.', ',')))

    #Удаление строки
    def deleteClicked(self, row, col):
        if col == 8:
            self.removeRow(row)
            self.row += 1

    #Текст для категории
    def make_numbertext(self, items):
        if len(items[2]) > 5:
            return items[2][:5] + '-' + items[1]
        else:
            return items[2]

    #Расчет стоимости
    def calculate(self, items):
        cost = float(items[0].replace(',', '.'))
        count = float(items[3].replace(',', '.'))
        k = float(items[4].replace(',', '.'))
        current_cost = str(round(cost*count*k,1))
        future_cost = str(round(float(current_cost)*1.2))
        return [current_cost.replace('.', ','), future_cost.replace('.', ',')]

    #Рисует крестик для удаления строки
    def make_closebutton(self):
        self.closebut = QTableWidgetItem('X')
        self.closebut.setBackgroundColor(QColor(240, 240, 240))
        self.closebut.setFont(QFont('Helvetica [Cronyx]', 18, QFont.ExtraBold))
        self.closebut.setTextColor(QColor(255, 11, 21))
        self.closebut.setTextAlignment(4)


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        #Заполнение дерева
        def treeItems():
            categories = Categories().data
            for key in categories:
                parent = QTreeWidgetItem(tree)
                parent.setText(0, key)
                for item in categories[key]:
                    child = QTreeWidgetItem(parent)
                    child.setText(0, item)

        #Базовое окно
        self.setGeometry(0, 0, 1900, 1000)
        self.setWindowTitle('УНЦ ПБЭ')

        #Инициализация дерева
        tree = QTreeWidget(self)
        tree.setHeaderHidden(True)

        #Инициализация объектов
        self.c = Communicate()
        self.c2 = Communicate()
        self.c3 = Communicate()
        self.wid = DataTable()
        self.table = MainTable()

        #Создание кнопок
        font_button = QFont('Helvetica [Cronyx]', 12, QFont.Bold)
        export_button = QPushButton('Экспорт в Excel')
        total_button = QPushButton('Сформировать "Итого"')
        export_button.setFont(font_button)
        total_button.setFont(font_button)


        #Формирование сигналов
        self.c.update_table.connect(self.wid.update_table)
        self.c2.update_main_table.connect(self.table.update_table)
        self.c3.recalculation.connect(self.table.recalculation)

        tree.itemClicked.connect(self.onItemClicked)
        self.wid.cellClicked.connect(self.onTableItemClicked)
        self.table.cellClicked.connect(self.recalc)
        export_button.clicked.connect(self.export_excel)
        export_button.setToolTip('Coming soon!')

        #Ининциализация слоев
        vbox = QVBoxLayout(self)
        hbox = QHBoxLayout(self)
        #Слой для кнопок
        buttons_layer = QHBoxLayout(self)
        button_hbox = QHBoxLayout(self)
        button_hbox.addStretch(1)
        button_hbox.addWidget(export_button)
        button_hbox.addWidget(total_button)
        button_vbox = QVBoxLayout(self)
        button_vbox.addStretch(1)
        button_vbox.addLayout(button_hbox)
        buttons_layer.addLayout(button_vbox)
        #Заполнение слоев
        hbox.addWidget(tree)
        hbox.addWidget(self.wid)

        vbox.addLayout(hbox)
        vbox.addWidget(self.table)
        vbox.addLayout(buttons_layer)


        treeItems() #Заполнить дерево

        self.show()

    #Экспорт таблицы в Excel
    def export_excel(self):
        pass

    #Обработка клика по элементу дерева
    def onItemClicked(self, it, col):
        item = it.text(col)
        self.c.update_table.emit(item)

    #Обработка клика по элементу таблицы
    def onTableItemClicked(self, row, col):
        items = [self.wid.item(row, col).text(), #Значение
                 self.wid.item(0, col).text(),   #Категория
                 self.wid.item(row, 0).text(),   #Номер расценки
                 '1',                            #Количество
                 '1,1']                          #Коэффициент
        self.c2.update_main_table.emit(items)

    #Пересчет таблице при изменении значений
    def recalc(self, row, col):
        rows = self.table.rowCount()
        cost = []
        count = []
        koef = []
        for i in range(0, rows-1):
            cost.append(self.table.item(i, 3).text().replace(',', '.'))
            count.append(self.table.item(i, 4).text().replace(',', '.'))
            koef.append(self.table.item(i, 5).text().replace(',', '.'))
        self.c3.recalculation.emit([cost, count, koef])

if __name__ == '__main__':
    app = QApplication(sys.argv)
    categories = Categories()

    ex = Window()
    sys.exit(app.exec_())
