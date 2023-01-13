from abc import abstractmethod, ABC


# Abstract class
class Product(ABC):
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def show(self):
        print('Name  :', self.name)
        print('Price :', self.price)

    @abstractmethod
    def getprice(self):
        pass


class ImportedProduct(Product):
    def __init__(self, name, price, importduty):
        super().__init__(name, price)
        self.importduty = importduty

    def show(self):
        super().show()
        print("Import duty : ", self.importduty)

    def getprice(self):
        return self.price + (self.price * self.importduty / 100)


class DiscountedProduct(Product):
    def __init__(self, name, price, discountrate):
        super().__init__(name, price)
        self.discountrate = discountrate

    def show(self):
        super().show()
        print("Discount Rate : ", self.discountrate)

    def getprice(self):
        return self.price - (self.price * self.discountrate / 100)


p1 = DiscountedProduct("Abc", 10000, 10)
print(p1.getprice())
p2 = ImportedProduct("Xyz", 20000, 20)
print(p2.getprice())
