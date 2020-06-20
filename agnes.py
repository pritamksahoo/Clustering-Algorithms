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
	dist_m = [[0 for j in range(no)] for i in range(no)]

	if flag == 0:
		for i in range(no):
			points.append(list(map(float, input(chr(s_no+i) + " : ").split())))

		d_f = int(input("Enter distance calculating function (1 for euclidean, 0 for manhattan) : "))

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
			for j in range(no):
				dist_m[i] = list(map(float, input().split()))

		for i in range(no):
			for j in range(no):
				dist_m[i][j] = dist_m[j][i] = max(dist_m[i][j], dist_m[j][i])

	linkage = int(input("Enter the linkage type (1-Single, 2-Complete, 3-Average) : "))
	termination = input("Enter the termination cond. distance (Leave blank for no condition) : ")

	if termination == "":
		termination = 10**8
	else:
		termination = int(termination)

	print("\n================\nSOLUTION : \n================\n")

	clusters = { i: [chr(s_no+i)] for i in range(no) }
	epoch, n_clusters = 1, no

	while True:
		print("\n----------------\nEpoch {0} : ".format(epoch), '\n')

		for cl in sorted(clusters.keys()):
			st = ''.join(clusters[cl])

			print("%10s" % (st), end='')

		print()
		# print("      ".join([''.join(clusters[cl]) for cl in sorted(clusters.keys())]))
		for i in range(n_clusters):
			for j in range(n_clusters):
				print("%10.2f" % (dist_m[i][j]), end='')

			print()

		r, c, min_d = None, None, 10**8
		for i in range(n_clusters):
			for j in range(n_clusters):
				if min_d > dist_m[i][j] and i != j:
					min_d = dist_m[i][j]
					r, c = i, j

		print("\nCluster {0} and {1} have minimum distance between them, which is {2}".format(''.join(clusters[r]), ''.join(clusters[c]), min_d), end = ' ')
		if min_d > termination:
			print("> termination threshold !!!")
			break

		else:
			print("<= termination threshold")
			min_cell, max_cell = min(r, c), max(r, c)

			print("\nRecalculating Distance matrix - ")
			for k in range(n_clusters):
				if k != min_cell and k != max_cell:
					if linkage == 1:
						d = min(dist_m[min_cell][k], dist_m[max_cell][k])
					elif linkage == 2:
						d = max(dist_m[min_cell][k], dist_m[max_cell][k])
					else:
						l1, l2 = len(clusters[min_cell]), clusters[max_cell]
						d = (l1*dist_m[min_cell][k] + l2*dist_m[max_cell][k]) / (l1 + l2)

					dist_m[min_cell][k] = dist_m[k][min_cell] = d

			clusters[min_cell] = clusters[min_cell] + clusters[max_cell]
			for k in range(max_cell, n_clusters-1):
				clusters[k] = clusters[k+1].copy()

			clusters.pop(n_clusters-1)
			print("\nClusters :", clusters, "\n")
			n_clusters = n_clusters-1

			dist_m = np.delete(np.array(dist_m), (max_cell), axis=0)
			dist_m = np.delete(np.array(dist_m), (max_cell), axis=1)

			if n_clusters == 1:
				break

		epoch = epoch + 1

	print("\n----------------\nANS : \n")
	print("Clusters :", clusters, "\n")