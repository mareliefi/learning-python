class BankAccount(object):
  balance = 0
  def __init__(self,name):
    self.name = name
  def __repr__(self):
    return "This account belongs to: %s and the account balance is: R%.2f" %  (self.name,self.balance)
  
  def show_balance(self):
    print "The account balance is: R%.2f" % (self.balance)
    
  def deposit(self,amount):
    if amount <= 0:
      print "You cannot deposit zero or less than zero funds"
      return
    else:
      print "You are depositing an amount of %.2f" % (amount)
      self.balance += amount
      self.show_balance()
    
  def withdraw(self,amount):
    if amount > self.balance:
      print "You do not have sufficient funds available"
      return
    else:
      print "You are withdrawing %.2f" % (amount)
      self.balance -= amount
      self.show_balance()

my_account = BankAccount("Jason")
print my_account
my_account.show_balance()
my_account.show_balance(2000)
my_account.withdraw(1000)
print my_account