class Bank():

    def __init__(self,name,amount):
        self.name = name
        self.amount = amount

    def __str__(self):

        return f'Owners name is {self.name}\nBalance - {self.amount}'


    def add_amount(self,value):
        self.amount = self.amount + value
        print(f'{value} $ recieved')
        return self.amount
    def cashout(self,value):
        if self.amount < value:
            print('Not enough amount of money on your account')
        else:
            self.amount = self.amount - value
            print(f'{value} withdraw from your account')
        return self.amount

myacc = Bank('Max',1000)


print(myacc)


