# from taxstrategy import imported_strategy, national_strategy
from repository import ItemRepository
from defaultTaxHandler import DefaultTaxHandler
from taxstrategy import *


class Store:
    national_strategyInstance = NationalStrategy()
    national_strategy = national_strategyInstance.calculateNational

    imported_strategy = ImportedStrategy().calculateImported

    national_strategyInstance.tax_exempt_item_types = {"book", "food", "medical"}

    tax_handler = DefaultTaxHandler(national_strategy, imported_strategy)

    def purchase(self, ids):
        repo = ItemRepository()

        net_purchase_price = 0.0
        gross_purchase_price = 0.0

        for id in ids:
            item = repo.getById(id)
            netprice = self.tax_handler.calculate(item)

            itemNetPriceLabel = "%.2f" % round(netprice, 2)
            print("item net price", itemNetPriceLabel)

            net_purchase_price += netprice
            gross_purchase_price += float(item.grossprice)

        print("Sales Taxes : %.2f" % round(net_purchase_price - gross_purchase_price, 2))
        print("Total : %.2f" % round(net_purchase_price, 2))
