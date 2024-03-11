
from PyQt6 import QtWidgets, QtCore

import pyqtgraph as pg

from zoom import ZoomPan

from SETTING import TOKEN
from Tools import singl_usd_ru



from matplotlib.pyplot import figure, show
import numpy

class MainWindow(QtWidgets.QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)


        #----setting main window----
        self.setFixedSize(1500, 500)
        self.first_value = singl_usd_ru(TOKEN)

        #------create object---------

        self.graphWidget = pg.PlotWidget()


        #-------placement of objects---------
        self.setCentralWidget(self.graphWidget)



        #-----setting plot-----
        self.x = [self.first_value, self.first_value]
        self.y = [self.first_value, self.first_value]

        # self.graphWidget.setBackground('w')
        self.graphWidget.setTitle('Graph', color='b', size='30pt')

        pen = pg.mkPen(color=(255, 0, 0))
        self.data_line = self.graphWidget.plot(self.x, self.y, pen=pen, symbol='+')


        #------- renewal period-----

        self.timer = QtCore.QTimer()
        self.timer.setInterval(5000)

        # self.value = singl_usd_ru()
        # self.min_max_x = [self.value - 1, self.value + 1]
        # self.min_max_y = [self.value - 1, self.value + 1]
        #
        # self.graphWidget.setXRange(self.min_max_x[0], self.min_max_x[1], padding=0)
        # self.graphWidget.setYRange(self.min_max_y[0], self.min_max_y[1], padding=0)

        self.timer.timeout.connect(self.update_plot_data)
        self.timer.start()

    def update_plot_data(self):


        # self.x = self.x[1:]  # Remove the first y element.
        self.x.append(self.x[-1] + 1)  # Add a new value 1 higher than the last.


        # update of y value

        # self.y = self.y[1:]  # Remove the first
        self.y.append(singl_usd_ru(TOKEN))  # Add a new random value.

        self.data_line.setData(self.x, self.y)  # Update the data.


fig = figure()
ax = fig.add_subplot(111, xlim=(0,1), ylim=(0,1), autoscale_on=False)
scale = 1.1
zp = ZoomPan()
figZoom = zp.zoom_factory(ax, base_scale = scale)
figPan = zp.pan_factory(ax)
show()