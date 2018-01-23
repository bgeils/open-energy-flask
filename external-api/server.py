import json
from flask import Flask, request, redirect

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
                         power=data['power'])
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
                         power=data['power'])
    if ret.acknowledged:
        return json.dumps({'success': True}), 200, {'ContentType': 'application/json'}
    else:
        return "Please check your request", 400

@app.route("/petition", methods=['POST'])
def pet():
    name = request.form['name']
    email = request.form['email']
    zipcode = request.form['zipcode']
    insert_petition(name, email, zipcode)
    return redirect("http://isuenergy.com/thanks", code=302)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
