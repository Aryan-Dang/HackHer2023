import serial
import time
import requests
import datetime

ser = serial.Serial('/dev/cu.usbmodem142101',9600)

K = 5
queue = [0 for i in range(K)]
qIndex = 0

def getRunningAverage():
  avg = 0
  for i in range(K):
    avg += queue[i]
  return avg/K

def getCurrentAvgReading():
    global qIndex
    print("#########")
    curReading = int(ser.readline())
    queue[qIndex%K] = curReading
    qIndex += 1
    print(getRunningAverage())
    return getRunningAverage()

while True:
    avg1 = getCurrentAvgReading()
    time.sleep(1)
    avg2 = getCurrentAvgReading()
    if(abs(avg1 - avg2) > 2):
      response = requests.post('http://localhost:3400/sensor', json={
        'mLChanged': str(1.6 * abs(avg1 - avg2))
      })

ser.close()