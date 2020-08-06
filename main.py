from csv_operator import CsvOperation
from web_scrap import WebScrap
from VoiceMesssage import VoiceHandler
from MakeCall import MakeCalls
import time

if __name__ == '__main__':
    cs = CsvOperation
    l = cs.read_csv()
    ws = WebScrap
    vh = VoiceHandler
    mc = MakeCalls
    stop_flag = True
    stock_updated_list = []
    while stop_flag:
        for stock_list in l:
            # print(stock_list[1])
            fv = ws.getQuote(stock_list[1])
            msg = "Current Rate of " + str(stock_list[0]) + " is " + str(fv)
            print(msg)
            stop_loss = float(stock_list[2])
            target = float(stock_list[3])
            print(stop_loss)
            print(target)
            if stop_loss >= fv:
                msg = "Alert ! Stop Loss for " + str(stock_list[0]) + " is " + str(fv)
                stock_list[4]=1
                mc.CallUser()
                mc.SendMessage(msg)
                vh.read_message(msg)
            elif target <= fv:
                stock_list[5] = 1
                msg = "Alert ! Target Achieved for " + str(stock_list[0]) + " is " + str(fv)
                vh.read_message(msg)
                mc.SendMessage(msg)
            stock_updated_list.append(stock_list)
        print(stock_updated_list)
        cs.write_file(stock_updated_list)
        time.sleep(120)


