#  CoinGecko API wrapper
Write a Python code which pulls the data from coingecko.com, and
filters out top N cryptocurrencies by market capitalization
## Installation
PyPl
> pip install pip install pycoingecko;

pandas
> pip install pandas;
## Usage
from pycoingecko import CoinGeckoAPI  
cg = CoinGeckoAPI()
## Examples
Entering any parameter to find N top cryptocurrencies <numeric, name, cashflow> defined  
from CoinGecko API doc (https://www.coingecko.com/api/docs/v3)  

List Top 20:  

Please define N top of cryptocurrencies  
20  
TOP 20  
1 BTC 784907775839    
2 ETH 328682881746  
3 USDT 69275001263  
4 ADA 67426381547  
5 BNB 52669476982  
6 XRP 42118740914  
7 SOL 39255916728  
8 USDC 30161576247  
9 DOT 29530421437  
10 DOGE 26313893822  
11 AVAX 15121425262  
12 LUNA 13340238945  
13 BUSD 13226807595  
14 ATOM 10262475582  
15 LINK 9972175630  
16 ALGO 9822062772  
17 UNI 9700205037  
18 LTC 9644847157  
19 BCH 9206503564  
20 WBTC 8599642494   
## API Documentation
https://www.coingecko.com/api/docs/v3

