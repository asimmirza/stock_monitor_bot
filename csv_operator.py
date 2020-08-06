import csv
import shutil
import os

class CsvOperation:
    def read_csv():
        with open('stockdetails.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            stock_list= []
            for row in csv_reader:
                # print(row)
                stock_list.append(row)
            csv_file.close()

        return stock_list

    def copy_file():

        shutil.copy('temp_stockdetails.csv','stockdetails.csv')
        os.remove('temp_stockdetails.csv')


    def write_file(row):
        with open('stockdetails.csv', 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerows(row)
            # # c = CsvOperation
            # # l = c.read_csv()
            # for row in l:




# c = CsvOperation
# c.write_file()
# print(l)
# c.copy_file()