__author__ = 'joezhou'
import requests
import json
import time
from bs4 import BeautifulSoup


URL1 = 'http://chartapi.finance.yahoo.com/instrument/1.0/'
URL2 = '/chartdata;type=quote;range=1d/json'
class FLOW(object):
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
        self.up = 0
        self.up_sum = 0.0
        self.sum = 0.0
        self.down = 0
        self.down_sum = 0.0

    def get_content(self, url, params):
        response = requests.get(url, params=params)
        #print (url, params)
        if response.status_code == 200:
            content_json = response.content.decode()
            content_json1 = content_json.split(' ', 1)[1]
            content_json1 = content_json1[:-1]
            data=json.loads(content_json1)
            #print(data['series'])
            pre_close = 0.0
            pre_sum = 0.0
            for item in data['series']:
                # print (item)
                # print (item['Timestamp'],item['high'],item['volume'])
                avg = (float(item['close']) + float(item['high']) + float(item['low'])) / 3
                if pre_close == 0.0:
                    next
                else:
                    if  avg> pre_close:
                        self.up_sum += pre_sum
                        self.up += 1
                    else:
                        self.down_sum += pre_sum
                        self.down += 1
                pre_close = avg
                pre_sum = avg* float(item['volume'])
            self.sum = self.up_sum - self.down_sum
        else:
            data = 0
        return data




if __name__ == '__main__':
    total_up=0
    total_down=0
    sum1=0.0
    #for key, value in list.items():
    tickers =['nmbl',
             'goog',
             'fb',
             'aapl',
             'tsla',
             'amzn',
             'gpro'
             ]
    for ticker in tickers:
        FLOW_URL=URL1+ticker+URL2
        oc = FLOW(ticker)
        data = oc.get_content(FLOW_URL, oc.params)
        print (ticker, oc.up, oc.down, "{:,.0f}".format(oc.sum), "percent {:,.2f}".format(oc.sum/(oc.up_sum+ oc.down_sum)))
        file_line= "\n"+time.strftime('%X %x') + " up= " + str(oc.up) + " down= " + str(oc.down) + " total= " + str(oc.sum)
        with open("nmbl_intraday.txt", "a") as myfile:
            myfile.write(file_line)
    myfile.close()

