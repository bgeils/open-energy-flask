from flask import Flask, request
import json

app = Flask(__name__)

from src.energy_post import *

@app.route("/")
def hello():
    return "<h1 style='color:blue'>Arun listens to Nickleback...</h1>"

@app.route("/insert_prod_data", methods=['POST'])
def prod():
    print('Recieved from client: {}'.format(request.json))
    data = request.json
    ret = insert_prod_data(device_id=data['device_id'],
                         start_time=data['start_time'],
                         duration=data['duration'],
                         energy=data['energy'])
    if ret.acknowledged:
        return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}
    else:
        return "Please check your request", 400

@app.route("/insert_consum_data", methods=['POST'])
def consum():
    print('Recieved from client: {}'.format(request.json))
    data = request.json
    ret = insert_consum_data(device_id=data['device_id'],
                         start_time=data['start_time'],
                         duration=data['duration'],
                         energy=data['energy'])
    if ret.acknowledged:
        return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}
    else:
        return "Please check your request", 400

if __name__ == "__main__":
    app.run(host='0.0.0.0')
