import os
import requests
import time
import paho.mqtt.client as paho
from dotenv import find_dotenv, load_dotenv
from paho import mqtt


def on_connect(client, userdata, flags, rc, properties=None):
    print("CONNACK received with code %s." % rc)

def on_publish(client, userdata, mid, properties=None):
    print("mid: " + str(mid))

def on_subscribe(client, userdata, mid, granted_qos, properties=None):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))

def on_message(client, userdata, msg):
    print("Received a message from the " + msg.topic + " topic\n" + "QOS Level " + str(msg.qos) + "\n" + "Message: " + str(msg.payload))


# # url1 = 'https://gnurr6dmoi.execute-api.eu-west-1.amazonaws.com/v1/rooms/e472d5c7-6c35-455e-ac59-1c99ef20c7e5/items/metadata?'

# site_uuids = {
#     # 'ADC CPT 1.1':'48abd69d-c099-4b7b-a1fa-43015bb3fdbe',
#     # 'ADC CPT 1.2':'75187c5a-af2e-49a5-963e-0bbea569e9e7',
#     # 'ADC CPT 1.3,1.5,1.6':'7ffd53a5-b6d8-4c9e-a505-6888383d2633',
#     # 'ADC CPT 1.4':'0267dbe7-21e1-446d-92f8-673b399c1557',
#     'ADC JHB 1.1-1.3':'a1a63f93-67b5-4568-a44b-07c340adca2b',
#     # 'ADC JHB 1.4':'59163e96-4cb9-4b3a-b967-ed16cff5a641',
#     # 'ADC JHB 1.5-1.8':'d1c03734-9f41-4a5a-84d7-ba55a889d4f7',
#     # 'ADC JHB 2':'37cc79f6-d2e4-4106-b325-3224d2802f08',
#     # 'ADC LOS 1':'33aa9716-e3c9-4196-87e7-920688bd9870',
#     # 'ADC NBO 1':'9ee69e93-6db8-494e-a312-6c7e9c66c3ce'
# }

# site_numbers = {
#     # 0:'ADC CPT 1.1',
#     # 1:'ADC CPT 1.2',
#     2:'ADC JHB 1.1-1.3',   
#     # 3:'ADC JHB 1.4',
#     # 4:'ADC JHB 1.5-1.8',
#     # 5:'ADC JHB 2',
#     # 6:'ADC LOS 1',
#     # 7:'ADC NBO 1',
#     # 8:'ADC CPT 1.4',
#     # 9:'ADC CPT 1.3,1.5,1.6'    
# }

colour_codes = [
    '#000080',
    '#0101FB',
    '#33C4F2',
    '#94CA53',
    '#F3EC19',
    '#FEC00F',
    '#ED1F24'
]

def get_items(url):
    dotenv_path = find_dotenv()
    load_dotenv(dotenv_path)

    key = os.getenv('API_KEY')

    headers = {
        'x-api-key': key
    }

    try:
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            items = response.json()
            return items
        else:
            print('Error:', response.status_code)
            return None
    except requests.exceptions.RequestException as e:
        print('Error:', e)
        return None

item_uuids = [
    '89fed435-80ea-4b12-8246-54dab938ff9b',
    '5c9f6c04-56a4-455a-b6fa-f32d519d42de',
    'd59186c0-0563-445b-8176-9a6f805c5b75',
    'e8027939-90e8-4794-ae93-7afb901c3c63',
    '08a3b4f3-a006-4153-b07e-f354efd76b24',
    '2da90c70-2dfc-4743-97f6-f90574a792d2',
    'd11748b0-b866-4f11-89a3-e1d389b6b230',
    '24a68fc7-9df2-4694-bf11-ea3a5e317b97',
    'e1c00d3d-c4cd-4b68-9408-a0333108d849'
]
room_uuid = 'ee47fba3-b715-434e-ba78-d7b962483e8c'

def main(item_uuids, room_uuid):
    results_list = []
    
    for i in range(0,9):
        readings_url = 'https://gnurr6dmoi.execute-api.eu-west-1.amazonaws.com/v1/items/' + item_uuids[i] + '/readings?'
        readings = get_items(readings_url)

        if readings:
            item_list_url = 'https://gnurr6dmoi.execute-api.eu-west-1.amazonaws.com/v1/rooms/' + room_uuid +'/items/metadata'
            items = get_items(item_list_url)
            for item in items:
                
                if item['itemUuid'] == item_uuids[i]:
                    name = item['data']['label']
                    temperature = round(readings[0]['data']['inletTemperature']['average'], 1)
                    if temperature < 18:
                        colour = colour_codes[0]
                        results_list.append(f'Rack {name} - Temperature: {temperature} \N{DEGREE sign}C; HEX Colour Code: {colour}')
                    elif temperature >= 18 and temperature <= 21:
                        colour = colour_codes[1]
                        results_list.append(f'Rack {name} - Temperature: {temperature} \N{DEGREE sign}C; HEX Colour Code: {colour}')
                    elif temperature > 21 and temperature <= 23:
                        colour = colour_codes[2]
                        results_list.append(f'Rack {name} - Temperature: {temperature} \N{DEGREE sign}C; HEX Colour Code: {colour}')
                    elif temperature > 23 and temperature <= 25:
                        colour = colour_codes[3]
                        results_list.append(f'Rack {name} - Temperature: {temperature} \N{DEGREE sign}C; HEX Colour Code: {colour}')
                    elif temperature > 25 and temperature <= 27:
                        colour = colour_codes[4]
                        results_list.append(f'Rack {name} - Temperature: {temperature} \N{DEGREE sign}C; HEX Colour Code: {colour}')
                    elif temperature > 27 and temperature <= 30:
                        colour = colour_codes[5]
                        results_list.append(f'Rack {name} - Temperature: {temperature} \N{DEGREE sign}C; HEX Colour Code: {colour}')
                    else:
                        colour = colour_codes[6]
                        results_list.append(f'Rack {name} - Temperature: {temperature} \N{DEGREE sign}C; HEX Colour Code: {colour}')
        else:
            results_list.append('There are no available readings for this rack.')

    output = ' | '.join(results_list)
    
    client = paho.Client(client_id="", userdata=None, protocol=paho.MQTTv5)
    client.on_connect = on_connect

    client.tls_set(tls_version=mqtt.client.ssl.PROTOCOL_TLS)

    username = os.getenv('HIVE_USERNAME');
    password = os.getenv('HIVE_PASSWORD');
    
    client.username_pw_set(username, password)

    client.connect("4e7484bd490942099996a545d81d84ef.s1.eu.hivemq.cloud", 8883)

    client.on_subscribe = on_subscribe
    client.on_message = on_message
    client.on_publish = on_publish

    client.subscribe("temperature_request/#", qos=1)
    
    client.publish("temperature_request/api_call", payload=output, qos=1)
    
    client.loop_forever()
    
    return output

    # print(site_uuids.keys().__contains__('ADC CPT 1.1'))
    # uuid = site_uuids[site_numbers[2]]
    # rooms_url = f'https://gnurr6dmoi.execute-api.eu-west-1.amazonaws.com/v1/sites/a1a63f93-67b5-4568-a44b-07c340adca2b/rooms/metadata'
    # rooms = get_items(rooms_url)
    
    # if rooms:
    #         for room in rooms:
    #             # items_url = f'https://gnurr6dmoi.execute-api.eu-west-1.amazonaws.com/v1/rooms/' + \
    #             #     room['roomUuid'] + '/items/metadata'
    #             item_url = f'https://gnurr6dmoi.execute-api.eu-west-1.amazonaws.com/v1/rooms/3b0ef5f0-b51d-46d1-a487-a306936391c9/items/metadata'
    #             items = get_items(item_url)
    #             print()
    #             if items:
    #                     readings_url = 'https://gnurr6dmoi.execute-api.eu-west-1.amazonaws.com/v1/items/d8f58c6b-45e3-4062-a91e-8aaa19c0d2b2/readings?'
    #                     readings = get_items(readings_url)
    #                     if len(readings) != 0 and readings[0]['data'].keys().__contains__('inletTemperature'):
    #                         room_name = room['data']['label']
    #                         name = items['data']['label']
    #                         temperature = round(readings[0]['data']['inletTemperature']['average'], 1)
    #                         humidity = round(readings[0]['data']['inletRh']['average'],1)
    #                         print(f'{room_name} | Rack {name} - Temperature: {temperature} \N{DEGREE sign}C; Humidity {humidity}%')

    #             if items:
    #                 for item in items:
    #                     readings_url = 'https://gnurr6dmoi.execute-api.eu-west-1.amazonaws.com/v1/items/' + \
    #                         item['itemUuid'] + '/readings?'
    #                     if item['data']['object'] == 'Standard Server Rack':
    #                         readings = get_items(readings_url)
    #                         # if readings:
    #                         if len(readings) != 0 and readings[0]['data'].keys().__contains__('inletTemperature'):
    #                                 room_name = room['data']['label']
    #                                 item_uuid = item['itemUuid']
    #                                 name = item['data']['label']
    #                                 temperature = round(
    #                                     readings[0]['data']['inletTemperature']['average'], 1)
    #                                 # humidity = round(readings[0]['data']['inletRh']['average'],1)
    #                                 print(
    #                                     f'{room_name} | Rack {name} - Temperature: {temperature} \N{DEGREE sign}C;')
    #                         # else:
    #                         #     print('Failed to fetch readings from API. Search for: ' + item_uuid)    
    #                     elif item['data']['object'] == 'Server Rack':
    #                         readings = get_items(readings_url)
    #                         # if readings:
    #                         if len(readings) != 0 and readings[0]['data'].keys().__contains__('inletTemperature'):
    #                                 room_name = room['data']['label']
    #                                 item_uuid = item['itemUuid']
    #                                 name = item['data']['label']
    #                                 temperature = round(
    #                                     readings[0]['data']['inletTemperature']['average'], 1)
    #                                 #humidity = round(readings[0]['data']['inletRh']['average'],1)
    #                                 print(
    #                                     f'{room_name} | Rack {name} - Temperature: {temperature} \N{DEGREE sign}C;')
    #                         # else:
    #                         #     print('Failed to fetch readings from API. Search for: ' + item_uuid)
    #             else:
    #                 print('Failed to fetch items from API.')
    # else:
    #     print('Failed to fetch rooms from API.')


if __name__ == '__main__':
    main(item_uuids, room_uuid)
