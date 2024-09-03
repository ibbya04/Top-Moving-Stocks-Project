import keys
import requests
from twilio.rest import Client

url = "https://api.polygon.io"

headers = {
    "Authorization": "Bearer " + keys.api_key
}

yesterday_figures = requests.get(url + "/v2/aggs/ticker/AAPL/prev?adjusted=true", headers=headers)

yesterday_oc = (yesterday_figures.json()["results"])[0]

prev_close = yesterday_oc["c"]
prev_open = yesterday_oc["o"]

percentage_change = (prev_close-prev_open)/prev_open * 100

print("yesterdays open =", prev_open ,"yesterdays close =", prev_close) #

print(round(percentage_change, 2), "%")

tickers = requests.get(url + "/v3/reference/tickers?market=stocks&active=true&limit=100", headers=headers)
print(tickers.json()["results"])



# client = Client(keys.account_sid, keys.auth_token)
# message = client.messages.create(
#     to="+4407378170226",
#     from_="+4407378170226",
#     body="Hi"
# )