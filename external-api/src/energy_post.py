import pymongo
import datetime

client = pymongo.MongoClient("mongodb://bubbles:ybQWqmc97zHnrBYxKZLeghrNM44h@\
ec2-35-167-132-139.us-west-2.compute.amazonaws.com:27017/production")

db = client.production

def insert_prod_data(device_id, start_time, duration, energy):
    '''
    :param device_id: unique id of the device
    :param start_time: start time for the device
    :param duration: time in seconds
    :param energy: amount of energy during the duration in watt-hours
    :return: true or false
    '''

    return db.prod.insert_one({
        "device_id": device_id,
        "start_time": start_time,
        "duration": duration,
        "energy": energy
         })

def insert_consum_data(device_id, start_time, duration, energy):
    '''
    :param device_id: unique id of the device
    :param start_time: start time for the device
    :param duration: time in seconds
    :param energy: amount of energy during the duration in watt-hours
    :return: true or false
    '''

    # 2017-11-06 14:32:57.935540
    date_format = "%Y-%m-%d %H:%M:%S.%f"
    start_time = datetime.datetime.strptime(start_time, date_format)

    return db.consum.insert_one({
        "device_id": device_id,
        "start_time": start_time,
        "duration": duration,
        "energy": energy
         })

if __name__ == "__main__":
    pass