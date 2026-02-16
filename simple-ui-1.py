from PySide6 import QtCore as qtc
from PySide6 import QtGui as qtg
from PySide6 import QtWidgets as qtw
from PySide6.QtCore import QRect

from UI_MainWindow.UI.imageMain import Ui_MainWindow

def crop_center(pixmap, target_w, target_h):
    w = pixmap.width()
    h = pixmap.height()
    x = max(0, (w - target_w) // 2)
    y = max(0, (h - target_h) // 2)
    cw = min(target_w, w)
    ch = min(target_h, h)
    return pixmap.copy(QRect(x, y, cw, ch))


class MainWindow(qtw.QMainWindow, Ui_MainWindow):

    def __init__(self):
        super().__init__()
        self._date = qtc.QDate.currentDate().toString('yyyyMMdd')
        self.setupUi(self)
        self.dateEdit.setDate(qtc.QDate.currentDate())

        self.pb_up.clicked.connect(self.load_up)
        self.pb_down.clicked.connect(self.load_down)
        self.pb_right.clicked.connect(self.load_right)
        self.pb_left.clicked.connect(self.load_left)
        self.pb_exit.clicked.connect(qtc.QCoreApplication.instance().quit)
        self.pb_set_date.clicked.connect(self.set_date)

    @qtc.Slot()
    def set_date(self):
        self._date = self.dateEdit.date().toString('yyyyMMdd')
        print('Setting self._date to', self._date, '')
        self.load_up()

    def image_load_and_show(self, icount):
#        self.message_label.setText(f"Loading image {icount}")
        pixmap = qtg.QPixmap(f"/Users/george/egoscue/{self._date}/posture_{icount}.jpg")
        if pixmap.isNull():
            print("Could not load image")
            self.statusBar().showMessage(f"Could not load image for date {self._date}")
            return

        pixmap2 = crop_center(pixmap, 751, 1121)
        self.lw_image.setPixmap(pixmap2)

    def load_up(self):
        self.image_load_and_show(0)

    def load_down(self):
        self.image_load_and_show(2)

    def load_right(self):
        self.image_load_and_show(1)

    def load_left(self):
        self.image_load_and_show(3)



if __name__ == "__main__":
    app = qtw.QApplication([])
    window = MainWindow()
    window.show()
    app.exec()



