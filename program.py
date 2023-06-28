import datetime
import pytz
import requests


def format_unix_timestamp(timestamp):
    # Set the time zone to GMT+1 (Czech Republic)
    tz = pytz.timezone('Europe/Prague')
    date = datetime.datetime.fromtimestamp(timestamp / 1000, tz)
    formatted_date = date.strftime("%A, %B %d, %Y, %I:%M:%S %p")
    return formatted_date


def fetch_data():
    #url = 'https://api.example.com/data/{}'.format(range_value)
    url = 'https://fapi.binance.com/fapi/v1/fundingRate?symbol=BTCUSDT&limit=1000'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        # Process the retrieved data
        return data
    else:
        print('Request failed with status code:', response.status_code)
        return None


timestamp = 1687968000000  # Assuming the timestamp is in seconds
human_readable_date = format_unix_timestamp(timestamp)

#print(fetch_data())
data1 = fetch_data()
print("ahoj")
print(human_readable_date)

#url = 'https://api.example.com/data'
#response = requests.get(url)
#
# if response.status_code == 200:
#    data = response.json()
# Process the retrieved data
# else:
#    print('Request failed with status code:', response.status_code)
