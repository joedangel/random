import csv

class TransactionsCsvReader:
    def getCleanedData(self):
        raw_data = self.__getCsvData()
        data = list(filter(lambda x: x[3].count("USD") == 0, raw_data))

        # ['User_Id', 'Time', 'Operation', 'Transaction_Id', 'Base_Asset', 'Realized_Amount_For_Base_Asset', 'Realized_Amount_For_Quote_Asset', 'Asset_Price']
        filtered_data = [[row[0], row[1], row[3], round(int(row[5]), 3), row[9], round(float(row[10]), 3), round(float(row[13]), 3), round(float(row[13]) / float(row[10]), 3)] for row in data[1:]]
        filtered_data_sorted = sorted(filtered_data, key=lambda x: x[3])
        return filtered_data_sorted

    def __getCsvData(self):
        output = []
        csv_file = '/Users/joedangelewicz/Documents/Taxes/BinanceTaxStatement2021.csv'
        with open(csv_file) as file:
            reader = csv.reader(file)
            for line in reader:
                output.append(line)
        return output
