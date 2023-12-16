import sys
import mysql.connector
from mysql.connector import errorcode

# Database configuration
DB_CONFIG = {
    "user": "whatabook_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "whatabook",
    "raise_on_warnings": True
}

def show_menu():
    print("\n  -- Main Menu --")
    print("    1. View Books\n    2. View Store Locations\n    3. My Account\n    4. Exit Program")

    try:
        choice = int(input('      <Example enter: 1 for book listing>: '))
        return choice
    except ValueError:
        print("\n  Invalid number, program terminated...\n")
        sys.exit(0)

def execute_query(cursor, query):
    cursor.execute(query)
    return cursor.fetchall()

def show_books(cursor):
    query = "SELECT book_id, book_name, author, details FROM book"
    books = execute_query(cursor, query)

    print("\n  -- DISPLAYING BOOK LISTING --")
    for book in books:
        print(f"  Book ID: {book[0]}\n  Book Name: {book[1]}\n  Author: {book[2]}\n")

def show_locations(cursor):
    query = "SELECT store_id, locale FROM store"
    locations = execute_query(cursor, query)

    print("\n  -- DISPLAYING STORE LOCATIONS --")
    for location in locations:
        print(f"  Locale: {location[1]}\n")

def validate_user():
    try:
        user_id = int(input('\n      Enter a customer ID <Example 1 for user_id 1>: '))
        if not 0 <= user_id <= 3:
            print("\n  Invalid customer number, program terminated...\n")
            sys.exit(0)
        return user_id
    except ValueError:
        print("\n  Invalid number, program terminated...\n")
        sys.exit(0)

def show_account_menu():
    try:
        print("\n      -- Customer Menu --")
        print("        1. Wishlist\n        2. Add Book\n        3. Main Menu")
        account_option = int(input('        <Example enter: 1 for wishlist>: '))
        return account_option
    except ValueError:
        print("\n  Invalid number, program terminated...\n")
        sys.exit(0)

def show_wishlist(cursor, user_id):
    query = f"SELECT user.user_id, user.first_name, user.last_name, book.book_id, book.book_name, book.author " \
            f"FROM wishlist " \
            f"INNER JOIN user ON wishlist.user_id = user.user_id " \
            f"INNER JOIN book ON wishlist.book_id = book.book_id " \
            f"WHERE user.user_id = {user_id}"
    
    wishlist = execute_query(cursor, query)

    print("\n        -- DISPLAYING WISHLIST ITEMS --")
    for book in wishlist:
        print(f"        Book Name: {book[4]}\n        Author: {book[5]}\n")

def show_books_to_add(cursor, user_id):
    query = f"SELECT book_id, book_name, author, details " \
            f"FROM book " \
            f"WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id = {user_id})"
    
    books_to_add = execute_query(cursor, query)

    print("\n        -- DISPLAYING AVAILABLE BOOKS --")
    for book in books_to_add:
        print(f"        Book ID: {book[0]}\n        Book Name: {book[1]}\n")

def add_book_to_wishlist(cursor, user_id, book_id):
    query = f"INSERT INTO wishlist(user_id, book_id) VALUES({user_id}, {book_id})"
    execute_query(cursor, query)

def main():
    try:
        # Connect to the WhatABook database
        db = mysql.connector.connect(**DB_CONFIG)
        cursor = db.cursor()

        print("\n  Welcome to the WhatABook Application! ")

        user_selection = show_menu()

        while user_selection != 4:
            if user_selection == 1:
                show_books(cursor)
            elif user_selection == 2:
                show_locations(cursor)
            elif user_selection == 3:
                my_user_id = validate_user()
                account_option = show_account_menu()

                while account_option != 3:
                    if account_option == 1:
                        show_wishlist(cursor, my_user_id)
                    elif account_option == 2:
                        show_books_to_add(cursor, my_user_id)
                        book_id = int(input("\n        Enter the ID of the book you want to add: "))
                        add_book_to_wishlist(cursor, my_user_id, book_id)
                        db.commit()
                        print(f"\n        Book ID: {book_id} was added to your wishlist!")

                    if not 0 <= account_option <= 3:
                        print("\n      Invalid option, please retry...")

                    account_option = show_account_menu()

            if not 0 <= user_selection <= 4:
                print("\n      Invalid option, please retry...")

            user_selection = show_menu()

        print("\n\n  Program terminated...")

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("  The supplied username or password are invalid")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("  The specified database does not exist")
        else:
            print(err)

    finally:
        db.close()

if __name__ == "__main__":
    main()
