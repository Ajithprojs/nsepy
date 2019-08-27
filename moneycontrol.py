from bs4 import BeautifulSoup
import requests
from models.stock import Stock
import parsers.stock_detail as stock_detail

ALL_STOCKS_URL = "https://www.moneycontrol.com/india/stockpricequote"

all_stocks = []

def get_all_stocks():
    source = requests.get(ALL_STOCKS_URL).text
    soup = BeautifulSoup(source, 'html5lib')
    data_table = soup.find('table', class_='pcq_tbl MT10')
    rows = data_table.find_all('td')
    for row in rows:
            title = row.find('a').text
            href = row.find('a', href=True)['href']
            all_stocks.append(Stock(title, href))


def get_details_for_a_stock(name):
        if(len(all_stocks) < 1):
                get_all_stocks()
        stock = [x for x in all_stocks if x.title.lower() == str(name.lower())]   
        print(f'the stock is {stock[0].details_url}')
        source = requests.get(stock[0].details_url).text
        soup = BeautifulSoup(source, 'html.parser')
        main_div = soup.find('div', id='nChrtPrc')
        return stock_detail.retireve_bse_nse_data(main_div)



def get_stock_from_local(name):
        for x in all_stocks:
                title = x.title
                print(f"checking for {title} against {name}")
                if(title == name):
                        return x

print(f"stock name details {get_details_for_a_stock('BEML')}")
#print([str(x) for x in get_all_stocks()])
