STOCK_URL = 'https://www.nseindia.com/live_market/dynaContent/live_watch/get_quote/GetQuote.jsp?'
TOP_GAINER_URL = 'http://www.nseindia.com/live_market/dynaContent/live_analysis/gainers/niftyGainers1.json'
TOP_LOSER_URL = 'http://www.nseindia.com/live_market/dynaContent/live_analysis/losers/niftyLosers1.json'
ALL_INDEXES_JSON = 'http://www.nseindia.com/content/equities/EQUITY_L.csv'

def get_quote(name):
    name = name.upper()
    url = self.build_url_for_quote(name)
    req = Request(url, None, self.headers)

def build_url_for_quote(self, code):
        """
        builds a url which can be requested for a given stock code
        :param code: string containing stock code.
        :return: a url object
        """
        if code is not None and type(code) is str:
            encoded_args = urlencode([('symbol', code), ('illiquid', '0'), ('smeFlag', '0'), ('itpFlag', '0')])
            return self.STOCK_URL + encoded_args