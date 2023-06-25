import datetime
import pytz
#import requests


def format_unix_timestamp(timestamp):
    # Set the time zone to GMT+1 (Czech Republic)
    tz = pytz.timezone('Europe/Prague')
    date = datetime.datetime.fromtimestamp(timestamp / 1000, tz)
    formatted_date = date.strftime("%A, %B %d, %Y, %I:%M:%S %p")
    return formatted_date


# def fetch_data(range_value):
    url = 'https://api.example.com/data/{}'.format(range_value)
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        # Process the retrieved data
        return data
    else:
        print('Request failed with status code:', response.status_code)
        return None


timestamp = 1658851200000  # Assuming the timestamp is in seconds
human_readable_date = format_unix_timestamp(timestamp)

print(human_readable_date)

#url = 'https://api.example.com/data'
#response = requests.get(url)
#
# if response.status_code == 200:
#    data = response.json()
# Process the retrieved data
# else:
#    print('Request failed with status code:', response.status_code)
