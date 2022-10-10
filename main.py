import sys
import PySide2
import os
from PySide2.QtWidgets import QApplication, QWidget, QMainWindow
from windows import about, admire, mainwindow

dirname = os.path.dirname(PySide2.__file__)
plugin_path = os.path.join(dirname, 'plugins', 'platforms')
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path


# if __name__ == '__main__':
#     app = QApplication(sys.argv)
#     MainWindow = QMainWindow()
#     # ui = admire.Ui_MainWindow()  # 开启 admire 赞助页面
#     # ui = about.Ui_MainWindow()  # 开启 about 关于页面
#     ui = mainwindow.Ui_MainWindow()  # 开启 mainwindow 主页面
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())

# 主页面
class Mainwindow(QMainWindow):
    def __init__(self, parent=None):
        super(Mainwindow, self).__init__(parent)
        self.ui = mainwindow.Ui_MainWindow()
        self.ui.setupUi(self)

    def clicked1(self):
        win2.show()

    def clicked2(self):
        win3.show()


# 关于页面
class aboutWindow(QMainWindow):
    def __init__(self, parent=None):
        super(aboutWindow, self).__init__(parent)
        self.ui = about.Ui_MainWindow()
        self.ui.setupUi(self)


# 赞赏页面
class admireWindow(QMainWindow):
    def __init__(self, parent=None):
        super(admireWindow, self).__init__(parent)
        self.ui = admire.Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Mainwindow()
    win.show()
    win2 = aboutWindow()

    win.ui.action.triggered.connect(win.clicked1)
    win.ui.action_3.triggered.connect(win.clicked2)
    win3 = admireWindow()
    sys.exit(app.exec_())
