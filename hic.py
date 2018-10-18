def hic():
	f = open('raw.txt')
	lst = []
	lst = f.readlines()	
	f.close()
	#bigboy = []
	#hics = []
	lst = lst[100:-100]
	lst = list(map(lambda x : float(x.split()[1]), lst))

	lst = list(map(lambda x : abs(x+4), lst))

	max_hic = 0
	max_hic_start = -1
	max_hic_end = -1
	for start in range(len(lst)):
	  for end in range(start + 15, min(len(lst), start + 25)):
	    avg = sum(lst[start : end + 1]) / float(   1  *  len(lst[start : end + 1]))
	    t = (len(lst[start : end + 1])) * 0.001
	    hic_test = t * ((avg) ** 2.5)
	    #bigboy.append(hic_test)
	    if hic_test > max_hic:
	      max_hic = hic_test
	      max_hic_start = start
	      max_hic_end = end

	print("Max HIC: ", max_hic)
	print("Start:", max_hic_start)
	print("End:", max_hic_end)
	print(lst[max_hic_start:max_hic_end])
	import matplotlib.pyplot as plt
	#for a in range(len(bigboy)):
	#  hics.append(a)


	#plt.plot(hics,bigboy)
	#plt.show()

	return max_hic
hic()

