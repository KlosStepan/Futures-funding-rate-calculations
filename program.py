import datetime
import pytz
import requests
#DEFAULT TIMEZEONE IS GMT
#BINANCE FUTURES SHOW +2
#https://www.binance.com/en/futures/funding-history/perpetual/funding-fee-history

def format_unix_timestamp(timestamp):
    # Set the time zone to GMT+1 (Czech Republic)
    #tz = pytz.timezone('Europe/Prague')
    #.../ 1000, tz)
    date = datetime.datetime.fromtimestamp(timestamp / 1000)
    formatted_date = date.strftime("%A, %B %d, %Y, %I:%M:%S %p")
    return formatted_date


def fetch_data(symbol):
    data = []
    url = 'https://fapi.binance.com/fapi/v1/fundingRate?symbol={}&limit=1000&startTime=1568102400000'.format(symbol)
    response = requests.get(url)
    if response.status_code == 200:
        data = data + response.json()
        print(len(response.json()))
        print(format_unix_timestamp(response.json()[0]['fundingTime']))
        print(response.json()[0])
        print(format_unix_timestamp(response.json()[999]['fundingTime']))
        #print((response.json()[999]['fundingTime']))
        print(response.json()[999])
        #return data
    else:
        print('Request failed with status code:', response.status_code)
        #return None
    return []    
    
def fetch_data_rec(symbol, limit, startTime):
    url = f"https://fapi.binance.com/fapi/v1/fundingRate?symbol={symbol}&limit={limit}&startTime={startTime}"

timestamp = 1687968000000  # Assuming the timestamp is in seconds
human_readable_date = format_unix_timestamp(timestamp)

#print(fetch_data('BTCUSDT'))
data1 = fetch_data('BTCUSDT')
#print(data1)
#print(len(data1))
#print("ahoj")
#print(human_readable_date)

#url = 'https://api.example.com/data'
#response = requests.get(url)
#
# if response.status_code == 200:
#    data = response.json()
# Process the retrieved data
# else:
#    print('Request failed with status code:', response.status_code)
