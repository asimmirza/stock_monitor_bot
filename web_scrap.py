import requests
from csv_operator import CsvOperation

class WebScrap:
    def getQuote(url):
        res = requests.get(url)
        temp_strp = res.text
        strt_indx = temp_strp.find('<span class="txt15B nse_span_price_wrap')
        end_indx = temp_strp.find('</span>',strt_indx)
        str1 = temp_strp[strt_indx:end_indx+7:]
        strt_indx1 = str1.find('>')
        end_indx1 = str1.find('<',strt_indx1)
        str2 = str1[strt_indx1+1:end_indx1:]
        return float(str2)


# cs = CsvOperation
# l = cs.read_csv()
# ws = WebScrap
# for stock_list in l:
#     # print(stock_list[1])
#     fv= ws.getQuote(stock_list[1])
#     print(fv)

# res = requests.get("https://www.moneycontrol.com/india/stockpricequote/refineries/relianceindustries/RI")
# temp_strp = res.text
