import os
import requests
import paho.mqtt.client as paho
from django.core.cache.backends.filebased import FileBasedCache
from dotenv import find_dotenv, load_dotenv

def on_connect(client, userdata, flags, rc, properties=None):
    if rc == 0:
        print("CONNACK received with code %s." % rc)
    else:
        print(f"Bad connection. Returned Code = {rc}")

colour_codes = {
    'Navy': [80, 0, 205],
    'Blue': [0, 0, 255],
    'Deep Sky Blue': [0, 255, 255],
    'Pastel Green': [124, 252, 0],
    'Lemon': [255, 155, 0],
    'Amber': [255, 69, 0],
    'Transport Red': [255, 0, 0]
}

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

item_uuids = ''
room_uuid = ''
cache = FileBasedCache('C:\\Users\\TalifhaniNetshiheni\\Desktop\\Django\\Temp-Request-Repo\\Temperature-Request-App\\django_cache', {})

def cache_rack_data(key, red, green, blue, start_pixel, end_pixel):
    data = [red, green, blue, start_pixel, end_pixel]
    cache.set(key, data)  # Store in cache

# Accessing data, which might be cachedd

def main(item_uuids, room_uuid):
    
    uuid_list = item_uuids.split()
    results_list = []
    red = 0
    green = 0
    blue = 0
    num_pixel = 1
    start_pixel = 0
    end_pixel = num_pixel
    messageList = []
    results_list.__contains__

    for uuid in uuid_list:
        if uuid:
            readings_url = 'https://gnurr6dmoi.execute-api.eu-west-1.amazonaws.com/v1/items/' + uuid + '/readings?'
            readings = get_items(readings_url)

            if readings:
                item_list_url = 'https://gnurr6dmoi.execute-api.eu-west-1.amazonaws.com/v1/rooms/' + room_uuid +'/items/metadata'
                items = get_items(item_list_url)
                for item in items:
                    
                    if item['itemUuid'] == uuid:
                        name = item['data']['label']
                        temperature = round(readings[0]['data']['inletTemperature']['average'], 1)
                        if temperature < 18:
                            colour = colour_codes['Navy']
                            red = colour[0]
                            green = colour[1]
                            blue = colour[2]
                            
                            if uuid in cache:
                                if cache.get(uuid)[0] == red and cache.get(uuid)[1] == green and cache.get(uuid)[2] == blue:
                                    results_list.append(f'Rack {name} - Temperature: {temperature} \N{DEGREE sign}C; Colour: Navy')
                                    break
                                else:
                                    cache_rack_data(uuid, red, green, blue, start_pixel, end_pixel)
                                    results_list.append(f'Rack {name} - Temperature: {temperature} \N{DEGREE sign}C; Colour: Navy')
                                    messageList.append(f'{red},{blue},{green},{start_pixel},{end_pixel}')
                            else:
                                cache_rack_data(uuid, red, green, blue, start_pixel, end_pixel)
                                results_list.append(f'Rack {name} - Temperature: {temperature} \N{DEGREE sign}C; Colour: Navy')
                                messageList.append(f'{red},{blue},{green},{start_pixel},{end_pixel}')
                                
                            
                        elif temperature >= 18 and temperature <= 21:
                            colour = colour_codes['Blue']
                            red = colour[0]
                            green = colour[1]
                            blue = colour[2]
                            
                            if uuid in cache:
                                if cache.get(uuid)[0] == red and cache.get(uuid)[1] == green and cache.get(uuid)[2] == blue:
                                    results_list.append(f'Rack {name} - Temperature: {temperature} \N{DEGREE sign}C; Colour: Blue')
                                    break
                                else:
                                    cache_rack_data(uuid, red, green, blue, start_pixel, end_pixel)
                                    results_list.append(f'Rack {name} - Temperature: {temperature} \N{DEGREE sign}C; Colour: Blue')
                                    messageList.append(f'{red},{blue},{green},{start_pixel},{end_pixel}')
                            else:
                                cache_rack_data(uuid, red, green, blue, start_pixel, end_pixel)
                                results_list.append(f'Rack {name} - Temperature: {temperature} \N{DEGREE sign}C; Colour: Blue')
                                messageList.append(f'{red},{blue},{green},{start_pixel},{end_pixel}')
                            
                        elif temperature > 21 and temperature <= 23:
                            colour = colour_codes['Deep Sky Blue']
                            red = colour[0]
                            green = colour[1]
                            blue = colour[2]
                            
                            if uuid in cache:
                                if cache.get(uuid)[0] == red and cache.get(uuid)[1] == green and cache.get(uuid)[2] == blue:
                                    results_list.append(f'Rack {name} - Temperature: {temperature} \N{DEGREE sign}C; Colour: Deep Sky Blue')
                                    break
                                else:
                                    cache_rack_data(uuid, red, green, blue, start_pixel, end_pixel)
                                    results_list.append(f'Rack {name} - Temperature: {temperature} \N{DEGREE sign}C; Colour: Deep Sky Blue')
                                    messageList.append(f'{red},{blue},{green},{start_pixel},{end_pixel}')
                            else:
                                cache_rack_data(uuid, red, green, blue, start_pixel, end_pixel)
                                results_list.append(f'Rack {name} - Temperature: {temperature} \N{DEGREE sign}C; Colour: Deep Sky Blue')
                                messageList.append(f'{red},{blue},{green},{start_pixel},{end_pixel}')
                            
                        elif temperature > 23 and temperature <= 25:
                            colour = colour_codes['Pastel Green']
                            red = colour[0]
                            green = colour[1]
                            blue = colour[2]
                            
                            if uuid in cache:
                                if cache.get(uuid)[0] == red and cache.get(uuid)[1] == green and cache.get(uuid)[2] == blue:
                                    results_list.append(f'Rack {name} - Temperature: {temperature} \N{DEGREE sign}C; Colour: Pastel Green')
                                    break
                                else:
                                    cache_rack_data(uuid, red, green, blue, start_pixel, end_pixel)
                                    results_list.append(f'Rack {name} - Temperature: {temperature} \N{DEGREE sign}C; Colour: Pastel Green')
                                    messageList.append(f'{red},{blue},{green},{start_pixel},{end_pixel}')
                            else:
                                cache_rack_data(uuid, red, green, blue, start_pixel, end_pixel)
                                results_list.append(f'Rack {name} - Temperature: {temperature} \N{DEGREE sign}C; Colour: Pastel Green')
                                messageList.append(f'{red},{blue},{green},{start_pixel},{end_pixel}')
                            
                        elif temperature > 25 and temperature <= 27:
                            colour = colour_codes['Lemon']
                            red = colour[0]
                            green = colour[1]
                            blue = colour[2]
                            
                            if uuid in cache:
                                if cache.get(uuid)[0] == red and cache.get(uuid)[1] == green and cache.get(uuid)[2] == blue:
                                    results_list.append(f'Rack {name} - Temperature: {temperature} \N{DEGREE sign}C; Colour: Lemon')
                                    break
                                else:
                                    cache_rack_data(uuid, red, green, blue, start_pixel, end_pixel)
                                    results_list.append(f'Rack {name} - Temperature: {temperature} \N{DEGREE sign}C; Colour: Lemon')
                                    messageList.append(f'{red},{blue},{green},{start_pixel},{end_pixel}')
                            else:
                                cache_rack_data(uuid, red, green, blue, start_pixel, end_pixel)
                                results_list.append(f'Rack {name} - Temperature: {temperature} \N{DEGREE sign}C; Colour: Lemon')
                                messageList.append(f'{red},{blue},{green},{start_pixel},{end_pixel}')
                            
                        elif temperature > 27 and temperature <= 30:
                            colour = colour_codes['Amber']
                            red = colour[0]
                            green = colour[1]
                            blue = colour[2]
                            
                            if uuid in cache:
                                if cache.get(uuid)[0] == red and cache.get(uuid)[1] == green and cache.get(uuid)[2] == blue:
                                    results_list.append(f'Rack {name} - Temperature: {temperature} \N{DEGREE sign}C; Colour: Amber')
                                    break
                                else:
                                    cache_rack_data(uuid, red, green, blue, start_pixel, end_pixel)
                                    results_list.append(f'Rack {name} - Temperature: {temperature} \N{DEGREE sign}C; Colour: Amber')
                                    messageList.append(f'{red},{blue},{green},{start_pixel},{end_pixel}')
                            else:
                                cache_rack_data(uuid, red, green, blue, start_pixel, end_pixel)
                                results_list.append(f'Rack {name} - Temperature: {temperature} \N{DEGREE sign}C; Colour: Amber')
                                messageList.append(f'{red},{blue},{green},{start_pixel},{end_pixel}')
                            
                        else:
                            colour = colour_codes['Transport Red']
                            red = colour[0]
                            green = colour[1]
                            blue = colour[2]
                            
                            if uuid in cache:
                                if cache.get(uuid)[0] == red and cache.get(uuid)[1] == green and cache.get(uuid)[2] == blue:
                                    results_list.append(f'Rack {name} - Temperature: {temperature} \N{DEGREE sign}C; Colour: Transport Red')
                                    break
                                else:
                                    cache_rack_data(uuid, red, green, blue, start_pixel, end_pixel)
                                    results_list.append(f'Rack {name} - Temperature: {temperature} \N{DEGREE sign}C; Colour: Transport Red')
                                    messageList.append(f'{red},{blue},{green},{start_pixel},{end_pixel}')
                            else:
                                cache_rack_data(uuid, red, green, blue, start_pixel, end_pixel)
                                results_list.append(f'Rack {name} - Temperature: {temperature} \N{DEGREE sign}C; Colour: Transport Red')
                                messageList.append(f'{red},{blue},{green},{start_pixel},{end_pixel}')
            else:
                results_list.append('There are no available readings for this rack.')
        else:
            break
        
        start_pixel += num_pixel
        end_pixel += num_pixel
        
    output = ' | '.join(results_list)
    payload = ','.join(messageList)
   
    client = paho.Client()
    client.on_connect = on_connect

    client.connect("10.154.91.120", 1883)

    client.subscribe("red", qos=0)

    if payload != '':
        client.publish("red", payload=payload, qos=0)

    return output


if __name__ == '__main__':
    main(item_uuids, room_uuid)
    
