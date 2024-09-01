from PySide6.QtCore import QCoreApplication, Qt
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import (QApplication, QMainWindow, QWidget, QPushButton)
from ui_main import Ui_MainWindow
from app import executar_automacao
import sys

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Teste")
        appIcon = QIcon(U"icon.ico")
        self.setWindowIcon(appIcon)

        # Conecte o botão à função de automação
        self.pushButton.clicked.connect(executar_automacao)

        # # Adicione um botão para executar a automação
        # self.automacao_button = QPushButton(self)
        # self.automacao_button.setGeometry(10, 32, 162, 23)
        # self.automacao_button.clicked.connect(executar_automacao)

if __name__ == "__main__":

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()
    