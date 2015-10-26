import requests
from requests.exceptions import ConnectionError
import json
import re
import urllib3
from bs4 import BeautifulSoup

OPTION_CHAIN_URL = 'https://www.google.com/finance/option_chain'
SITE = "http://en.wikipedia.org/wiki/List_of_S%26P_500_companies"
class OptionChain(object):
    def __init__(self, q):
        """
        Usage:
        from optionchain import OptionChain
        oc = OptionChain('NASDAQ:AAPL')
        # oc.calls
        # oc.puts
        """
        self.params = {
            'q': q,
            'output': 'json'
        }
        self.put_total=0
        self.call_total=0
        self.put_sum=0
        self.call_sum=0

    def get_option(self, data):
        datajson =json.loads(data)
        calls= datajson['calls']
        puts= datajson['puts']
        for item in calls:
          detail = json.dumps(item)
          detail_json=json.loads(detail)
          if (detail_json['oi'] != "-" and detail_json['vol'] != "-") :
             vol=int(detail_json['vol'] )
             oi =int(detail_json['oi'])
             if ((vol>500) and vol > oi*3) or vol > 4000:
                 self.call_total +=1
                 self.call_sum += float(detail_json['p']) * float(detail_json['vol'])
                 print ("call",detail_json['s'],detail_json['strike'], detail_json['vol'],detail_json['oi'],detail_json['a'],detail_json['b'],detail_json['p'])
        for item in puts:
          detail = json.dumps(item)
          detail_json=json.loads(detail)
          if (detail_json['oi'] != "-" and detail_json['vol'] != "-"):
             vol=int(detail_json['vol'] )
             oi =int( detail_json['oi'])
             if ((vol >500) and vol > oi*3) or vol > 4000 :
                self.put_total +=1
                self.put_sum += float(detail_json['p']) * float (detail_json['vol'])
                print ("Puts",detail_json['s'],detail_json['strike'], detail_json['vol'],detail_json['oi'],detail_json['a'],detail_json['b'],detail_json['p'])
        #print (total_calls, sum_calls, "put", total_puts, sum_puts )
        return detail_json

    def _get_content(self, url, params):
        response = requests.get(url, params=params)
        #print (url, params)
        if response.status_code == 200:
            content_json = response.content
            content=re.sub("(\w+):",'"\\1":',content_json.decode())
            return content
        else:
            params['q'] ="NYSE:" + params['q']
            response = requests.get(url, params=params)
            print (url, params)
            if response.status_code == 200:
                content_json = response.content
                content=re.sub("(\w+):",'"\\1":',content_json.decode())
                return content

class scrape(object):
    def __init__(self, site, q):
        """
        Usage:
        from optionchain import OptionChain
        oc = OptionChain('NASDAQ:AAPL')
        # oc.calls
        # oc.puts
        """
        self.params = {
            'q': q,
            'output': 'json'
        }

        self.site=site

    def scrape_list(self, site, params):
        response = requests.get(site, params=params)
        if response.status_code == 200:
            page = response.content
        soup = BeautifulSoup(page)

        table = soup.find('table', {'class': 'wikitable sortable'})
        sector_tickers = dict()
        for row in table.findAll('tr'):
            col = row.findAll('td')
            if len(col) > 0:
                sector = str(col[3].string.strip()).lower().replace(' ', '_')
                ticker = str(col[0].string.strip())
                if sector not in sector_tickers:
                    sector_tickers[sector] = list()
                sector_tickers[sector].append(ticker)
        #print (sector_tickers)
        return sector_tickers



if __name__ == '__main__':
    LT=scrape(SITE, json)
    list =LT.scrape_list(SITE, LT.params)
    total_puts=0
    total_calls=0
    sum_puts=0
    sum_calls=0
    for key, value in list.items():
        for ticker  in value :
            oc = OptionChain(ticker)
            data = oc._get_content(OPTION_CHAIN_URL, oc.params)
            option= oc.get_option(data)
            total_calls += oc.call_total
            sum_calls += oc.call_sum
            total_puts += oc.put_total
            sum_puts += oc.put_sum

    print ("put counts", total_puts, "call counts", total_calls, "sum of puts",sum_puts, "sum of calls", sum_calls)



