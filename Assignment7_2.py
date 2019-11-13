class BankAccount:
    ROI=10.5
    def __init__(self,n,a):
        self.name=n;
        self.amount=a;


    def Display(self):
        print(self.name," by",self.author," No of All different type of book-",self.NoOfBook)

    def Deposit(self):
        N= int(input("Enter amount to deposit:"))
        if N<=0:
            return print("Don't give Negative value")
        else:
            self.amount += N

    def WithDraw(self):
        if self.amount <= 0:
            return print("Bank balance zero")
        else:
            n=int(input("Enter amount to deposit:"))
            if(n>self.amount):
                return print("Bank balance not enough")
            else:
                self.amount -= n
                print("Withdraw Succefully and balance is ",self.amount)

    def calInterest(self):
        if self.amount <= 0:
            return print("Bank balance zero")
        else:
            #add your formula if needed
            n=(self.amount*self.ROI*1)/100
            print("On current balance Interest for 1 year is ",n)
    def Display(self):
        print("Name :",self.name," Amount :",self.amount)

def main():
    name=str(input("Enter name:"))
    amount=int(input("Enter amount:"))
    obj1=BankAccount(name,amount)

    obj1.Deposit()
    obj1.WithDraw()
    obj1.calInterest()
    obj1.Display()

    name = str(input("Enter name:"))
    amount = int(input("Enter amount:"))
    obj2 = BankAccount(name, amount)

    obj2.calInterest()
    obj2.Display()


if __name__=='__main__':
    main()

