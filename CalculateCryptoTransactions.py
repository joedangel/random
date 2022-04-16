from TransactionsCsvReader import TransactionsCsvReader

class CalculateCryptoTransactions:
    def calculateAllTransactions(self):
        coins = ["BTC", "ETH", "DOGE"]
        for coin in coins:
            print(coin, "Transactions:")
            typed_transactions = self.__getTypedTransactions(coin)
            self.calculateTransactions(typed_transactions)

    def calculateTransactions(self, typed_transactions):
        # We have transactions split by type. Now we match sells with their respective buys.
        completed_transactions = []
        profit = 0
        for buy in typed_transactions["btc_buy"]:
            purchased = buy[5]
            p_price = buy[7]
            while purchased > 0 and typed_transactions["btc_sell"]:
                sell = typed_transactions["btc_sell"][0]
                sold = sell[5]
                s_price = sell[7]
                if sold < purchased:
                    spent = sold * p_price
                    made = sold * s_price
                    completed_transactions.append(("acquired date:", buy[1], "sold date:", sell[1], "p_price:", p_price, "s_price:", s_price, "amount:", sold, "profit:", made-spent))

                    profit += (made - spent)
                    typed_transactions["btc_sell"] = typed_transactions["btc_sell"][1:]
                    purchased -= sold
                else:
                    spent = purchased * p_price
                    made = purchased * s_price
                    completed_transactions.append(("acquired date:", buy[1], "sold date:", sell[1], "p_price:", p_price, "s_price:", s_price, "amount:", purchased, "profit:", made-spent))

                    profit += (made - spent)
                    sell[5] -= purchased
                    purchased = 0

        for trans in completed_transactions:
            print(trans)

        print("profit:", profit)

    def __getTypedTransactions(self, coin):
        reader = TransactionsCsvReader()
        data = reader.getCleanedData()

        items = { "btc_buy":[], "btc_sell":[] }

        for row in data:
            if row[4] == coin:
                if row[2] == "Buy":
                    items["btc_buy"] += [row]
                elif row[2] == "Sell":
                    items["btc_sell"] += [row]

        return items

calculator = CalculateCryptoTransactions()
calculator.calculateAllTransactions()
