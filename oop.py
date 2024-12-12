


'''
Basic: Create a class called Car with attributes brand and color. 
Instantiate an object of the Car class and print its attributes.

'''
class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

my_car = Car('Audi', 'Red')
print('Car Details:')
print(f'Brand:{my_car.brand}')
print(f'Color:{my_car.color}')


'''
Intermediate: Add a method called start_engine to the Car class that prints a message saying the 
engine of the car has started. Create an instance of Car and call the method.

'''


class Car:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def start_engine(self):
        print(f'The {self.color} {self.brand} engine has started.')

car1 = Car('Mazda', 'White')
print(f' My {car1.brand} car is {car1.color}')

car2 = Car('Audi', 'Maroon')
car2.start_engine()


'''
Advanced: Create a class called BankAccount with attributes account_number and balance. Add methods to:
Deposit an amount.
Withdraw an amount (only if sufficient balance exists).
Print the account balance.
'''

class BankAccount:
    def __init__(self, account_number, balance):
        self.account_balance = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance +=amount
        print(f'You have deposited {amount} shillings.')
    
    def withdraw(self, amount):
        if self.balance >= 5000:
            self.balance -= amount
        else:
            print('Insufficient Balance.')

    def check_balance(self):
        print(f'Your account balance is {self.balance}')

account1 =BankAccount(1234, 10000)

account1.deposit(2000)
account1.withdraw(1000)
account1.check_balance()



''' Challenge:
Implement a class called Library that manages a collection of books. 
Each book has a title, author, and available status. The Library class should have methods to:

Add a book to the library.
Remove a book from the library.
Check if a book is available by title.
Borrow a book (mark it as unavailable if it’s available).
Return a book (mark it as available again if it was borrowed)'''


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_available = True

    def __str__(self):
     return f"{self.title} by {self.author}"



class Library:
    def __init__(self):
        self.books = []  # List to store the collection of books

    def add_book(self, title, author):
        new_book = Book(title, author)
        self.books.append(new_book)
        print(f"Added {new_book} to the library.")

    def remove_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                print(f"Removed {book} from the library.")
                return
        print(f"Book titled '{title}' not found in the library.")

    def check_availability(self, title):
        for book in self.books:
            if book.title == title:
                return book.is_available
        print(f"Book titled '{title}' not found in the library.")
        return False

    def borrow_book(self, title):
        for book in self.books:
            if book.title == title:
                if book.is_available:
                    book.is_available = False
                    print(f"You have successfully borrowed {book}.")
                else:
                    print(f"{book} is currently unavailable.")
                return
        print(f"Book titled '{title}' not found in the library.")

    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                if not book.is_available:
                    book.is_available = True
                    print(f"You have successfully returned {book}.")
                else:
                    print(f"{book} was not borrowed.")
                return
        print(f"Book titled '{title}' not found in the library.")


# Example usage:
library = Library()

# Add books
library.add_book("To Kill a Mockingbird", "Harper Lee")
library.add_book("1984", "George Orwell")

# Check availability
print("Is '1984' available?", library.check_availability("1984"))

# Borrow a book
library.borrow_book("1984")
print("Is '1984' available?", library.check_availability("1984"))

# Return a book
library.return_book("1984")
print("Is '1984' available?", library.check_availability("1984"))

# Remove a book
library.remove_book("1984")




        


