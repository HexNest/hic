# HIC Data Collector and Plotter

## Setup
1. Install Python 3+
2. Navigate to this directory with your command prompt
3. Run `pip install -r requirements.txt`
4. If step 3 fails, run `pip install X` where X is each line in requirements.txt (should be matplotlib and pyserial)

## Running
When you want to collect data from the Arduino, you should connect the arduino to your laptop and then run `python3 arduino_reader.py`. This should ask you for a filename where you want to save the data. Once you enter a filename, it will start reading from the arduino. Press CTRL-C in your terminal to stop it and save the data to a file.

When you are done and want to plot it and calculate the HIC, run `python3 hic.py` and then enter the file name that you want to plot.