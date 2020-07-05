books_file='books.txt'

def create_book_table():
    with open("books.txt",'w'):
        pass
     
def add_book(name,author):
    with open('books.txt','a') as file:
        file.write(f"{name},{author},Not read yet \n")


def get_all_books():
    with open("books.txt",'r') as file:
        lines=[line.strip().split(',')for line in file.readlines()]
    return [
        {'name':line[0], "author":line[1],"read":line[2]}
        for line in lines
    ]


def mark_book_as_read(name):
    books= get_all_books()
    for book in books:
        if book['name'] == name:
            book['read'] = "Yes, Read already"

    _save_all_books(books)

def _save_all_books(books):
    with open("books.txt",'w') as file:
        for book in books:
            file.write(f"{book['name']},{book['author']},{book['read']}\n")


def delete_book(name):
    books= get_all_books()
    books=[book for book in books if books['name'] !=name]
    _save_all_books(books)