import xlrd
import plotly.plotly as py
from plotly.graph_objs import *

data = xlrd.open_workbook('data2.xlsx')
table = data.sheets()[0]

nrows = table.nrows
ncols = table.ncols

a1 = -8.74554e-4
b1 = 8.76441e-5
a2 = -6.46049e-4
b2 = 7.27853e-5
a3 = -2.6283e-4
b3 = 4.9049e-5
a4 = -0.00143
b4 = 1.64825e-4

x = table.col_values(0)[1:]
#print x
y1 = table.col_values(6)[1:]
y2 = table.col_values(7)[1:]
y3 = table.col_values(8)[1:]
y4 = table.col_values(9)[1:]

y5 = []
y6 = []
y7 = []
y8 = []

for item in x:
	tmp1 = a1 + b1 * item
	tmp2 = a2 + b2 * item
	tmp3 = a3 + b3 * item
	tmp4 = a4 + b4 * item

	y5.append(tmp1)
	y6.append(tmp2)
	y7.append(tmp3)
	y8.append(tmp4)

data1 = {'x': x, 'y': y1}
data2 = {'x': x, 'y': y2}
data3 = {'x': x, 'y': y3}
data4 = {'x': x, 'y': y4}
data5 = {'x': x, 'y': y5}
data6 = {'x': x, 'y': y6}
data7 = {'x': x, 'y': y7}
data8 = {'x': x, 'y': y8}

#print data5

trace1 = Scatter(
	data1,
	mode='lines',
	marker=Marker(
		color='blue',
		symbol='square'))

trace2 = Scatter(
	data2,
	mode='lines',
	marker=Marker(
		color='red',
		symbol='square'))

trace3 = Scatter(
	data3,
	mode='lines',
	marker=Marker(
		color='orange',
		symbol='square'))

trace4 = Scatter(
	data4,
	mode='lines',
	marker=Marker(
		color='green',
		symbol='square'))

#trace5 = Scatter(
#	data5,
#	mode='lines',
#	marker=Marker(
#		color='blue',
#		symbol='square'))

#trace6 = Scatter(
#	data6,
#	mode='lines',
#	marker=Marker(
#		color='red',
#		symbol='square'))

#trace7 = Scatter(
#	data7,
#	mode='lines',
#	marker=Marker(
#		color='orange',
#		symbol='square'))

#trace8 = Scatter(
#	data8,
#	mode='lines',
#	marker=Marker(
#		color='green',
#		symbol='square'))

#data = Data([trace1, trace2, trace3, trace4, trace5, trace6, trace7, trace8])
data = Data([trace1, trace2, trace3, trace4])
py.plot(data)