import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from matplotlib import style

style.use('fivethirtyeight')

fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1)
file = "G:\PyCharm\LiveGraph\LiveGraph\\test_data.txt"


def animate(i):
    data_file = open(file, 'r')
    xs = []
    ys = []
    s_op = slice(3)
    while True:
        data_string = None
        try:
            data_string = data_file.readline()
            print(data_string)
        except Exception as e:
            print(e)
        if len(data_string) > 1:
            x, y = data_string.split(' ')
            x = x[s_op]
            y = y[s_op]
        xs.append(x)
        ys.append(y)
        ax1.clear()
        ax1.plot(xs, ys)
        print(x)
        print(y)


ani = FuncAnimation(fig, animate, interval=1000)
plt.show()

#
# fig, ax = plt.subplots()
# xdata, ydata = [], []
# ln, = plt.plot([], [], 'ro', animated=True)
#
# def init():
#     ax.set_xlim(0, 2*np.pi)
#     ax.set_ylim(-1, 1)
#     return ln,
#
# def update(frame):
#     xdata.append(frame)
#     ydata.append(np.sin(frame))
#     ln.set_data(xdata, ydata)
#     return ln,
#
# ani = FuncAnimation(fig, update, frames=np.linspace(0, 2*np.pi, 128), init_func=init, blit=True)
# plt.show()