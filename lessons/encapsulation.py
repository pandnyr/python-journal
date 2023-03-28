class BankAccount(object):
    def __init__(self, name, money, adress):
        self.name = name # Global
        self.__money = money # Private
        self.address = adress

    # get and set
    def getMoney(self):
        return self.__money

    def setMoney(self, amount):
        self.__money = amount

    # Private
    def __increase(self):
        self.__money = self.__money + 500


p1 = BankAccount("Jack", 1000, "NYC")
p2 = BankAccount("Lisa", 2000, "Paris")

print("Get Method : ", p1.getMoney())


p1.setMoney(5000)
print("After Set Method : ", p1.getMoney())

# p1.increase()
# print("After raise : ", p1.getMoney())

