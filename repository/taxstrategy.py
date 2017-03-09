class NationalStrategy:
    tax_exempt_item_types = None
    __tax = float(10)

    def calculateNational(self, item):
        iterables = []
        iterables.append(float(item.grossprice))
        iterables.append(self.__calculate(item))
        # netprice = [
        #     float(item.grossprice) + self.__calculate(item) if item.type not in self.tax_exempt_item_types else float(
        #         item.grossprice)][0]
        netprice = [
            sum(iterables) if item.type not in self.tax_exempt_item_types else float(
                item.grossprice)][0]
        print(netprice)
        return netprice

    def __calculate(self, item):
        return NationalStrategy.__tax / 100 * float(item.grossprice)


class ImportedStrategy:
    __imported = "imported"
    __tax = float(5)

    def calculateImported(self, item):
        iterables = []
        iterables.append(self.__calculate(item))
        netprice = [self.__calculate(item) if item.origin == self.__imported else 0][0]

        print(netprice)
        return netprice


    def __calculate(self, item):
        return ImportedStrategy.__tax / 100 * float(item.grossprice)
