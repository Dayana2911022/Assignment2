from pycoingecko import CoinGeckoAPI

cg = CoinGeckoAPI()


class Coin:
    def __init__(self, top, Name, market_cap):
        self.top = top
        self.name = Name
        self.market_cap = market_cap

    def __str__(self):
        return f"{self.name}"


print("Please define N top of cryptocurrencies")
topN = input()
print("----GETTING ALL COINS----")
market = cg.get_coins_markets(vs_currency="usd")

market = sorted(market, key=lambda k: k['market_cap'], reverse=True)
print(f"----TOP {topN}----")
top = 1
listOfTops = []
for crypto in market:
    name = crypto['symbol'].upper()
    market_cap = crypto['market_cap']
    coin = Coin(top=top, Name=name, market_cap=market_cap)
    listOfTops.append(coin)
    top += 1
    if top > int(topN):
        break

for i in listOfTops:
    print(f"{i.top}. {i.name} - {int(i.market_cap)}")

