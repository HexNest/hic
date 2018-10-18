def hic(interval_length, calibration = 4):
	f = open('raw.txt')
	lines = f.readlines()
	f.close()

	# get rid of bad data
	lines = lines[100:-100]

	time_stamps = list(map(lambda x : float(x.split()[0]), lines))
	accelerations = list(map(lambda x : float(x.split()[1]), lines))
	
	# adjust accelerations based on calibration
	accelerations = list(map(lambda x : abs(x + calibration), accelerations))

	max_hic = 0
	max_hic_start_index = -1
	max_hic_end_index = -1

	for start_index in range(len(time_stamps) - interval_length):
		start_timestamp = time_stamps[start_index]
		end_index = start_index + 1

		while time_stamps[end_index] - start_timestamp < interval_length:
			end_index += 1

		sum_of_acceleration = sum(accelerations[start_index : end_index + 1])
		avg_acceleration = sum_of_acceleration / float(end_index - start_index + 1)
		time_elapsed = (time_stamps[end_index] - time_stamps[start_index]) * 0.001

		hic_value = time_elapsed * (avg_acceleration ** 2.5)

		if hic_value > max_hic:
			max_hic = hic_value
			max_hic_start_index = start_index
			max_hic_end_index = end_index

	print("Max HIC: ", max_hic)
	print("Start:", time_stamps[max_hic_start_index])
	print("End:", time_stamps[max_hic_end_index])
	print(accelerations[max_hic_start_index : max_hic_end_index + 1])

	import matplotlib.pyplot as plt

	plt.plot(time_stamps, accelerations)
	plt.show()

	return max_hic

hic(15)