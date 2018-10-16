#!/usr/bin/env python

import requests

icons = {
    'clear-day': '',
    'clear-night': '',
    'cloudy-day': '',
    'cloudy-night': '',
    'cloudy': '',
    'wind': '',
    'rain': '',
    'showers': '',
    'thunder': '',
    'snow': '',
    }

with open('config', 'r') as config:
    lines = config.readlines()
    for line in lines:
        if 'api:' in line:
            line = line.strip().split(' ')
            api = line[1]
        if 'loc:' in line:
            line = line.strip().split(' ')
            coords = line[1]


url = f'https://api.darksky.net/forecast/{api}/{coords}'

weather = requests.get(url)
weather.raise_for_status()

w = weather.json()

temp = w['currently']['temperature']
iconcode = w['currently']['icon']

if 'rain' in iconcode:
    icon = icons['rain']
elif 'shower' in iconcode:
    icon = icons['showers']
elif 'clear' in iconcode:
    if 'day' in iconcode:
        icon = icons['clear-day']
    elif 'night' in iconcode:
        icon = icons['clear-night']
elif 'snow' in iconcode or 'sleet' in iconcode:
    icon = icons['snow']
elif 'wind' in iconcode or 'fog' in iconcode:
    icon = icons['wind']
elif 'cloudy' in iconcode:
    if iconcode == 'partly-cloudy-day':
        icon = icons['cloudy-day']
    elif iconcode == 'partly-cloudy-night':
        icon = icons['cloudy-night']
    else:
        icon = icons['cloudy']
elif 'thunderstorm' in iconcode:
    icon = icons['thunder']
else:
    icon = icons['cloudy']

print(f'{icon}{round(temp)}°F')
