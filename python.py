
class atm(object):
    def __init__(self, cardnumber, pin):
        self.cardnumber=cardnumber
        self.pin=pin
   
    def balance_checker(self):
      
        if self== new_user:
            balance=200.00
            print("balance of", self.cardnumber,"is", "$", balance)
        if self== new_user2:
            balance=400.00
            print("balance of", self.cardnumber,"is", "$", balance)
        if self==new_user3:
            balance=600.00
            print("balance of", self.cardnumber,"is", "$", balance)
    
    def withdraw(self):
        
        if self==new_user:
            print(self.cardnumber,"withdrawed","is",200, "$")
        if self==new_user2:
            print(self.cardnumber,"withdrawed","is",300, "$")
        if self==new_user3:
            print(self.cardnumber,"withdrawed","is",100, "$")
    def card_number_user(self, cardnumber):
        #cardnumber=12345678
        print(cardnumber)
        print(self.cardnumber)

    def print_pin(self):
        #pin_number=3453
        print("pint number: ", self.pin)
new_user=atm(123, 789)
new_user2=atm(456,000)
new_user3=atm(678,100)
#print(new_user2.print_pin())
#print(new_user2.card_number_user("yui"))
new_user.balance_checker()
new_user2.balance_checker()
new_user3.balance_checker()
new_user.withdraw()
new_user2.withdraw()
new_user3.withdraw()


