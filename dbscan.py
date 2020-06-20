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

	flag = int(input("Is distance matrix given? (1 for yes, 0 for no) : "))
	points = []

	if flag == 0:
		for i in range(no):
			points.append(list(map(float, input(chr(s_no+i) + " : ").split())))

		d_f = int(input("Enter distance calculating function (1 for euclidean, 0 for manhattan) : "))

		eps_n = {}
		dist_m = [[0 for j in range(no)] for i in range(no)]

		for i in range(no):
			for j in range(no):
				if i == j:
					dist_m[i][j] = 0

				elif i > j:
					dist_m[i][j] = dist_m[j][i]

				else:
					dist_m[i][j] = round(dist(points[i], points[j], d_f), 2)

	else:
		print("Enter the entire Distance Matrix : ")
		for i in range(no):
			dist_m[i] = list(map(float, input().split()))

		for i in range(no):
			for j in range(no):
				dist_m[i][j] = dist_m[j][i] = max(dist_m[i][j], dist_m[j][i])

	epsilon = float(input("Enter eps value : "))
	minpts = int(input("Enter Minimum Points : "))

	print("\n================\nSOLUTION : \n================\n")
	print("en : epsilon neighbourhood\n")

	print("Distance Matrix : ")
	for i in range(no):
		print(dist_m[i])

	print("\nEpsilon neighbourhood :")
	for ind, point in enumerate(points):
		eps_n[chr(s_no+ind)] = []
		print("en({0}) :".format(chr(s_no+ind)), end=' ')

		for j in range(no):
			if j != ind:
				if dist_m[ind][j] <= epsilon:
					eps_n[chr(s_no+ind)].append(chr(s_no+j))

		print(eps_n[chr(s_no+ind)])

	visit = [False for i in range(no)]
	outlier = []
	clusters, n_clusters = {}, 0

	for ind, point in enumerate(points):
		if not visit[ind]:
			visit[ind] = True
			print("\n----------------\nPoint {0} : unvisited".format(chr(s_no+ind)))

			if len(eps_n[chr(s_no+ind)]) >= minpts-1:
				print("!!! Core point !!!")
				cl_set = set(eps_n[chr(s_no+ind)])

				n_clusters = n_clusters + 1
				clusters[n_clusters] = [chr(s_no + ind)]
				print("Point {0} goes to Cluster C{1}".format(chr(s_no+ind), n_clusters))

				while len(cl_set) != 0:
					el = list(cl_set)[0]
					print("EN_SET :", cl_set)
					print("\t--------\n\tConsidering point {0} of its en-set".format(el))
					if not visit[ord(el)-s_no]:
						print("\t\t! Not visited !")
						visit[ord(el)-s_no] = True

						if len(eps_n[el]) >= minpts-1:
							print("\t\t! Core Point !")
							print("\t\tPutting all points of en-set of point {0} into en-set of Point {1}".format(el, chr(s_no+ind)))
							for po in eps_n[el]:
								cl_set.add(po)

						clusters[n_clusters].append(el)
						print("\t\tPoint {0} goes to Cluster C{1}".format(el, n_clusters))

					elif el in outlier:
						print("\t\tAlready visited and not included in any cluster. So, point {0} goes to Cluster C{1}".format(el, n_clusters))
						clusters[n_clusters].append(el)

					cl_set.remove(el)
			else:
				print("Not a core point!!! Marking as outlier for now! May be considered later!")
				outlier.append(chr(s_no+ind))

	print("\n----------------\nAns : \n")
	print("Clusters :", clusters)
	print("Outliers :", outlier)
	print()