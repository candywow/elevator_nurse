import function
import plotly.plotly as py
import datetime
import time
from plotly.graph_objs import *
import math
import pywt
import matplotlib.pyplot as plt
from operator import attrgetter

class Point(object):
	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y

	def __repr__(self):
		return "x:%f, y:%f" % (self.x, self.y)

class TreeNode(object):
	def __init__(self, point=None, left=None, right=None, dist=None, index=-1):
		self.point = point
		self.left = left
		self.right = right
		self.dist = dist
		self.index = index

class SBTree(object):
	def __init__(self, root=0):
		self.root = root

	def is_empty(self):
		if self.root is 0:
			return True
		else:
			return False

	def create(self, pip_list, array_point, max_vd_list):
		#let last data point become the root of SBTree
		last_point = array_point[pip_list[0]]
		cnode = TreeNode(last_point, None, None, max_vd_list[0], pip_list[0])
		self.root = cnode
		pnode = self.root

		#let first data point become the right child of root
		first_point = array_point[pip_list[1]]
		cnode = TreeNode(first_point, None, None, max_vd_list[1], pip_list[1])
		pnode.left = cnode
		pnode = cnode

		for i in range(2,len(pip_list)):
			tmp_point = array_point[pip_list[i]]
			cnode = TreeNode(tmp_point, None, None, max_vd_list[i], pip_list[i])
			pnode = self.root.left
			while True:
				if cnode.point.x < pnode.point.x:
					if pnode.left == None:
						pnode.left = cnode
						break
					else:
						pnode = pnode.left
				else:
					if pnode.right == None:
						pnode.right = cnode
						break
					else:
						pnode = pnode.right

	def middle_order(self, tree_node):
		if tree_node.left != None:
			self.middle_order(tree_node.left)
		print tree_node.index
		if tree_node.right != None:
			self.middle_order(tree_node.right)

	def display(self):
		self.middle_order(self.root)

	def find_max(self, tmp):
		max = TreeNode()
		max.dist = 0

		for node in tmp['heap']:
			if node.dist >= max.dist:
				max = node
		#print 'max:'
		#print max.index

		tmp['result'].append(max)
		tmp['heap'].remove(max)

		if max.left != None:
			tmp['heap'].append(max.left)
		if max.right != None:
			tmp['heap'].append(max.right)

	def access(self, length):
		result = []
		heap = []
		tmp = {'result': result, 'heap': heap}
		tmp['result'].append(self.root)
		tmp['result'].append(self.root.left)
		node = self.root.left

		if node.left != None:
			tmp['heap'].append(node.left)
		if node.right != None:
			tmp['heap'].append(node.right)

		for i in range(length):
			self.find_max(tmp)

		#print 'result:'
		#for i in tmp['result']:
		#	print i.index
		return result

def restruct(data):
	data_new = []
	for i in range(len(data['z'])):
		tmp_point = Point(data['time'][i], data['z'][i])
		#print tmp_point
		data_new.append(tmp_point)

	return data_new

def calculate_vd(point1, point2, point3):
	vd = abs(point1.y + (point2.y - point1.y) * \
		(point3.x - point1.x) / (point2.x - point1.x) - point3.y)

	#print vd
	return vd

def pip_identification(array_point, rate):
	num = len(array_point) / rate

	pip_list = []
	max_vd_list = []

	pip_list.append(len(array_point) - 1)
	pip_list.append(0)
	max_vd_list.append(0)
	max_vd_list.append(0)

	for k in range(num):
		print k
		vd = []
		#print 'k %d' % k

		for i in range(len(array_point)):
			#print 'i %d' % i
			flag = True
			adjacent_left = 0
			adjacent_right = len(array_point) - 1
			for j in range(len(pip_list)):
				if i == pip_list[j]:
					flag = False
					break
				elif (pip_list[j] < i and pip_list[j] > adjacent_left):
					adjacent_left = pip_list[j]
				elif (pip_list[j] > i and pip_list[j] < adjacent_right):
					adjacent_right = pip_list[j]

			if flag:
				#print 'left %d' % adjacent_left
				#print 'right %d' % adjacent_right
				tmp_vd = calculate_vd(array_point[adjacent_left], \
					array_point[adjacent_right], array_point[i])

				tmp_vd = {'vd': tmp_vd, 'index': i}

				vd.append(tmp_vd)

		#print 'vd'
		#print vd
		max_vd = {'vd': 0, 'index': -1}
		for distance in vd:
			if distance['vd'] >= max_vd['vd']:
				max_vd = distance

		pip_list.append(max_vd['index'])
		max_vd_list.append(max_vd['vd'])
		#print 'pip_list: '
		#print pip_list

	tmp_list = {'pip_list': pip_list, 'max_vd_list': max_vd_list}
	#print pip_list
	#print max_vd_list
	return tmp_list

def tree_pruning(max_vd_list):
	change_vd = []
	for i in range(2, len(max_vd_list)-1):
		tmp = abs(max_vd_list[i] - max_vd_list[i+1])
		tmp = {'change_vd': tmp, 'index': i}
		change_vd.append(tmp)
	#paint_change_vd(change_vd)

	max = {'change_vd': 0, 'index': -1}
	for item in change_vd:
		if item['change_vd'] >= max['change_vd']:
			max = item
	#print max['index'] 

	return max['index'] + 1



def paint_change_vd(change_vd):
	time = range(2, len(change_vd)+2)
	tmp_vd = []
	for item in change_vd:
		tmp_vd.append(item['change_vd'])
	data = {'time':time, 'z':tmp_vd}
	function.paint(data)


def paint(array_point):
	time = []
	z = []

	sorted_point = sorted(array_point, key=attrgetter('x'))

	for item in sorted_point:
		#time_tmp = datetime.datetime.\
		#				fromtimestamp(item.x).strftime('%Y-%m-%d %H:%M:%S:%f')
		time.append(item.x)
		z.append(item.y)

	data = {'time':time, 'z':z}
	function.paint(data)

def paint_vd(max_vd_list):
	time = range(2, len(max_vd_list))
	z = max_vd_list[2:len(max_vd_list)]
	data = {'time':time, 'z':z}
	function.paint(data)

def sample(data, rate):
	result = []
	number = len(data) / rate
	i = 0
	while len(result) != number:
		result.append(data[i*rate])
		i += 1
	return result

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
		a = pywt.idwt(a, None, wavelet, mode)

	return a

def dwt(data, level=1):
	coeffs_list = wavedec(data['z'], 'db2', level)
	y = waverec(coeffs_list, 'db2')
	x = range(len(y))

	result = {'z': y, 'time':x}
	#function.paint(result)
	return result
	

def main():
	z = function.get_z('acc_data3.txt')
	data = dwt(z, 8)
	data = restruct(data)
	#paint(data)
	
	tmp_list = pip_identification(data, 100)
	pip_list = tmp_list['pip_list']
	#print pip_list
	result = []
	for i in pip_list:
		result.append(data[i])
	#print result
	paint(result)
	'''max_vd_list = tmp_list['max_vd_list']
	#paint_vd(max_vd_list)
	length = tree_pruning(max_vd_list)
	#print length
	#paint_change_vd(change_vd)
	#print pip_list
	#print max_vd_list

	sb_tree = SBTree()
	sb_tree.create(pip_list, data, max_vd_list)
	result = sb_tree.access(length)
	tmp = []

	for item in result:
		tmp.append(item.point)
	paint(tmp)'''
	#print 'middle_order:'
	#sb_tree.display()'''

if __name__ == '__main__':
	main()