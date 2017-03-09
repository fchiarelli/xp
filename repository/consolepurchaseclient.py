import glob
import re
from sys import argv
from csvimporter import CsvImporter
from store import Store

class ConsolePurchaseClient:
    store = Store()

    def purchase(self):
        print("User Purchase Request", glob.glob(argv[1]))
        purchases = dict()
        for purchasefile in glob.glob(argv[1]):
            try:
                ids = open(purchasefile, 'r').readline().strip().split(",")
                key = re.match('.*(\d).*', purchasefile).group(1)
                purchases[key] = ids
                #print("%s -> %s" % (key, ids))
                self.store.purchase(ids)
            except Exception as e: print(e)
           # except Exception:
                # pass
                #print("Unable to process purchase request : ", purchasefile)


if __name__ == "__main__":
    purchaseClient = ConsolePurchaseClient().purchase()
