import function
import qu_zao
import reduce_dimension

def main():
	data = function.get_z('acc_data3.txt')
	data = data['z']
	#quzao
	data_f = qu_zao.qu_zao_fourier(data)
	data_w = qu_zao.qu_zao_wavelet(data)

	#reduce dimension
	time = range(len(data))
	data = {'time': time, 'z': data_w}
	data = reduce_dimension.main(data)

if __name__ == '__main__':
	main()