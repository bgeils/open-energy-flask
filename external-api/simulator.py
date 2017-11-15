'''
Simulates a home that is consuming energy
'''
import requests, string
import datetime, time
import random

random_device_id = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(16))

def consume_energy(power_range, device_id=random_device_id):
    '''
    Consume energy each time the unit is called.
    :param energy_range: tuple, range to consume energy in watts
    :return:
    '''
    rand_power = random.randrange(power_range[0], power_range[1])

    data = {
        "device_id" : device_id,
        "start_time" : str(datetime.datetime.utcnow()),
        "duration" : 15,
        "power" : rand_power
    }
    print(data)
    r = requests.post('http://localhost:5000/insert_consum_data', json=data)
    return r.status_code

def produce_energy(energy_range):
    '''
    Simulate a device producing energy
    :param energy_range:
    :return:
    '''
    # TODO

if __name__ == "__main__":
    print('starting simulator.')
    '''
    Use the following device_id for testing:
    4NH5SOZMPNIDR7FK
    consume_energy(consume_range, device_id=4NH5SOZMPNIDR7FK)
    '''

    consume_range = (1000,1500) # watts to consume

    try:
        while True:
            consume_energy(consume_range)
            time.sleep(3)
    except KeyboardInterrupt:
        print('simulator exited!')
