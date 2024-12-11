class Store:
    def __init__(self, name='', address='', items=None):
        if items is None:
            self.items = {}
        self.name = name
        self.address = address

m1 = Store("Магазин №21","ул.Главная, 134")
