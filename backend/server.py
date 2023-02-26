from flask import Flask, request, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

waterData = {
  'progress': '0',
  'totalDrank': '0',
  'intakeGoal': '800',
  'bottleSize': '100'
}

# @app.route('/drank',methods=['POST'])
# def changeLevel():
#     print(request)
#     data = request.get_json() # get the json from the post request object
#     print(data["drank"])
#     waterData['drank'] = data["drank"]
#     return jsonify(waterData) # for the browser to understand that waterData was changed

#get waterData
@app.route('/data')
def get_data():
  return jsonify(waterData)

# @app.route('/progress', methods=['POST'])
# def changeProgress():
#   data = request.get_json()
#   waterData['progress'] = data['progress']
#   return jsonify(waterData)

#change intakeGoal
@app.route('/intakeGoal', methods=['POST'])
def changeIntake():
  data = request.get_json()
  waterData['intakeGoal'] = data['intake']
  return jsonify(waterData)

#get values from water sensor and calculated how much user drank from bottle, and change progress
@app.route('/sensor', methods=['POST'])
def sendSensorData():
  data = request.get_json()
  reading = float(data['mLChanged'])
  print("Reading:",reading)
  totalDrankVal = float(waterData["totalDrank"]) + reading
  waterData["totalDrank"] = totalDrankVal
  waterData["progress"] = int(totalDrankVal/(int(waterData["intakeGoal"]))*100)
  return jsonify(waterData)

#change bottle size
@app.route('/bottle', methods=['POST'])
def changeBottleSize():
  data = request.get_json()
  waterData['bottleSize'] = data['bottleSize']
  return jsonify(waterData)
  
 
@app.route("/")
def showHomePage():
    return "This is home page"

if __name__ == "__main__":
  app.run(host="0.0.0.0", port="3400")
