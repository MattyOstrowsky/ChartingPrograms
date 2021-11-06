import numpy as np
import matplotlib.pyplot as plt
import sys
from scipy import stats
from main import *
import os.path


class FirstApp(Ui_MainWindow):
    def __init__(self, window):
        self.setupUi(window)
        self.pushButton.clicked.connect(self.clickme)

    def clickme(self):
        if os.path.exists(self.lineEdit.text()):
            text = np.loadtxt(self.lineEdit.text())
            plt.title(self.lineEdit_4.text())
            plt.xlabel(r"" + self.lineEdit_2.text())
            plt.ylabel(r"" + self.lineEdit_3.text())
            plt.plot(text[:, [0]], text[:, [1]], self.comboBox.currentText())

            if self.checkBox.isChecked():
                y1 = text[:, [0]].transpose()
                x1 = text[:, [1]].transpose()
                x = np.loadtxt(self.lineEdit.text(), usecols=[0])
                y = np.loadtxt(self.lineEdit.text(), usecols=[1])
                z = np.polyfit(x, y, 1)
                p = np.poly1d(z)
                plt.plot(x, p(x), "r-")
                slope, intercept, r_value, p_value, st = stats.linregress(x1[0], y1[0])
            # plt.plot(x1[0], intercept + slope * x1[0], self.comboBox_2.currentText())
            if self.checkBox_3.isChecked():
                decimal = "y=%." + str(self.spinBox.value()) + "fx+%." + str(self.spinBox.value()) + "f"
                std = "u(a)=" + str(st)
                print(decimal % (z[0], z[1]), std)
                plt.text(self.doubleSpinBox_2.value(), self.doubleSpinBox.value(), decimal % (z[0], z[1]), ha='center')
                plt.text(self.doubleSpinBox_2.value(), self.doubleSpinBox.value() + 4, std, ha='center')
            if self.checkBox_2.isChecked():
                plt.grid(True)

            plt.show()


app = QtWidgets.QApplication(sys.argv)
MainWindow = QtWidgets.QMainWindow()
ui = FirstApp(MainWindow)
MainWindow.show()
app.exec_()
