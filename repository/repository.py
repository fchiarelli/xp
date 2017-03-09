from item import Item
class ItemRepository:
    DEFAULT_FILE_PATH = "data/store_repository.csv"
    __shared_state = {}
    items = None

    def __init__(self):
        self.__dict__ = self.__shared_state

    def saveitems(self, odict):
        self.items = odict
        print('repo initialized: ', self.items)

    def getById(self, id):

        itemValue = self.items[id]
        return Item(itemValue)


