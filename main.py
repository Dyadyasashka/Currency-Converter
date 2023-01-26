import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QIcon
from ui import Ui_MainWindow  # импорт графического интерфейса
from currency_converter import CurrencyConverter  # импорт библиотеки конвертера

class CurrencyConv(QtWidgets.QMainWindow):

    def __init__(self):
        super(CurrencyConv, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self) # отрисовка
        self.init_UI()

    def init_UI(self):
        self.setWindowTitle('Конвертер валют') # заголовок окна
        self.setWindowIcon(QIcon('currency_exchange_icon-icons.com_54433.png')) # иконка окна
        self.ui.input_currency.setPlaceholderText('Что меняем ?')  # setPlaceholderText - метод для подсказки куда записывать данные пользователю
        self.ui.input_amount.setPlaceholderText('Сколько у вас есть?')
        self.ui.output_currency.setPlaceholderText('На что меняем?')
        self.ui.output_amount.setPlaceholderText('Вы получите')
        self.ui.pushButton.clicked.connect(self.converter) # связка конвертера с вызовом по нажатию кнопки

    def converter(self):
        c = CurrencyConverter()
        input_currency = self.ui.input_currency.text()  # .text-метод для хранения вводиммых данных в str
        output_currency = self.ui.output_currency.text()
        input_amount = int(self.ui.input_amount.text())

        output_amount = round(c.convert(input_amount, '%s' % (input_currency), '%s' % (output_currency)), 2)

        self.ui.output_amount.setText(str(output_amount))  # .setText - метод для отображения результата в поле

app = QtWidgets.QApplication([])
application = CurrencyConv()
application.show() # отображение графического интерфейса

sys.exit(app.exec())
