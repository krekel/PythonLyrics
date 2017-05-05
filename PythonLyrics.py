#! /usr/bin/env python3
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout, QScrollArea
from PyQt5.QtCore import QTimer
import sys
from Lyrics import Lyrics


class PythonLyrics(QWidget):

    def __init__(self):
        super().__init__()

        self.lyrics = Lyrics()
        self.label = QLabel(self)

        self.init_ui()

    def init_ui(self):

        self.setGeometry(300, 300, 500, 700)
        self.setWindowTitle('PythonLyrics')
        self.setFixedSize(500, 700)

        self.label.setText(self.lyrics.get_lyrics())
        self.label.setOpenExternalLinks(True)

        scrollbar = QScrollArea()
        scrollbar.setWidget(self.label)

        hbox = QVBoxLayout()
        hbox.addWidget(scrollbar)

        self.setLayout(hbox)
        self.show()

    def set_display_message(self, message):
        self.label.setText(message)

    def refresh(self):
        if self.lyrics.update():
            self.label.setText(self.lyrics.get_lyrics())
            self.label.setOpenExternalLinks(True)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    l = PythonLyrics()
    timer = QTimer()
    timer.timeout.connect(l.refresh)
    timer.start(5000)
    sys.exit(app.exec_())
