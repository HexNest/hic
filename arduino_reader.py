import warnings
import serial
import serial.tools.list_ports
import re
import io

# list of ports that have an arduino connected to them

all_ports = [p for p in serial.tools.list_ports.comports()]
print("Enter a number:")
for i in range(len(all_ports)):
    print(str(i) + " for " + all_ports[i].device)
index = int(input())
#arduino_ports = [p.device for p in serial.tools.list_ports.comports() if 'Arduino' in p.description]

addr  = all_ports[index].device
baud  = 115200
fname = input('Enter a file name to save data from: ')
lines = []

print(addr)

with serial.Serial(addr, baud) as pt:
    spb = io.TextIOWrapper(io.BufferedRWPair(pt,pt,1),
        encoding='ascii', errors='ignore', newline='\n',line_buffering=True)
    spb.readline()  # throw away first line; likely to start mid-sentence (incomplete)
    while (True):
        try:
            line = spb.readline()
            lines.append(line)  # read one line of text from serial port
        except KeyboardInterrupt:
            break
    
with(open(fname, 'w+')) as f:
    f.writelines(lines)

print('Finished writing contents to file.')
