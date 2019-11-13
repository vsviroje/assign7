import math
class Numbers:
    def __init__(self):
        self.value=int(input("Enter the Number:"));

    def ChkPrime(self):
        if self.value > 0 and self.value < 4:
            res = True
        elif self.value == 4:
            res = False
        else:
            c=math.ceil((self.value/2)+1);
            i = 0
            for i in range(2, c, 1):
                if self.value % i == 0:
                    break;
            if (i == (c - 1)):
                res = True;
            else:
                res = False;
        return res

    def Factor(self):
        c = math.ceil((self.value / 2) + 1);
        i = 0
        for i in range(1, c, 1):
            if self.value % i == 0:
                print("Factors is",i)

    def SumOFFactor(self):
            c=math.ceil((self.value/2)+1);
            i,s = 0,0
            for i in range(1, c, 1):
                if self.value % i == 0:
                    s += i
            return s

    def ChkPerfect(self):
        if self.value==self.SumOFFactor():
            return True
        else:
            return False

def main():
    obj1=Numbers()
    print("SumofFactor is ",obj1.SumOFFactor())
    print("Number is ",obj1.ChkPrime(),"ly Prime")
    obj1.Factor()
    print("Number is ", obj1.ChkPerfect(), "ly Prefect")

if __name__=='__main__':
    main()

