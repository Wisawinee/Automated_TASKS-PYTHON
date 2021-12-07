import requests
from bs4 import BeautifulSoup

def get_price_crypto(crypto_name):
    url = f'https://coinmarketcap.com/th/currencies/{crypto_name}/'
    res = requests.get(url)
    res.encoding = "utf-8"
    if res.status_code == 200:
        soup = BeautifulSoup(res.text,'html.parser')
        price_stock = soup.find_all('div',{"class":"priceValue smallerPrice"})
        for price in price_stock:
            without_tag_price = price.string
            without_tag_price = str(without_tag_price)[1:]
            print("Price of "+crypto_name+" is : "+without_tag_price+ " บาท]")
    else:
        print("Http Respone Code is : "+res.status_code)

crypto_name_list = ["bitcoin","ethereum","binance-coin","cardano","dogecoin"]
for crypto_name in crypto_name_list:
    get_price_crypto(crypto_name)

