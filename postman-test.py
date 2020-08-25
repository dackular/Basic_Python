import requests

url = "https://deckofcardsapi.com/api/deck/87nfwro26sjd/draw/"

querystring = {"count":"6"}

headers = {
    'cache-control': "no-cache",
    'postman-token': "5d0fe71a-1337-93ca-b4d0-8ba5cb9b32d8"
    }

response = requests.request("GET", url, headers=headers, params=querystring)
print(response.text)
deck = response.json()
deck_id = deck['deck_id']
print(deck_id)
