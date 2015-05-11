import xlrd
import plotly.plotly as py
from plotly.graph_objs import *

data = xlrd.open_workbook('data.xlsx')
table = data.sheets()[0]

nrows = table.nrows
ncols = table.ncols

x = table.col_values(0)[1:]
#print x
y1 = table.col_values(6)[1:]
y2 = table.col_values(7)[1:]
y3 = table.col_values(8)[1:]
y4 = table.col_values(9)[1:]

data1 = {'x': x, 'y': y1}
data2 = {'x': x, 'y': y2}
data3 = {'x': x, 'y': y3}
data4 = {'x': x, 'y': y4}

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

data = Data([trace1, trace2, trace3, trace4])
py.plot(data)