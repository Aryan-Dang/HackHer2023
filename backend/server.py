from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

waterData = {
  'waterLevel': '0',
  'progress': '0',
  'dailyIntake': '3L'
}

#route for changing the level of water
@app.route('/level',methods=['POST'])  
def changeLevel():
    print(request)
    data = request.get_json() # get the json from the post request object
    print(data["level"])
    waterData['waterLevel'] = data["level"]
    return jsonify(waterData) # for the browser to understand that waterData was changed

@app.route('/data')
def get_data():
  return jsonify(waterData)

@app.route('/progress', methods=['POST'])
def changeProgress():
  data = request.get_json()
  waterData['progress'] = data['progress']
  return jsonify(waterData)

@app.route('/intake', methods=['POST'])
def changeIntake():
  data = request.get_json()
  waterData['dailyIntake'] = data['intake']
  return jsonify(waterData)

@app.route('/sensor', methods=['POST'])
def sendSensorData():
  data = request.get_json()
  reading = float(data['sensorReading'])
  #130 max, 46 low
  if reading <= 46.0 and reading > 0:
    data['progress'] = '25'
  elif reading > 46.0 and reading <= 88.0:
    data['progress'] = '50'
  elif reading > 88 and reading < 110:
    data['progress'] = '100'
  return jsonify(waterData)
 
@app.route("/")
def showHomePage():
    return "This is home page"

if __name__ == "__main__":
  app.run(host="0.0.0.0", port="3400")