from csv_operator import CsvOperation
from web_scrap import WebScrap
from VoiceMesssage import VoiceHandler

if __name__ == '__main__':
    cs = CsvOperation
    l = cs.read_csv()
    ws = WebScrap
    vh = VoiceHandler
    for stock_list in l:
        # print(stock_list[1])
        fv = ws.getQuote(stock_list[1])
        msg = "Current Rate of " + str(stock_list[0]) + " is " + str(fv)
        print(msg)
        vh.read_message(msg)


