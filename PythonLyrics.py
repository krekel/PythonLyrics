#! /usr/bin/env python3
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QVBoxLayout, QTextEdit
from PyQt5.QtCore import QTimer
import sys
from Lyrics import Lyrics


class PythonLyrics(QWidget):

    def __init__(self):

        super(PythonLyrics, self).__init__()
        self.lyrics = Lyrics()
        self.init_ui()

    def init_ui(self):

        self.text = QTextEdit(self)
        # self.text.setFixedSize(480, 700)
        self.text.setText(self.lyrics.get_lyrics())
        self.text.setLineWrapMode(QTextEdit.NoWrap)
        self.text.setReadOnly(True)

        self.info = QLabel(self)
        self.info.setText(self.lyrics.get_artist() + ' ' + self.lyrics.get_song())

        vbox = QVBoxLayout()
        vbox.addWidget(self.info)
        vbox.addWidget(self.text)

        self.setWindowTitle('PythonLyrics')
        self.setGeometry(700, 200, 605, 700)

        self.setLayout(vbox)

        self.show()

    def refresh(self):
        if self.lyrics.update():
            self.text.clear()
            self.text.setText(self.lyrics.get_lyrics())
            self.info.clear()
            self.info.setText(self.lyrics.get_artist() + ' ' + self.lyrics.get_song())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    l = PythonLyrics()
    timer = QTimer()
    timer.timeout.connect(l.refresh)
    timer.start(5000)
    sys.exit(app.exec_())
