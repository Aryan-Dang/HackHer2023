import serial
import time
import requests
import datetime

ser = serial.Serial('/dev/cu.usbmodem141101',9600)

K = 5
queue = [0 for i in range(K)]
qIndex = 0

def getRunningAverage():
  avg = 0
  for i in range(K):
    avg += queue[i]
  return avg/K

def getCurrentAvgReading():
    print("#########")
    curReading = int(ser.readline())
    queue[qIndex%K] = curReading
    qIndex += 1

    print(getRunningAverage())

while True:
    avg1 = getCurrentAvgReading()
    time.sleep(1)
    avg2 = getCurrentAvgReading()
    if(abs(avg1 - avg2) > 2):
      response = requests.post('http://127.0.0.1:5000/sensor', json={
        'sensorReading': str(avg2)
      })

ser.close()