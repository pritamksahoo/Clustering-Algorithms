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
		while len(set(n_rand)) != n_clusters:
			n_rand = np.random.randint(0, no, n_clusters)

		for i in range(n_clusters):
			clusters[i+1] = {}
			clusters[i+1]["center"] = points[n_rand[i]]

			print("C{0} : {1}".format(i+1, ' '.join(list(map(str, clusters[i+1]["center"])))))

	d_f = int(input("Enter distance calculating function (1 for euclidean, 0 for manhattan) : "))

	print("\n================\nSOLUTION : \n================\n")

	change, epoch, old_cost = True, 1, 10**8
	while change:
		stable_clusters, new_cost = {}, 0

		for cl in clusters:
			stable_clusters[cl] = clusters[cl].copy()
			clusters[cl]["points"] = [] if clusters[cl].get("points", None) is None else clusters[cl]["points"]

		print("---------------\nEPOCH #{0} : \n".format(epoch))

		if epoch > 1:
			print("\nFinding a new representative : \n")
			n_repr = np.random.randint(0, no)

			cents = [clusters[cl]["center"] for cl in clusters]
			while points[n_repr] in cents:
				n_repr = np.random.randint(0, no)

			str_repr = chr(s_no + n_repr)
			target_cl = None

			for cl in clusters:
				if str_repr in clusters[cl]["points"]:
					target_cl = cl
					break

			clusters[target_cl]["center"] = points[n_repr]

			print("!!! New representative {0} belongs to Cluster #{1}. Replacing C{2} by {3} !!!\n".format(str(points[n_repr]), target_cl, target_cl, str(points[n_repr])))

		for cl in clusters:
			clusters[cl]["points"] = []

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
			new_cost = new_cost + min_d

			print("\nPoint {0} belongs to Cluster {1}\n".format(chr(s_no + ind), n_cl))

		print("\nCost : {0}".format(new_cost))
		
		if new_cost < old_cost:
			old_cost = new_cost
			print("\n!!! New representative gives better result. Sticking with it !!!\n")
		else:
			clusters = stable_clusters.copy()
			print("\n!!! New representative is worse! Aborting !!!\n")
			break


		# print("New Cluster centers : ")
		# for cl in sorted(clusters.keys()):
		# 	clusters[cl]["center"] = list(np.average([points[ord(p)-s_no] for p in clusters[cl]["points"]], 0))
		# 	print("C{0} = Mean of ({1}) = ({2})".format(cl, ', '.join(clusters[cl]["points"]), ' '.join(list(map(str, clusters[cl]["center"])))))

		print("\nAt the end of the epoch : " + str(clusters) + "\n")
		# print(stable_clusters)

		if stable_clusters == clusters:
			print("\n!!! No change since the last epoch !!!\n")
			change = False
		
		epoch = epoch + 1

	print("\n----------------\nAns : " + str(clusters) + "\n----------------\n")
