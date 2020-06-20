import numpy as np

if __name__ == '__main__':
	no = int(input("Eneer the number of points : "))
	print("Enter the points : ")

	points = []
	for i in range(no):
		points.append(list(map(float, input().split())))

	mean_x = sum(np.array(points)[:, 0]) / no
	mean_y = sum(np.array(points)[:, 1]) / no

	print("\n================\nSolution :- \n================\n")

	print("m(x) = {0}, m(y) = {1}".format(mean_x, mean_y))
	print()

	stat_calc = ["x", "y", "xy", "x-m(x)", "y-m(y)", "(x-m(x))^2", "(y-m(y))^2", "(x-m(x))(y-m(y))"]

	for stat in stat_calc:
		print("%20s" % (stat))

	mean_dev_x, mean_dev_y, sq_mean_dev_x, sq_mean_dev_y, mult_mean_dev, mult = [], [], [], [], [], []

	for ind, (x, y) in enumerate(points):
		mult.append(x*y)
		mean_dev_x.append(x-mean_x)
		mean_dev_y.append(y-mean_y)
		sq_mean_dev_x.append((x-mean_x)**2)
		sq_mean_dev_y.append((y-mean_y)**2)
		mult_mean_dev.append((x-mean_x)*(y-mean_y))

		print("%10.2f%10.2f%10.2f%10.2f%10.2f%10.2f%10.2f%10.2f" % (x, y, mult[ind], mean_dev_x[ind], mean_dev_y[ind], sq_mean_dev_x[ind], sq_mean_dev_y[ind], mult_mean_dev[ind]))

	for i in range(80):
		print("-", end='')

	print()
	print("%10.2f%10.2f%10.2f%10.2f%10.2f%10.2f%10.2f%10.2f" % (sum(np.array(points)[:, 0]), sum(np.array(points)[:, 1]), sum(mult), sum(mean_dev_x), sum(mean_dev_y), sum(sq_mean_dev_x), sum(sq_mean_dev_y), sum(mult_mean_dev)))

	print("\n### Statistical Measures ###\n")
	
	var_x, var_y = sum(sq_mean_dev_x) / no, sum(sq_mean_dev_y) / no
	print("VAR(x) =", var_x)
	print("VAR(y) =", var_y)
	print()

	sd_x, sd_y = var_x**0.5, var_y**0.5
	print("SD(x) =", sd_x)
	print("SD(y) =", sd_y)
	print()

	cov_xy = sum(mult_mean_dev) / no
	print("COV(x,y) =", cov_xy)
	print("COV(x,y) [Another Method] =", (sum(mult)/no - mean_x*mean_y))
	print()

	r_xy = cov_xy / (sd_x*sd_y)
	print("CORRELATION(x,y) =", r_xy)
	print()

	print("\n### LINEAR REGRESSION ###\n")

	print("Say, line : y = ax + b\n")
	a = (r_xy * sd_y) / sd_x
	b = mean_y - a*mean_x
	print("a = {0}, b = {1}".format(a, b))

	print("\nSay, line : x = ay + b\n")
	a = (r_xy * sd_x) / sd_y
	b = mean_x - a*mean_y
	print("a = {0}, b = {1}".format(a, b))

	print()