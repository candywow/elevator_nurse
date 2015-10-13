import numpy as np
import function
import plotly.plotly as py
from plotly.graph_objs import *
import matplotlib.pyplot as plt


class SAX():

    def __init__(self, w=8, a=7, e=1e-6):
        self.w = w
        self.alphasize = a
        self.epsilon = e
        self.breakpoints = {3: [-0.43, 0.43],
                            4: [-0.67, 0, 0.67],
                            5: [-0.84, -0.25, 0.25, 0.84],
                            6: [-0.97, -0.43, 0, 0.43, 0.97],
                            7: [-1.07, -0.57, -0.18, 0.18, 0.57, 1.07],
                            8: [-1.15, -0.67, -0.32, 0, 0.32, 0.67, 1.15],
                            9: [-1.22, -0.76, -0.43, -0.14, 0.14, 0.43,
                                0.76, 1.22],
                            10: [-1.28, -0.84, -0.52, -0.25, 0, 0.25,
                                 0.52, 0.84, 1.28]
                            }

    def normalize(self, data):
        """normalize each time series to have a mean
        of zero and a standard deviation of one before
        converting it to the PAA representation.
        """
        data_ = np.array(data)
        if np.std(data_) < self.epsilon:
            return np.zeros(len(data_))

        return (data_ - np.average(data_)) / np.std(data_)

    def to_PAA(self, data):
        representation_ = []
        sum_ = 0
        for i in range(len(data) / self.w):
            for j in range(i * self.w, (i + 1) * self.w):
                sum_ = sum_ + data[j]
            average_ = sum_ * 1.0 / self.w
            representation_.append(average_)
            sum_ = 0

        return representation_

    def paint_PAA(self, data_nomalize, data_PAA):
        data_time_1 = []
        data_time_2 = []
        tmp = 0
        for i in range(len(data_PAA)):
            data_time_2.append(tmp)
            for j in range(self.w):
                data_time_1.append(tmp)
                tmp += 1

        # matplotlib paint
        '''plt.plot(data_nomalize, 'g--', data_PAA_, 'b-')
        plt.show()'''

        # plotly paint
        data1 = {'x': data_time_1, 'y': data_nomalize}
        trace1 = Scatter(
            data1,
            mode='lines',
            marker=Marker(
                color='blue',
                symbol='square'))

        data2 = {'x': data_time_2, 'y': data_PAA}
        trace2 = Scatter(
            data2,
            mode='lines',
            marker=Marker(
                color='green',
                symbol='square'))

        data = Data([trace1, trace2])
        py.plot(data)

    def discretization(self, data):
        breakpoints_ = self.breakpoints[self.alphasize]
        string = ""
        for i in range(len(data)):
            if data[i] < breakpoints_[0]:
                string = string + 'a'
            elif data[i] > breakpoints_[len(breakpoints_) - 1]:
                string = string + chr(ord('a') + len(breakpoints_))
            else:
                for j in range(len(breakpoints_) - 1):
                    if data[i] >= breakpoints_[j] and \
                            data[i] < breakpoints_[j + 1]:
                        string = string + chr(ord('a') + j + 1)

        return string


def test():
    data = function.get_z('data/acc_data.txt')['z']
    '''a = np.std(data)
    data = np.log(data)
    b = np.std(data)
    print (a-b)/a'''
    s = SAX(w=15)

    n_data = s.normalize(data)
    '''print n_data
    print np.average(n_data)
    print np.std(n_data)'''
    paa_data = s.to_PAA(n_data)
    print s.discretization(paa_data)
    s.paint_PAA(n_data, paa_data)


if __name__ == '__main__':
    test()
