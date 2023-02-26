import serial
import time
import requests
import datetime

ser = serial.Serial('/dev/cu.usbmodem141101',9600)

K = 5
queue = [0 for i in range(K)]
qIndex = 0

def getRunningAverage():
  avg = 0;
  for i in range(K):
    avg += queue[i];
  return avg/K;

while True:
    print("#########")
    curReading = int(ser.readline())
    queue[qIndex%K] = curReading
    qIndex += 1
    print(getRunningAverage())

ser.close()