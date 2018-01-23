import pymongo
import datetime
import pkg_resources

import json

with open('../../settings.json', 'r') as f:
    config = json.load(f)

client = pymongo.MongoClient(config['mongo_uri'])

db = client.production

def insert_prod_data(device_id, start_time, duration, power):
    '''
    :param device_id: unique id of the device
    :param start_time: start time for the device
    :param duration: time in seconds
    :param power: amount of power during the duration in watt-hours
    :return: true or false
    '''

    return db.prod.insert_one({
        "device_id": device_id,
        "start_time": start_time,
        "duration": duration,
        "power": power
         })

def insert_consum_data(device_id, start_time, duration, power):
    '''
    :param device_id: unique id of the device
    :param start_time: start time for the device
    :param duration: time in seconds
    :param power: amount of power during the duration in watt-hours
    :return: true or false
    '''

    # 2017-11-06 14:32:57.935540
    date_format = "%Y-%m-%d %H:%M:%S.%f"
    start_time = datetime.datetime.strptime(start_time, date_format)

    return db.consum.insert_one({
        "device_id": device_id,
        "start_time": start_time,
        "duration": duration,
        "power": power
         })

def insert_petition(name, email, zipcode):
    return db.petition.insert_one({'name': name, 'email': email, 'zipcode': zipcode})


if __name__ == "__main__":
    pass