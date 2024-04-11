
class Library:

    def __init__(self):
        self.NoBooks = 0
        self.Books = []


    def AddBook(self,books):
        self.Books.append(books)
        self.NoBooks = len(self.Books)


    def ShowInfo(self):
        print(f"There are {self.NoBooks} in the Library. The Books are : ")
        i = 0
        for book in self.Books:
            print(f"{i+1}) {book}")
            i = i + 1


a = Library()
b = Library()

a.AddBook("Python Notes")
a.AddBook("Python Projects")
a.AddBook("Python Loops")

b.AddBook("HTML")
b.AddBook("HTML Docs")
b.AddBook("HTML Project")

while(True):

    print('''
        ====== Welcome To Central Library ======
    1. List of Books
    2. Add an Book
    3. Go To Other Library
    4. Exit Central Library
    ''')

    user = input("Enter Your Choise : ")

    if user == '1':
        a.ShowInfo()
    elif user == '2':
        Book_Input = input("Enter the Name Of Book You Want To Add : ")
        a.AddBook(Book_Input)
        print("Thanks For Adding The Book")
    elif user == '3':
        print("1. Go to HTML Library")
        lib = input("Enter Your Choice : ")
        if lib == '1':
            print("Welcome To HTML Library")
            while(True):
                print("Welcome To Python Library")
                print('''
                    ====== Welcome To Central Library ======
                1. List of Books
                2. Add an Book
                3. Go To Other Library
                4. Exit Central Library
                ''')

                user = input("Enter Your Choise : ")

                if user == '1':
                    b.ShowInfo()
                elif user == '2':
                    Book_Input = input("Enter the Name Of Book You Want To Add : ")
                    b.AddBook(Book_Input)
                    print("Thanks For Adding The Book")
                elif user == '3':
                    print("1. Go to HTML Library")
                    print("2. Go to Python Library")
                    lib = input("Enter Your Choice : ")
                    if lib == '1':
                        print("Welcome To HTML Library")
                    elif lib == '2':
                        break
                elif user == '4':
                    print("Thanks For Visiting Our Library")
                    break
                else:
                    print("Please Try Again !")
    elif user == '4':
        print("Thanks For Visiting Our Library")
        break
    else:
        print("Please Try Again !")