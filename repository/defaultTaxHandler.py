class DefaultTaxHandler:
    def __init__(self, *strategies):
        self.strategies = strategies

    def calculate(self, item):
        netprice = 0
        for strategy in self.strategies:
            netprice += strategy(item)

        #print("Total net price is " + str(netprice))
        return netprice
