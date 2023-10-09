class Computer:
    def __init__(self):
        self.__maxprice = 900
    def sell(self):
        print('Selling Price: {}'.format(self.__maxprice))

    def setMaxPrice(self, price):
        self.__maxprice = price

c = Computer()

c.__maxprice = 10000
c.setMaxPrice(100)
c.sell()

