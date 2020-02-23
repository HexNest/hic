import matplotlib.pyplot as plt

def hic(filename, interval_length, calibration = 4):
	with open(filename) as f:
		lines = f.readlines()

	# get rid of bad data
	lines = lines[100:-100]

	# each data point comes in the following form: time_stamp_ms, acceleration
	time_stamps = list(map(lambda x : float(x.split(',')[0]), lines))
	accelerations = list(map(lambda x : float(x.split(',')[1]), lines))

	print(time_stamps)
	
	# adjust accelerations based on calibration
	accelerations = list(map(lambda x : abs(x + calibration), accelerations))

	max_hic = 0
	max_hic_start_index = -1
	max_hic_end_index = -1

	for start_index in range(len(time_stamps) - 1):
		start_timestamp = time_stamps[start_index]
		end_index = start_index + 1

		# move the end index forward until we reach the desired interval length
		while time_stamps[end_index] - start_timestamp < interval_length:
			end_index += 1

			# if the interval length goes off the end, then go back 1 and stop adding to end_index
			if end_index >= len(time_stamps):
				end_index -= 1
				break

		sum_of_acceleration = sum(accelerations[start_index : end_index + 1])
		avg_acceleration = sum_of_acceleration / float(end_index - start_index + 1)
		# multiply by 0.001 to make convert from milliseconds to seconds
		time_elapsed = (time_stamps[end_index] - time_stamps[start_index]) * 0.001

		hic_value = time_elapsed * (avg_acceleration ** 2.5)

		# if the current hic_value > max_hic, replace it
		if hic_value > max_hic:
			max_hic = hic_value
			max_hic_start_index = start_index
			max_hic_end_index = end_index

	print("Max HIC: ", max_hic)
	print("Start Timestamp(ms):", time_stamps[max_hic_start_index])
	print("End Timestamp(ms):", time_stamps[max_hic_end_index])
	print(accelerations[max_hic_start_index : max_hic_end_index + 1])

	plt.plot(time_stamps, accelerations)
	plt.show()

	return max_hic

filename = input("Please enter the name of the file you'd like to read: ")
hic(filename, interval_length = 15, calibration = 4)
