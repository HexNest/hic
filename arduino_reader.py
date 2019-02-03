import warnings
import serial
import serial.tools.list_ports

# list of ports that have an arduino connected to them
arduino_ports = [p.device for p in serial.tools.list_ports.comports() if 'Arduino' in p.description]

# error messaging if there is not exactly one arduino connected
if not arduino_ports:
    raise IOError('No Arduino found')
if len(arduino_ports) > 1:
    warnings.warn('Multiple Arduinos found - using the first')

# open a stream from the serial port connected to the arduino
ser = serial.Serial(arduino_ports[0])

# ask the user to enter a filename to save in
filename = input('Enter a file name to save data from: ')
lines = []
print('Press CTRL-C to finish reading a save to the file.')

while True:
    try:
        # put newline into a
        line.append(ser.readline())
    except KeyboardInterrupt:
        # if the user presses CTRL-C just break out of the loop
        break
    
with(open(filename, 'w+')) as f:
    for line in lines:
        f.write(line)

print('Finished writing contents to file.')