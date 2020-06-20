import numpy as np

def dist(p1, p2, flag):
	if flag == 1:
		ans = 0
		for i in range(len(p1)):
			ans = ans + (p1[i]-p2[i])**2

		return (ans)**(0.5)
	else:
		ans = 0
		for i in range(len(p1)):
			ans = ans + abs(p1[i]-p2[i])

		return ans


if __name__ == '__main__':
	no = int(input("Enter no. of points : "))
	s_no = ord('A')

	points = []
	for i in range(no):
		points.append([list(map(float, input(chr(s_no+i) + " : ").split())), None])

	threshold = int(input("Enter threshold distance : "))

	clusters = {}
	n_clusters = 0

	d_f = int(input("Enter distance calculating function (1 for euclidean, 0 for manhattan) : "))

	print("\n================\nSOLUTION : \n================\n")

	for ind, point in enumerate(points):
		print("\n----------------\nPoint {0} : ".format(chr(s_no+ind)))
		if n_clusters == 0:
			n_clusters = n_clusters + 1
			points[ind][1] = n_clusters
			print("!!! Point {0} goes to Cluster C{1} !!!".format(chr(s_no+ind), n_clusters))

		else:
			target_point, min_d = None, 10**8
			for index in range(ind):
				d = dist(point[0], points[index][0], d_f)

				print("d({0}, {1}) = {2}".format(chr(s_no+ind), chr(s_no+index), d))

				if min_d > d:
					min_d = d
					target_point = index

			if min_d <= threshold:
				print("Min Distance = {0} <= threshold".format(min_d))
				points[ind][1] = points[target_point][1]
				print("!!! Point {0} goes to Cluster C{1} !!!".format(chr(s_no+ind), points[target_point][1]))
			else:
				print("Min Distance = {0} > threshold".format(min_d))
				n_clusters = n_clusters + 1
				points[ind][1] = n_clusters
				print("!!! Point {0} goes to Cluster C{1} !!!".format(chr(s_no+ind), n_clusters))

	print("\n----------------\nAns : \n")
	for ind, p in enumerate(points):
		cl = p[1]
		point = chr(s_no + ind)

		if clusters.get(cl, None) is None:
			clusters[cl] = [point]

		else:
			clusters[cl].append(point)

	print(clusters)
	print()