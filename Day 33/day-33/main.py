import requests
from datetime import datetime

# response = requests.get(url='http://api.open-notify.org/iss-now.json')
# response.raise_for_status()
#
# data = response.json()
#
# iss_position = (data['iss_position']['longitude'], data['iss_position']['latitude'])
#
# print(iss_position)

MY_LAT = 48.856613
MY_LONG = 2.352222

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
    "tzid": "Europe/Paris"
}

response = requests.get(url='https://api.sunrise-sunset.org/json', params=parameters)
response.raise_for_status()

data = response.json()
sunrise = data['results']['sunrise'].split("T")[1].split(":")[0]
sunset = data['results']['sunset'].split("T")[1].split(":")[0]

print(datetime.now().hour)
print(sunrise)
print(sunset)
