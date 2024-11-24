import PySide6.QtGui
import PySide6.QtCore
import PySide6.QtWidgets

import api
import ui_mainwindow


class MainWindow(PySide6.QtWidgets.QMainWindow):

    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        self.ui = ui_mainwindow.Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.ActionOpenFile.triggered.connect(self.open_file)
        self.segmentation_api = api.SegmentationAPI()
        self.classification_api = api.ClassificationAPI()

    @PySide6.QtCore.Slot()
    def open_file(self) -> None:
        path = PySide6.QtWidgets.QFileDialog.getOpenFileName(self, "Open File", ".", "PNG File (*.png)")[0]
        with open(path, mode="rb") as file:
            image = file.read()
            mask = self.segmentation_api.fetch_data(image)
            probability = self.classification_api.fetch_data(image)
            self.handle_image(image)
            self.handle_mask(mask)
            self.handle_probability(probability)

    def handle_image(self, image: bytes) -> None:
        pixmap = PySide6.QtGui.QPixmap()
        pixmap.loadFromData(image)
        scene = PySide6.QtWidgets.QGraphicsScene()
        scene.addPixmap(pixmap)
        self.ui.WidgetImage.setScene(scene)
        self.ui.WidgetImage.show()

    def handle_mask(self, mask: bytes) -> None:
        pixmap = PySide6.QtGui.QPixmap()
        pixmap.loadFromData(mask)
        scene = PySide6.QtWidgets.QGraphicsScene()
        scene.addPixmap(pixmap)
        self.ui.WidgetMask.setScene(scene)
        self.ui.WidgetMask.show()

    def handle_probability(self, probability: str) -> None:
        self.ui.WidgetProbability.setText(probability)
