class Library:
    def __init__(self, list_of_books, name):
        self.name=name
        self.list_of_books = list_of_books
        self.lendDict={}
        
    def displayBook(self):
        print(f"We have the following books in our library: {self.name}")
        for book in self.list_of_books:
            print(book)
    
    def lendBook(self, user, book):
        if book not in self.list_of_books:
            print("Sorry, we do not have that boook.")
        elif book in self.lendDict:
            print(f"Thebook is already being used by {self.lendDict[book]}")
        else:
            self.lendDict[book]=user
            print(f"You have successfully lent the book '{book}' to {user}")
    
    def addBook(self,book):
        self.list_of_books.append(book)
        print(f"The book '{book}' has been added to the library book list.")
    
    def returnBook(self, book):
        if book in self.lendDict:
            del self.lendDict[book]
            print("Book has been returned.")
        else:
            print("That book wasn't borrowed from us.")


if __name__=="__main__":
    books=Library([
        "To Kill a Mockingbird","1984","The Great Gatsby","Pride and Prejudice","The Book Thief"
    ],"Give a read")
    user_name=input("Welcome to our library! Please enter your name:")
    
    while True:
        print(f"\nHello{user_name}, Welcome to the {books.name} Library. Please choose an option:")
        print("1.Display Books\n2.Lend a Book\n3.Add a Book\n4.Return a Book\n5.Quit")
        user_choice=input("Enter your choice to continue:")
        
        if user_choice not in ["1","2","3","4","5"]:
            print("Invalid choice, please try again.")
            continue
        
        if user_choice=="1":
            books.displayBook()
        elif user_choice=="2":
            book=input("nter the name of the book you want to lend:")
            books.lendBook(user_name, book)
        elif user_choice=="3":
            book=input("Enter the name of the book you want to add:")
            books.addBook(book)
        elif user_choice=="4":
            book=input("Enter the name of the book you want to return:")
            books.returnBook(book)
        elif user_choice=="5":
            print(f"Thank you for using the library,{user_name}. Goodbye!")
            break
        