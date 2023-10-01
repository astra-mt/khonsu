# Docs: https://doc.qt.io/qtforpython-6/PySide6/QtMultimediaWidgets/QVideoWidget.html

from PySide6.QtCore import (Qt, QEvent, QObject, QUrl)
from PySide6.QtMultimedia import QMediaPlayer
from PySide6.QtWidgets import (
    QApplication, QLabel, QMainWindow, QPushButton, QVBoxLayout, QWidget)
from PySide6.QtMultimediaWidgets import QVideoWidget

import sys


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        widget = QWidget()
        self.setCentralWidget(widget)
        layout = QVBoxLayout(widget)

        player = QMediaPlayer()
        player.setSource(QUrl("http://192.168.1.18:81/stream"))

        videoWidget = QVideoWidget()
        player.setVideoOutput(videoWidget)

        videoWidget.show()
        player.play()

        self.text = QLabel("The answer is 42.")
        layout.addWidget(self.text, alignment=Qt.AlignmentFlag.AlignCenter)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()

    main_window.show()

    app.exec()
