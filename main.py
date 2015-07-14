import function
import denoise
import similarity_measure
import numpy as np


def main():
    data_origin = function.get_z('acc_data.txt')
    data = np.array(data_origin['z'])
    data_mean = function.mean(data)
    data = data - data_mean

    '''# paint origin data
    tmp = {'time': data_origin['time'], 'z': data}
    function.paint(tmp)'''

    # fourier tansform
    data_fourier = np.fft.fft(data)
    for i in range(len(data)):
        '''# 0-2.5 low pass
        if i > 2500 and i < len(data) - 2500:
            data_fourier[i] = 0'''
        '''# 20k-30k band pass
        if not ((i > 20000 and i < 30000) or
                (i > len(data) - 30000 and i < len(data) - 20000)):
            data_fourier[i] = 0'''
        '''# 33k-37k band pass
        if not ((i > 33000 and i < 37000) or
                (i > len(data) - 37000 and i < len(data) - 33000)):
            data_fourier[i] = 0'''
        '''# 48k-52k band pass
        if not ((i > 48000 and i < 52000) or
                (i > len(data) - 48000 and i < len(data) - 52000)):
            data_fourier[i] = 0'''
        # 70-73k band pass
        if not ((i > 70000 and i < 73000) or
                (i > len(data) - 70000 and i < len(data) - 73000)):
            data_fourier[i] = 0
    data_denoise = np.fft.ifft(data_fourier).real
    # paint
    time = []
    for i in range(len(data)):
        time.append(data_origin['time'][i])
    tmp = {'time': time, 'z': data_denoise}
    function.paint(tmp)

    '''# denoise
    data_denoise_f = denoise.qu_zao_fourier(data)
    #data_w = denoise.qu_zao_wavelet(data)
    # paint
    tmp = {'time': time, 'z': data_denoise_f}
    function.paint(tmp)

    # fourier transform of denosing data
    data_denoise_f_f = function.fft(data_denoise_f)
    # paint
    tmp = {'time': time, 'z': data_denoise_f_f}
    function.paint(tmp)'''

    # paint
    '''time = []
    for i in range(len(data_f)):
        time.append(i)'''

    '''# reduce dimension
    time = range(len(data))
    data = {'time': time, 'z': data_w}
    data = reduce_dimension.main(data)'''

if __name__ == '__main__':
    main()
