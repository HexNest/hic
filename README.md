# HIC Data Collector and Plotter

## Setup
1. Install Python 3+
2. Navigate to this directory with your command prompt
3. Run `pip install -r requirements.txt`
4. If step 3 fails, run `pip install X` where X is each line in requirements.txt (should be matplotlib and pyserial)

## Running
1. Connect the Arduino to your laptop via the USB port
2. Open the Arduino IDE and open the `arduino.ino` file
3. Run the file to put it on the Arduino
4. Run `python3 arduino_reader.py`
5. Enter a file name
6. Run your test
7. Press CTRL+C in your command line to stop collecting data and save it to the file.
8. To view the file as a plot, run `python3 hic.py` and enter the file name that you want to plot
