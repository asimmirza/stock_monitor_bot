import csv

class CsvOperation:
    def read_csv():
        with open('stockdetails.csv') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            stock_list= []
            for row in csv_reader:
                # print(row)
                stock_list.append(row)
        return stock_list

# c = CsvOperation
# l = c.read_csv()
# print(l)