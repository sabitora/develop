#import
import serial
import time

#kansu
val_size = 4
values = [0 for x in range(val_size)]
isValids = [False for x in range(val_size)]
ser = serial.Serial('/dev/ttyACM0',9600,timeout = 0.1)

while True:
    headByte = ser.read()
    head = int.from_bytes(headByte, 'big')
    if head == 128:
        isValids = [False for x in range(val_size)]

    for i in range(val_size):
        if head == 128+i:
            highByte = ser.read()
            lowByte = ser.read()
            high = int.from_bytes(highByte, 'big')
            low = int.from_bytes(lowByte, 'big')
            values[i] = (high<<7) + low
            if 0 <= values[i] and values[i] <= 1023:
                isValids[i] = True

    if all(i == True for i in isValids):
        tp = values[0]/10
        rh = values[1]/10
        ir = values[2]/10
        co2ppm = values[3]/10

        print(tp,rh,ir,co2ppm)
