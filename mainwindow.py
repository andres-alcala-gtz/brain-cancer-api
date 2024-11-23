import PySide6.QtWidgets

import ui_mainwindow


class MainWindow(PySide6.QtWidgets.QMainWindow):

    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        self.ui = ui_mainwindow.Ui_MainWindow()
        self.ui.setupUi(self)
