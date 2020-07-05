from utils import database

User_choice= """
Enter: 
- 'a' to add a new book
- 'l' to list all the books
- 'r' to mark a book as read
- 'd' to delete a book
- 'q' to quit 
 
Your choice: """

def menu():
    database.create_book_table()
    user_input= input (User_choice)
    while user_input != 'q':
        if user_input == 'a':
            prompt_add_book()
        elif user_input == 'l':
            list_all_books()
        elif user_input == 'r':
            mark_as_read()
        elif user_input == 'd':
            delete_the_book()

        user_input = input (User_choice)


def prompt_add_book():
    name = input("Enter the book's name to add: ")
    author = input("Enter the author's name: ")

    database.add_book(name,author)


def list_all_books():
    books = database.get_all_books()
    for book in books:
        print(book)


def mark_as_read():
    name= input("Enter the name of the book that you just finished reading: ")
    database.mark_book_as_read(name)

def delete_the_book():
    name = input("Enter the name of the book that you want to delete: ")
    database.delete_book(name)


menu()
