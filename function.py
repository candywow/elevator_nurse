import plotly.plotly as py
import datetime
import time
from plotly.graph_objs import *

def get_z(file_name):
	try:
		z = []
		time = []
		with open(file_name) as f:
			for line in f.readlines()[140000:]:
				data = line.split(',')
				#print data
				data_z = data[2].split(':')[1]
				data_z = data_z.split('}')[0]
				#print data_z
				data_time = data[3].split('\n')[0]
				'''tmp = float(data_time)
				data_time = datetime.datetime.\
						fromtimestamp(tmp).strftime('%Y-%m-%d %H:%M:%S.%f')'''
				z.append(float(data_z))
				#time.append(data_time)
				time.append(float(data_time))
				#try:
				'''
				data = line.split('"z":')
				#data = data[1].split('}')
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
				#except:
				#	pass
		data = {'time':time, 'z':z}
		#print data
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
				#print data
				z_per = data[1].split(':')[1].split('}')[0]

				time_tmp = data[3].split('\n')[0]
				tmp = float(time_tmp)
				time_per = datetime.datetime.\
						fromtimestamp(tmp).strftime('%Y-%m-%d %H:%M:%S.%f')
				#print time_per

				z.append(z_per)
				time.append(time_per)
			except:
				pass

	data = {'time':time, 'z':z}
	#print data
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
			elif (tmp > -0.95) or (tmp == -1) :
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



def paint(data):
	data = {'x': data['time'], 'y': data['z']}

	trace1 = Scatter(
		data,
		mode='lines',
		marker=Marker(
			color='blue',
			symbol='square'))

	data = Data([trace1])
	py.plot(data)

if __name__ == '__main__':
	data = get_z('acc_data3.txt')
	#paint(data)
	#get_start_num()