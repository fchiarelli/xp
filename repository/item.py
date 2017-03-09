class Item:
    """Represents a purchaseable Item
    attibutes id, grossprice, description
    """
    def __init__(self, itemValue):
        self.id = itemValue[0]
        self.origin = itemValue[1][0]
        self.type = itemValue[1][1]
        self.desc = itemValue[1][2]
        self.grossprice = itemValue[1][3]

