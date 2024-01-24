# proximity.py

import serial
import time

ser = serial.Serial("COM3", 9600)
command = b'\x01\x04\x03\xE9\x00\x01\xE0\x7A'
print('test program')

tstart = time.perf_counter()

def read_proximity_sensor():
    ser.flush()
    ser.write(command)
    readHEX = ser.read(7).hex()
    print(readHEX)

    if len(readHEX) > 7:
        data = (readHEX[6] + readHEX[7] + readHEX[8] + readHEX[9])
        rpm_value = int(data, 16)
        return rpm_value

# Run the code continuously
while True:
    tcurr = time.perf_counter() - tstart
    # Every 1s
    if tcurr > 1:
        rpm_value = read_proximity_sensor()
        print(rpm_value)

        tstart = time.perf_counter()
