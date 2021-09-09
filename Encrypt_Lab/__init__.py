from PyQt5.QtWidgets import QMainWindow, QApplication
import Sim

import sys

class Simulator:
    @classmethod
    def run(cls): # open the simulator gui
        app = QApplication(sys.argv)

        m = QMainWindow()
        m.resize(1000, 1000)
        w = Sim.Mod(m)

        m.setCentralWidget(w)
        m.show()

        sys.exit(app.exec_())
    @classmethod

    def statistics(cls, num=10): # statistics analysis
        return Sim.statistics(num)