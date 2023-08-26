
from os import system
clear = lambda : system("cls")

from pickle import load
with open("books.info","rb") as books_info: 
    books = load(books_info)

def add_to_excell():
    pass

def add_book():
    clear()
    global books       
    book = {}
    book ["title"] = input("Enter  title of book :")
    book ["author"] = input ("Enter author of book:")
    book [ "pages"]= int(input ( "enter pages of the book: "))
    book ["price"] = float(input ("enter price of the book:"))
    book ["isbn"] = input (" Enter ISBN of the book:")
    books.append(book)
    input ("press any key:")

def print_book():
    
    print ( "---------------------------------")
    print(f"Title : {book ['title']}")
    print(f"Author : {book ['author']}")
    print(f"Pages : {book ['pages']}")
    print(f"Price : {book ['price']}")
    print(f"ISBN : {book ['isbn']}")
    print ( "---------------------------------") 


def list_books():
    clear()
    for book in books:
       
        print(f"Title : {book ['title']}")
        print(f"Author : {book ['author']}")
        print(f"Pages : {book ['pages']}")
        print(f"Price : {book ['price']}")
        print(f"ISBN : {book ['isbn']}")
        print ( "---------------------------------") 
    input ("press any key:")

def find_book():
    clear()
 # item_key = input("What is your search basis? : (title/author/pages/price/isbn)")
    isbn = input ("enter ISBN to find your book:")
    for book in books:
        if book ["isbn"]== isbn : 
           print ( "---------------------------------")
           print(f"Title : {book ['title']}")
           print(f"Author : {book ['author']}")
           print(f"Pages : {book ['pages']}")
           print(f"Price : {book ['price']}")
           print(f"ISBN : {book ['isbn']}")
           print ( "---------------------------------")
           input ("press any key:")
           break
    else :
        input("this book is not in our store!")    

def delete_book():
    clear()
    isbn = input ("enter ISBN to delete book:")
    for book in books:
        if book ["isbn"] == isbn:
            books.remove (book)
            input ("books has been deleated successfully")
            
            break
    else:
        input("this book is not in books databass!")

def save_books():
    clear()
    from pickle import dump
    with open("books.info","wb") as books_info:
        dump(books,books_info)
        input("books has been saved successfully!")
