import requests

# Get city input from user
city_input = input("What city would you like to get the weather report for? ")
# Add input city to request query
city_request = 'https://www.metaweather.com/api/location/search/?query=' + city_input
# Get information for specified city

try:
    city_info = requests.get(city_request)
    json = city_info.json()
    for item in json:
        city_id = item['woeid']
        print(city_id)
        get_weather = 'https://www.metaweather.com/api/location/' + str(city_id)
        print(get_weather)
except requests.exceptions.ConnectionError:
    print("Please verify your internet connection")


# Capture JSON data for specified city

#
# weather_request = requests.get(get_weather)
# json = weather_request.json()
# print(json)

# r = requests.get('https://www.metaweather.com/api/location/2455920')
# text = r.json()
# for value in text['consolidated_weather']:
#     humidity = (value['humidity'])
#     date = (value['applicable_date'])
#     print(f'{date}\tHumidity: {humidity}')

# import requests
# r = requests.get("Programming rocks my socks.")
# print(r.text)

# roman = {'i': 1, 'v': 5, 'x': 10}
# roman['m'] = 1000
# letters = list(roman.keys())
# letters.sort()
# print(" ".join(letters))

# d = r.json()
#
# for forecast in d['consolidated_weather']:
#     date = forecast['applicable_date']
#     humidity = forecast['humidity']
#     print(f"{date}\tHumidity: {humidity}")


# weather = [
#     {
#         'date':'today',
#         'state': 'cloudy',
#         'temp': 68.5
#     },
#     {
#         'date':'tomorrow',
#         'state': 'sunny',
#         'temp': 74.8
#     }
# ]
#
# for forecast in weather:
#     date = (forecast['date'])
#     state = (forecast['state'])
#     temp = (forecast['temp'])
#     print(f'The weather for {date} will be {state} with a temperature of {temp} degrees.')
