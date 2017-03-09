import csv
from collections import OrderedDict
from repository import ItemRepository

class CsvImporter:


    def importitems(filename):
        odict = OrderedDict()
        try:
            file = open(filename, mode='r')

        except FileNotFoundError:

            print("Unable to read input filename ", filename)
        else:

            csvReader = csv.reader(file)

            next(csvReader)

            for row in csvReader:
                odict[row[0]] = row[0],row[1:]

        repository = ItemRepository()
        repository.saveitems(odict)

        #print(getattr(repository, 'items'))


    importitems(ItemRepository.DEFAULT_FILE_PATH)

# if __name__ == "__main__":
#     import sys
#
#     importitems(sys.argv[1])
