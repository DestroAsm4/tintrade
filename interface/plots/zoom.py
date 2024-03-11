from matplotlib.pyplot import figure, show
import numpy

class ZoomPan:
    def __init__(self):
        self.press = None
        self.cur_xlim = None
        self.cur_ylim = None
        self.x0 = None
        self.y0 = None
        self.x1 = None
        self.y1 = None
        self.xpress = None
        self.ypress = None


    def zoom_factory(self, ax, base_scale = 2.):
        def zoom(event):
            cur_xlim = ax.get_xlim()
            cur_ylim = ax.get_ylim()

            xdata = event.xdata # get event x location
            ydata = event.ydata # get event y location

            if event.button == 'down':
                # deal with zoom in
                scale_factor = 1 / base_scale
            elif event.button == 'up':
                # deal with zoom out
                scale_factor = base_scale
            else:
                # deal with something that should never happen
                scale_factor = 1
                event.button


            # стандартная формула масштабирования

            new_width = (cur_xlim[1] - cur_xlim[0]) * scale_factor
            new_height = (cur_ylim[1] - cur_ylim[0]) * scale_factor

            print(new_width)

            # if new_width >= 0:
            #     new_width = 0
            # if new_height >= 0:
            #     new_height = 0

            # каректировка под местоположение мыши
            relx = (cur_xlim[1] - xdata)/(cur_xlim[1] - cur_xlim[0])
            rely = (cur_ylim[1] - ydata)/(cur_ylim[1] - cur_ylim[0])

            # if relx <= 0:
            #     relx = 0
            # if rely <= 0:
            #     rely = 0
            # конечная установка машсштаба

            x1 = xdata - new_width * (1-relx)
            if x1 < 0:
                x1 = 0

            x2 = xdata + new_width * (relx)
            # if x2 < 1:
            #     x2 = 1

            y1 = ydata - new_height * (1-rely)

            if y1 < 0:
                y1 = 0

            y2 = ydata + new_height * (rely)

            # if y2 < 1:
            #     y2 = 1

            ax.set_xlim([x1, x2])
            ax.set_ylim([y1, y2])
            ax.figure.canvas.draw()

        fig = ax.get_figure() # get the figure of interest
        fig.canvas.mpl_connect('scroll_event', zoom)

        return zoom

    def pan_factory(self, ax):
        def onPress(event):
            if event.inaxes != ax: return
            self.cur_xlim = ax.get_xlim()
            self.cur_ylim = ax.get_ylim()
            self.press = self.x0, self.y0, event.xdata, event.ydata
            self.x0, self.y0, self.xpress, self.ypress = self.press

        def onRelease(event):
            self.press = None
            ax.figure.canvas.draw()

        def onMotion(event):
            if self.press is None: return
            if event.inaxes != ax: return
            dx = event.xdata - self.xpress
            dy = event.ydata - self.ypress
            self.cur_xlim -= dx
            self.cur_ylim -= dy

            # определяет то как будет двигаться в тороны, cur_xlim - это список
            if self.cur_xlim[0] < 0:
                self.cur_xlim[0] = 0
            if self.cur_ylim[0] < 0:
                self.cur_ylim[0] = 0
            ax.set_xlim(self.cur_xlim)
            ax.set_ylim(self.cur_ylim)

            ax.figure.canvas.draw()

        fig = ax.get_figure() # get the figure of interest

        # attach the call back
        fig.canvas.mpl_connect('button_press_event',onPress)
        fig.canvas.mpl_connect('button_release_event',onRelease)
        fig.canvas.mpl_connect('motion_notify_event',onMotion)

        #return the function
        return onMotion


# fig = figure()
# ax = fig.add_subplot(111, xlim=(0,1), ylim=(0,1), autoscale_on=False)
# scale = 1.1
# zp = ZoomPan()
# figZoom = zp.zoom_factory(ax, base_scale = scale)
# figPan = zp.pan_factory(ax)
# show()