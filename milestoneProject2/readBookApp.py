
from utils import database


USERCHOICE = """
Enter:
- 'a' to add a new book
- 'l' to list all books
- 'r' to mark a book as read
- 'd' to delete a book
- 'q' to quit
Your choice: """


def menu():
    database.createbooktable()
    userinput = input(USERCHOICE)
    while userinput != 'q':
        if userinput == 'a':
            promptaddbook()
        elif userinput == 'l':
            listbooks()
        elif userinput == 'r':
            promptreadbook()
        elif userinput == 'd':
            promptdeletebook()

        userinput = input(USERCHOICE)


def promptaddbook():
    name = input('Enter the new book name: ')
    author = input('Enter the new book author: ')

    database.addbooks(name, author)


def listbooks():
    for book in database.getallbooks():
        if book['read']:
            read='Yes'
        else:
            read='No'
        print(f"{book['name']} by {book['author']} — Read: {read}")


def promptreadbook():
    name = input('Enter the name of the book you just finished reading: ')
    author=input('Enter the author of the book you just finished reading: ')


    database.markasread(name,author)


def promptdeletebook():
    name = input('Enter the name of the book you wish to delete: ')
    author = input('Enter the author of the book you just finished reading: ')
    database.deletebook(name,author)


menu()

