import plotly.plotly as py
import datetime
from plotly.graph_objs import *

def get_z(file_name):
	try:
		z = []
		time = []
		with open(file_name) as f:
			for line in f:
				data = line.split('"z":')
				data = data[1].split('}')
				time_tmp = data[1].split('"timestamp":')

				tmp = int(time_tmp[1])/1000
				time_tmp = datetime.datetime.\
					fromtimestamp(tmp).strftime('%Y-%m-%d %H:%M:%S')

				z.append(float(data[0]))
				time.append(time_tmp)
		data = {'x':time, 'y':z}
		return data
	except IOError as err:
		print("File error:" + str(err))

def paint():
	data = get_z('data2')
	#x = []
	#for i in range(0,len(z)):
	#	x.append(i+1)

	#data = {'x': x, 'y': z}

	trace1 = Scatter(
		data,
		mode='lines',
		marker=Marker(
			color='blue',
			symbol='square'))

	data = Data([trace1])
	py.plot(data)

if __name__ == '__main__':
	#get_z('data2')
	paint()