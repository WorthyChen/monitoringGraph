import numpy as np
import pylab as pl
import pylab as pl


if __name__ == '__main__':

    data1 = np.loadtxt("data1.txt")
    data2 = np.loadtxt("data2.txt")
    data3 = np.loadtxt("data3.txt")
    data4 = np.loadtxt("data4.txt")
    data5 = np.loadtxt("data5.txt")
    data6 = np.loadtxt("data6.txt")
    data7 = np.loadtxt("data7.txt")
    data8 = np.loadtxt("data8.txt")
    data9 = np.loadtxt("data9.txt")
    data10 = np.loadtxt("data10.txt")
    data11 = np.loadtxt("data11.txt")
    data12 = np.loadtxt("data12.txt")

    y1 = data1[0, :]
    x1 = data1[1, :]
    y2 = data2[0, :]
    x2 = data2[1, :]
    y3 = data3[0, :]
    x3 = data3[1, :]
    y4 = data4[0, :]
    x4 = data4[1, :]
    y5 = data5[0, :]
    x5 = data5[1, :]
    y6 = data6[0, :]
    x6 = data6[1, :]
    y7 = data7[0, :]
    x7 = data7[1, :]
    y8 = data8[0, :]
    x8 = data8[1, :]
    y9 = data9[0, :]
    x9 = data9[1, :]
    y10 = data10[0, :]
    x10 = data10[1, :]
    y11 = data11[0, :]
    x11 = data11[1, :]
    y12 = data12[0, :]
    x12 = data12[1, :]


    fig = pl.figure(figsize=(10, 8))

    ax1 = fig.add_subplot(12, 1, 1)
    pl.plot(x1, y1, '#1F76B3')
    pl.xlim(-50, 5800)

    ax2 = fig.add_subplot(12, 1, 2)
    pl.plot(x2, y2, '#1F76B3')
    pl.xlim(-50, 5800)

    ax3 = fig.add_subplot(12, 1, 3)
    pl.plot(x3, y3, '#1F76B3')
    pl.xlim(-50, 5800)

    ax4 = fig.add_subplot(12, 1, 4)
    pl.plot(x4, y4, '#1F76B3')
    pl.xlim(-50, 5800)

    ax5 = fig.add_subplot(12, 1, 5)
    pl.plot(x5, y5, '#1F76B3')
    pl.xlim(-50, 5800)

    ax6 = fig.add_subplot(12, 1, 6)
    pl.plot(x6, y6, '#1F76B3')
    pl.xlim(-50, 5800)

    ax7 = fig.add_subplot(12, 1, 7)
    pl.plot(x7, y7, '#1F76B3')
    pl.xlim(-50, 5800)

    ax8 = fig.add_subplot(12, 1, 8)
    pl.plot(x8, y8, '#1F76B3')
    pl.xlim(-50, 5800)

    ax9 = fig.add_subplot(12, 1, 9)
    pl.plot(x9, y9, '#1F76B3')
    pl.xlim(-50, 5800)

    ax10 = fig.add_subplot(12, 1, 10)
    pl.plot(x10, y10, '#1F76B3')
    pl.xlim(-50, 5800)

    ax11 = fig.add_subplot(12, 1, 11)
    pl.plot(x11, y11, '#1F76B3')
    pl.xlim(-50, 5800)

    ax12 = fig.add_subplot(12, 1, 12)
    pl.plot(x12, y12, '#1F76B3')
    pl.xlim(-50, 5800)





    pl.show()
