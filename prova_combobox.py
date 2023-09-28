import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QComboBox, QLabel, QPushButton, QToolBox


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Widget a comparsa con QToolBox")
        self.setGeometry(100, 100, 400, 200)

        # Creiamo un QComboBox per il menu a tendina
        self.comboBox = QComboBox(self)
        self.comboBox.setGeometry(50, 50, 300, 30)
        self.comboBox.addItem("Elemento 1")
        self.comboBox.addItem("Elemento 2")
        self.comboBox.addItem("Elemento 3")

        # Creiamo un QToolBox per visualizzare i widget a comparsa
        self.toolBox = QToolBox(self)
        self.toolBox.setGeometry(50, 80, 300, 100)

        # Aggiungiamo widget a comparsa al QToolBox
        widget1 = QLabel("Widget per Elemento 1", self)
        widget2 = QLabel("Widget per Elemento 2", self)
        widget3 = QLabel("Widget per Elemento 3", self)
        self.toolBox.addItem(widget1, "Elemento 1")
        self.toolBox.addItem(widget2, "Elemento 2")
        self.toolBox.addItem(widget3, "Elemento 3")

        # Collega il menu a tendina al QToolBox
        self.comboBox.currentIndexChanged.connect(self.showSelectedWidget)

    def showSelectedWidget(self):
        index = self.comboBox.currentIndex()
        self.toolBox.setCurrentIndex(index)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
