import plotly.plotly as py
import datetime
import time
from plotly.graph_objs import *

def get_z(file_name):
	try:
		z = []
		time = []
		f1 = open('test.txt', 'w')
		with open(file_name) as f:
			for line in f.readlines()[4500:4520]:
				f1.write(line)
				#try:
				data = line.split('"z":')
				data = data[1].split('}')
				time_tmp = data[1].split('"timestamp":')

				tmp = int(time_tmp[1])/1000.0
				'''print tmp
				time_tmp = datetime.datetime.\
						fromtimestamp(tmp).strftime('%Y-%m-%d %H:%M:%S.%f')
					
				print time_tmp'''

				x = line.split('"x":')
				x = x[1].split(',')

				z.append(float(x[0]))
				time.append(tmp)
				#except:
				#	pass
		data = {'time':time, 'z':z}
		#print data
		f1.close()
		return data
	except IOError as err:
		print("File error:" + str(err))

def get_z_new(file_name):
	z = []
	time = []
	with open(file_name) as f:
		for line in f.readlines()[0:2]:
			try:
				data = line.split(',')
				z_per = data[2].split(' ')[1].split(']')[0]
				time_tmp = data[3].split('\n')[0]
				print time_tmp
				time_per = datetime.datetime.\
					fromtimestamp(tmp).strftime('%Y-%m-%d %H:%M:%S')

				z.append(z_per)
				time.append(time_per)
			except:
				pass

	print z
	print time
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
	get_z('data3')
	#paint()
	#get_start_num()