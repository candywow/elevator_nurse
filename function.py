import plotly.plotly as py
import datetime
import time
import math
from plotly.graph_objs import *
import numpy as np
import matplotlib.pyplot as plt


def get_z(file_name):
    try:
        z = []
        time = []
        with open(file_name) as f:
            for line in f.readlines()[410000:590010]:
                data = line.split(',')
                # print data
                data_z = data[1].split(':')[1]
                data_z = data_z.split('}')[0]
                # print data_z
                data_time = data[3].split('\n')[0]
                tmp = float(data_time)
                data_time = datetime.datetime.\
                    fromtimestamp(tmp).strftime('%Y-%m-%d %H:%M:%S.%f')
                z.append(float(data_z))
                # time.append(data_time)
                time.append(data_time)
                # try:
                '''
				data = line.split('"z":')
				# data = data[1].split('}')
				data = data[1].split(']')
				time_tmp = data[1].split('"timestamp":')

				tmp = float(time_tmp[1])/1000.0
				print tmp
				time_tmp = datetime.datetime.\
						fromtimestamp(tmp).strftime('%Y-%m-%d %H:%M:%S.%f')

				print time_tmp

				x = line.split('"x":')
				x = x[1].split(',')

				z.append(float(x[0]))
				time.append(tmp)'''
                # except:
                #	pass
        data = {'time': time, 'z': z}
        # print data
        return data
    except IOError as err:
        print("File error:" + str(err))


def get_z_new(file_name):
    z = []
    time = []
    with open(file_name) as f:
        for line in f.readlines():
            try:
                data = line.split(',')
                # print data
                z_per = data[1].split(':')[1].split('}')[0]

                time_tmp = data[3].split('\n')[0]
                tmp = float(time_tmp)
                time_per = datetime.datetime.\
                    fromtimestamp(tmp).strftime('%Y-%m-%d %H:%M:%S.%f')
                # print time_per

                z.append(z_per)
                time.append(time_per)
            except:
                pass

    data = {'time': time, 'z': z}
    # print data
    return data


def get_start_num():
    tmp = -1
    num = 0
    data = get_z('data3')
    for z in data['z']:
        if z > -0.95:
            print 'z %s' % z
            print 'tmp %s' % tmp
            if tmp < -1.05:
                num += 1
                tmp = -1
            elif (tmp > -0.95) or (tmp == -1):
                tmp = z
        elif z < -1.05:
            print 'z %s' % z
            print 'tmp %s' % tmp
            if tmp > -0.95:
                num += 1
                tmp = -1
            elif (tmp < -1.05) or (tmp == -1):
                tmp = z

    print num


def paint(data1, data2=0):
    data1 = {'x': data1['time'], 'y': data1['z']}

    trace1 = Scatter(
        data1,
        mode='lines',
        marker=Marker(
            color='blue',
            symbol='square'))

    data = Data([trace1])
    if data2 != 0:
        data2 = {'x': data2['time'], 'y': data2['z']}
        trace2 = Scatter(
            data2,
            mode='lines',
            marker=Marker(
                color='green',
                symbol='square'))

        data = Data([trace1, trace2])
    py.plot(data)


def paint_mat(data):
    plt.figure(figsize=(8, 8))
    plt.plot_date(data['time'], data['z'])
    plt.show()


def fft(data):
    result = []
    xf = np.fft.fft(data)
    for item in xf:
        # print item
        amp = math.sqrt(item.real ** 2 + item.imag ** 2)
        result.append(amp)
        # print amp
    return result

def mean(data):
    return float(sum(data))/len(data)

def get_data():
    result = {}
    data_z = []
    time = []
    with open('acc_desk.txt') as f:
        for line in f.readlines():
            # print line
            data = line.strip('\n').split(',')
            # data = data.split(',')
            #tmp = float(data[-1])
            #data_time = datetime.datetime.\
            #    fromtimestamp(tmp).strftime('%Y-%m-%d %H:%M:%S.%f')
            data_z.append(data[2])
            time.append(data[-1])

    result['z'] = data_z
    result['time'] = time
    # print result
    paint_mat(result)

if __name__ == '__main__':
    data = get_z('acc_data.txt')
    print mean(data['z'][:10])

    '''# get_data()
    data = get_z('acc_data.txt')
    #print data
    dataf = fft(data['z'])
    time = []
    for i in range(len(dataf)):
        time.append(i)
    z = {'time': time, 'z': data['z']}
    zz = {'time': time, 'z': dataf}

    # print max(dataf)
    # plt.plot(dataf)
    # plt.show()
    paint(zz)
    # get_start_num()'''
