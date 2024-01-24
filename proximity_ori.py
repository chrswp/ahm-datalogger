import serial
import time

ser = serial.Serial("COM3", 9600)
command = b'\x01\x04\x03\xE9\x00\x01\xE0\x7A'
print('test program')

tstart = time.perf_counter()

while True:

    tcurr = time.perf_counter() - tstart
    # Every 1s
    if tcurr > 1:
        ser.flush()
        ser.write(command)
        readHEX = ser.read(7).hex()
        print(readHEX)

        if len(readHEX) > 7:
            # print ('Lenght Data OK')
            data = (readHEX[6] + readHEX[7] + readHEX[8] + readHEX[9])
            # print(data)
            rpm_value = int(data, 16)
            print(rpm_value)

        tstart = time.perf_counter()





