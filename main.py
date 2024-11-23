import sys
import PySide6.QtWidgets

import mainwindow


if __name__ == "__main__":

    app = PySide6.QtWidgets.QApplication(sys.argv)

    window = mainwindow.MainWindow()
    window.show()

    sys.exit(app.exec())
