from scipy import signal
import numpy as np
import matplotlib.pyplot as pl
import matplotlib
import math
import function
import pywt
from operator import attrgetter

myfont = matplotlib.font_manager.FontProperties\
(fname='c:\\windows\\fonts\\fzshjw_0.ttf') 

#Fourier
def qu_zao_fourier(data):
	b, a = signal.butter(3, 0.10, 'low')
	sf = signal.filtfilt(b, a ,data)
	'''pl.subplot(121)
	pl.title(u'yuanshixinhao', fontproperties=myfont)
	pl.plot(data)
	pl.subplot(122)
	pl.title(u'fourierquzaojieguo', fontproperties=myfont)
	pl.plot(sf)
	pl.show()'''
	return sf

#wavelet
def wavedec(data, wavelet, level=None, mode='sym'):
	coeffs_list = []

	a = data
	for i in range(level):
		a, d = pywt.dwt(a, wavelet, mode)
		coeffs_list.append(d)

	coeffs_list.append(a)
	coeffs_list.reverse()

	return coeffs_list

def waverec(coeffs_list, wavelet, mode='sym'):
	a, ds = coeffs_list[0], coeffs_list[1:]

	for d in ds:
		a = pywt.idwt(a, d, wavelet, mode, 1)

	return a

def qu_zao_wavelet(data):
	std = np.std(data)
	r = std * math.sqrt(2 * math.log(len(data)))
	#print r
	coeffs_list = wavedec(data, 'db2', 3)
	#print coeffs_list
	for i in range(1, len(coeffs_list)):
		for j in range(len(coeffs_list[i])):
			if coeffs_list[i][j] >= r:
				coeffs_list[i][j] = coeffs_list[i][j] - r
			elif coeffs_list[i][j] <= -r:
				coeffs_list[i][j] = coeffs_list[i][j] + r
			else:
				coeffs_list[i][j] = 0

	#print coeffs_list
	result = waverec(coeffs_list, 'db2')
	'''pl.subplot(121)
	pl.title(u'yuanshixinhao', fontproperties=myfont)
	pl.plot(data)
	pl.subplot(122)
	pl.title(u'waveletquzaojieguo', fontproperties=myfont)
	pl.plot(result)
	pl.show()'''
	return result

if __name__ == '__main__':
	data = function.get_z('acc_data3.txt')
	data = data['z']
	qu_zao_fourier(data)
	#qu_zao_wavelet(data)

