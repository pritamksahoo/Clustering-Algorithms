import numpy as np

def dist(p1, p2, flag):
	if flag == 1:
		return ((p1[0]-p2[0])**2 + (p1[1]-p2[1])**2)**(0.5)
	else:
		return (abs(p1[0]-p2[0]) + abs(p1[1]-p2[1]))


if __name__ == '__main__':
	no = int(input("Enter no. of points : "))
	s_no = ord('A')

	points = []
	for i in range(no):
		points.append(list(map(float, input(chr(s_no+i) + " : ").split())))

	n_clusters = int(input("Enter no. of clusters : "))
	c_center = int(input("Method of choosing initial centroids/seeds (1 for randomly, 0 for manually) : "))

	clusters = {}
	print("\nInitial Centers : ")
	if c_center == 0:
		for i in range(n_clusters):
			clusters[i+1] = {}
			clusters[i+1]["center"] = list(map(int, input("C{0} : ".format(i+1)).split()))

	else:
		n_rand = np.random.randint(0, no, n_clusters)
		for i in range(n_clusters):
			clusters[i+1] = {}
			clusters[i+1]["center"] = points[n_rand[i]]

			print("C{0} : {1}".format(i+1, ' '.join(list(map(str, clusters[i+1]["center"])))))

	d_f = int(input("Enter distance calculating function (1 for euclidean, 0 for manhattan) : "))

	print("\n================\nSOLUTION : \n================\n")

	change, epoch = True, 1
	while change:
		stable_clusters = {}

		for cl in clusters:
			stable_clusters[cl] = clusters[cl].copy()
			clusters[cl]["points"] = []

		print("---------------\nEPOCH #{0} : \n".format(epoch))

		for ind, point in enumerate(points):
			print("Point {0} : ".format(chr(s_no + ind)))

			min_d = 10**8
			n_cl = -1
			for cl in sorted(clusters.keys()):
				d = dist(point, clusters[cl]["center"], d_f)
				print("d({0}, C{1}) = {2}".format(chr(s_no + ind), cl, d))

				if min_d > d:
					min_d = d
					n_cl = cl

			clusters[n_cl]["points"].append(chr(s_no + ind))

			print("\nPoint {0} belongs to Cluster {1}\n".format(chr(s_no + ind), n_cl))

		print("New Cluster centers : ")
		for cl in sorted(clusters.keys()):
			clusters[cl]["center"] = list(np.average([points[ord(p)-s_no] for p in clusters[cl]["points"]], 0))
			print("C{0} = Mean of ({1}) = ({2})".format(cl, ', '.join(clusters[cl]["points"]), ' '.join(list(map(str, clusters[cl]["center"])))))

		print("\nAt the end of the epoch : " + str(clusters) + "\n")
		# print(stable_clusters)

		if stable_clusters == clusters:
			print("\n!!! No change since the last epoch !!!\n")
			change = False
		
		epoch = epoch + 1

	print("\n----------------\nAns : " + str(clusters) + "\n----------------\n")
