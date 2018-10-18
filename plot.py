import matplotlib.pyplot as plt

def plot_data():
	t = []
	a = []

	f = open('raw.txt')
	lst = f.readlines()
	lst = lst[100:-100]

	for line in lst:
	    temp = tuple(map(float, line.split()))
	    t.append(temp[0])
	    a.append(temp[1] + 0)
	f.close()
	t = t[20:-20]
	a = a[20:-20]

	plt.plot(t, a)
	plt.show()