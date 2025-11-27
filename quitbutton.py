from PyQt5 import QtWidgets, QtCore
import sys

class QuitButton(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(QuitButton, self).__init__(parent)
        self.setGeometry(100, 200, 800, 650) #linke erste ecke -> länge und breite
        self.setWindowTitle("QuitButton")
        self.quit = QtWidgets.QPushButton("Quit", self)
        self.quit.setGeometry(200, 100, 300, 50)
        self.quit.clicked.connect(self.close)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    button = QuitButton()
    button.show()
    sys.exit(app.exec_())