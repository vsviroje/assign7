class BookStore:
    NoOfBook=0
    def __init__(self,n,a):
        self.name=n;
        self.author=a;
        #to change Class variable use class name
        BookStore.NoOfBook += 1

    def Display(self):
        print(self.name," by",self.author," No of All different type of book-",self.NoOfBook)


def main():
    obj1=BookStore("Linux System Programming","Robbert Love")
    obj1.Display()
    obj2=BookStore("C Programming","Dennis Ritchie")
    obj2.Display()

if __name__=='__main__':
    main()

