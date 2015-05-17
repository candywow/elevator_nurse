import function
import time
import datetime
import math

class Point(object):
	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y

	def __repr__(self):
		return "x:%f, y:%f" % (self.x, self.y)

class TreeNode(object):
	def __init__(self, x=0, y=0, left=0, right=0, dist=0):
		self.x = x
		self.y = y
		self.left = left
		self.right = right
		self.dist = dist

class SBTree(object):
	def __init__(self, root=0):
		self.root = root


def restruct(data):
	data_new = []
	for i in range(len(data['z'])):
		tmp_point = Point(data['time'][i], data['z'][i])
		print tmp_point
		data_new.append(tmp_point)

	return data_new

def calculate_vd(point1, point2, point3):
	vd = abs(point1.y + (point2.y - point1.y) * \
		(point3.x - point1.x) / (point2.x - point1.x) - point3.y)

	#print vd
	return vd

def pip_identification(array_point):
	pip_list = []
	max_vd_list = []

	pip_list.append(len(array_point) - 1)
	pip_list.append(0)
	max_vd_list.append(0)
	max_vd_list.append(0)

	for k in range(len(array_point) - 2):
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

	print pip_list
	print max_vd_list

def paint(array_point):
	time = []
	z = []

	for item in array_point:
		time_tmp = datetime.datetime.\
						fromtimestamp(item.x).strftime('%Y-%m-%d %H:%M:%S:%f')
		time.append(time_tmp)
		z.append(item.y)

	data = {'time':time, 'z':z}
	function.paint(data)

def main():
	z = function.get_z('data3')
	data = restruct(z)
	#paint(data)
	pip_identification(data)

if __name__ == '__main__':
	main()