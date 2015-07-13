import function
import denoise
import reduce_dimension


def main():
    data = function.get_z('acc_data.txt')
    data = data['z']

    # denoise
    data_f = denoise.qu_zao_fourier(data)
    #data_w = denoise.qu_zao_wavelet(data)

    # paint
    time = []
    for i in range(len(data_f)):
        time.append(i)
    tmp = {'time': time, 'z': data_f}
    function.paint(tmp)

    '''# reduce dimension
    time = range(len(data))
    data = {'time': time, 'z': data_w}
    data = reduce_dimension.main(data)'''

if __name__ == '__main__':
    main()
