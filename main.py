import function
import denoise
import similarity_measure
import paint_mark
import numpy as np
import time
import plotly.plotly as py
from plotly.graph_objs import *


def main():
    # acc_data
    data_origin = function.get_z('acc_data.txt')
    data = np.array(data_origin['z'])
    data_mean = function.mean(data)
    data = data - data_mean
    print data
    # print data_origin['time']

    '''# paint origin data
    tmp = {'time': data_origin['time'], 'z': data}
    function.paint(tmp)'''

    # fourier tansform
    data_fourier = np.fft.fft(data)
    #with open('data_fourier_70k_73k.txt', 'w+') as f:
    for i in range(len(data)):
        # high pass
        if i < 20000 or i > len(data) - 20000:
            data_fourier[i] = 0
        '''# 0-2.5k low pass
        if i > 2500 and i < len(data) - 2500:
            data_fourier[i] = 0
        # 20k-30k band pass
        if not ((i > 20000 and i < 30000) or
                (i > len(data) - 30000 and i < len(data) - 20000)):
            data_fourier[i] = 0
        # 33k-37k band pass
        if not ((i > 33000 and i < 37000) or
                (i > len(data) - 37000 and i < len(data) - 33000)):
            data_fourier[i] = 0
        # 48k-52k band pass
        if not ((i > 48000 and i < 52000) or
                (i > len(data) - 48000 and i < len(data) - 52000)):
            data_fourier[i] = 0
        # 70-73k band pass
        if not ((i > 70000 and i < 73000) or
                (i > len(data) - 70000 and i < len(data) - 73000)):
            data_fourier[i] = 0'''
    #print data_fourier
    data_denoise = np.fft.ifft(data_fourier).real
    #print data_denoise
        # for i in data_denoise:
        #    f.write(str(i) + '\n')'''
    '''# paint
    time = []
    for i in range(len(data)):
        time.append(data_origin['time'][i])
    tmp = {'time': time, 'z': data_denoise}
    function.paint(tmp)'''

    '''# denoise
    data_denoise_f = denoise.qu_zao_fourier(data)
    #data_w = denoise.qu_zao_wavelet(data)
    # paint
    tmp = {'time': time, 'z': data_denoise_f}
    function.paint(tmp)'''

    '''# fourier transform of denosing data
    data_denoise_f_f = function.fft(data_denoise)
    # paint
    time = []
    for i in range(len(data_denoise_f_f)):
        time.append(i)
    tmp = {'time': time, 'z': data_denoise_f_f}
    function.paint(tmp)'''

    '''# paint
    time = []
    for i in range(len(data_f)):
        time.append(i)'''

    '''# reduce dimension
    time = range(len(data))
    data = {'time': time, 'z': data_w}
    data = reduce_dimension.main(data)'''

    '''# acc_desk
    data = []
    data_time = []
    with open('acc_desk.txt') as d:
        for line in d.readlines()[1000:13500]:
            line = line.strip()
            item = line.split(',')
            data.append(float(item[0]))
            #print item[-1]
            t = time.localtime(float(item[-1]))
            time_per = time.strftime("%Y-%m-%d %H:%M:%S", t)
            #print time_per
            #time.append(time.localtime(float(item[-1])))

    data = np.array(data)
    data_mean = function.mean(data)
    data = data - data_mean
    #print time

    #print origin data
    tmp = {'time': time, 'z': data}
    function.paint(tmp)

    # fourier transform
    data_fourier = function.fft(data)
    time = range(len(data))
    tmp = {'time': time, 'z': data_fourier}
    function.paint(tmp)'''

    # paint mark on 0-2500hz
    data1 = {'x': data_origin['time'], 'y': data}
    trace1 = Scatter(
        data1,
        mode='lines',
        marker=Marker(
            color='blue',
            symbol='square'))
    elevator_data = paint_mark.read_mark()
    tmp_action = np.zeros(len(elevator_data['action']))
    tmp_action += 0.1
    # print tmp
    trace2 = Bar(
        x=elevator_data['action_time'],
        y=tmp_action
    )
    #tmp_in_out = np.zeros(len(elevator_data['in_out']))
    #tmp_in_out += 0.1
    tmp_in_out = []
    for i in elevator_data['in_out']:
        if i == 0:
            tmp_in_out.append(-0.1)
        else:
            tmp_in_out.append(0.1)

    trace3 = Bar(
        x=elevator_data['in_out_time'],
        y=tmp_in_out,
        maker=Marker(color='#FA8072')
    )

    data2 = {'x': data_origin['time'], 'y': data_denoise}
    trace4 = Scatter(
        data2,
        mode='lines',
        opacity=0.5,
        marker=Marker(
            color='green',
            symbol='square'))

    data = Data([trace1, trace2, trace3， trace4])
    #data = Data([trace4])
    py.plot(data)


if __name__ == '__main__':
    main()
