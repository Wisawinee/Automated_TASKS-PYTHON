import requests
from bs4 import BeautifulSoup
from songline import Sendline

def get_price_stock(company_name,messenger):
    url = f'https://www.settrade.com/C04_01_stock_quote_p1.jsp?txtSymbol={company_name}&ssoPageId=9&selectPage=1'
    res = requests.get(url)
    res.encoding = "tis-620"
    price_list = []
    if res.status_code == 200:
        soup = BeautifulSoup(res.text,'html.parser')
        price_stock = soup.find_all('h1')
        for price in price_stock:
            without_tag_price = price.string
            without_tag_price = str(without_tag_price).replace(" ","")
            without_tag_price = str(without_tag_price).replace("\r","")
            without_tag_price = str(without_tag_price).replace("\n","")
            price_list.append(without_tag_price)
        string_to_send_line = "Price of "+company_name+" is "+price_list[1]+ " BATH"
        messenger.sendtext(string_to_send_line)
        #print("Price of "+company_name+" is "+price_list[1]+ " BATH")
    else:
        string_to_send_line = f"Http Respone Code is : {res.status_code}"
        messenger.sendtext(string_to_send_line)
        #print("Http Respone Code is : "+res.status_code)

token = 'ce8cDvK71QQUKL6wWWCNEcUgSb81RQRnJhdB5pH4chx'
messenger = Sendline(token)

stock_name_list = ["ADVANC","AOT","BBL","BDMS","BEM","BGRIM","BH","VL","JUTHA"]
for stock_name in stock_name_list:
    get_price_stock(stock_name,messenger)
