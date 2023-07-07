# Futures-funding-rate-calculations

## Futures endpoints
- `f`api - `futures` api - https://fapi.binance.com/fapi/v1/fundingRate?symbol=BTCUSDT&limit=1000
- batching by 1000, can query multiple times w/ `startTime` -  https://fapi.binance.com/fapi/v1/fundingRate?symbol=BTCUSDT&limit=1000&startTime=1624564800000

## Internal notes
- Conda python 3.7
- /Users/stepo/anaconda3/envs/ffrc/bin/python pip install pytz
- /Users/stepo/anaconda3/envs/ffrc/bin/python pip install requests  

Run along with libraries like `pythonRT program.py`.
```zsh
/Users/stepo/anaconda3/envs/ffrc/bin/python program.py  
```

## Alg. idea - mock calc. w/ Futures-funding-rate-calculations
1a) **Short highest funded futures coin**  


|DATE| BTC | ETH | VET | ADA | **(/USDT)**  
| f_t0 | <ins>0.48</ins> | 0.22 | 0.18 | 0.11 |  
| f_t1 | 0.17 | <ins>0.68</ins> | 0.44 | 0.08 |  
| f_t2 | 0.20 | 0.44 | <ins>0.82</ins> | 0.20 |  
| f_t3 | 0.34 | 0.18 | 0.22 | <ins>0.52</ins> |  
| f_t4 | 0.08 | 0.14 | <ins>0.38</ins> | 0.12 |  

Horizontally Stacked By Stock https://towardsdatascience.com/pandas-multiindexing-and-working-with-time-series-data-8e6229f11998

- Futures we are interested in will give us columns to be fetched from fapi.
```json
['BTCUSDT', 'ETHUSDT', 'BCHUSDT', 'XRPUSDT', 'LTCUSDT']
```
- `pandas.DataFrame` https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html
- `data = data.set_index(['ticker','date'])`  

Downloaded data like
```json
[{
    "symbol": "BTCUSDT",
    "fundingTime": 1659542400008,
    "fundingRate": "0.00004382"
}, ...]
```

1b) **Long on spot the asset with same amount of cash**  
2) Rebalance & repeat.

## Implementation
- rec. list retrieval and chronological list
- then fill into pandas dataframe pd.DataFrame
- generate HTML table output for test 
- maximalize shit + constrains
___
## Misc. - ChatGPT response
Q: Get all history of Bitcoin BTCUSDT funding rates here https://fapi.binance.com/fapi/v1/fundingRate

To obtain the complete history of Bitcoin (BTC) funding rates for the BTCUSDT perpetual futures on Binance, you can use the following endpoint:

```
GET https://fapi.binance.com/fapi/v1/fundingRate?symbol=BTCUSDT&limit=1000
```

This endpoint will provide you with the funding rate history for the BTCUSDT perpetual futures, with a maximum limit of 1000 data points per request. If there are more than 1000 data points, you will need to make additional requests using the `startTime` parameter to retrieve the remaining history.

To retrieve the complete funding rate history, you can follow these steps:

1. Make an initial request to the endpoint mentioned above. This will provide you with the most recent 1000 funding rate data points for BTCUSDT.
2. Check the response to see if there is a `nextFundingTime` field. This field indicates the timestamp of the next funding rate, which will be your `startTime` parameter for the subsequent request.
3. Make another request to the endpoint, adding the startTime parameter to retrieve the next set of funding rate data points. For example, if the `nextFundingTime` is 1624564800000 (timestamp in milliseconds), the URL will be:

```
GET https://fapi.binance.com/fapi/v1/fundingRate?symbol=BTCUSDT&limit=1000&startTime=1624564800000
```

4. Repeat steps 2 and 3 until there is no `nextFundingTime` field in the response. Each subsequent request should use the `startTime` from the previous response.  

By following this approach, you can retrieve the complete history of Bitcoin funding rates for the BTCUSDT perpetual futures. Please note that the number of requests required will depend on the total number of data points in the history.

Remember to handle rate limits and pagination in accordance with the Binance API guidelines.