import mysql.connector
from mysql.connector import Error

# Database Initialization
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Bellevue!23b",
    database="whatabook"
)
cursor = conn.cursor()

# Create Tables
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Locations (
        location_id INT AUTO_INCREMENT PRIMARY KEY,
        location_name VARCHAR(255) NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Hours (
        location_id INT,
        day VARCHAR(255),
        open_time TIME,
        close_time TIME,
        PRIMARY KEY (location_id, day),
        FOREIGN KEY (location_id) REFERENCES Locations(location_id)
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Books (
        book_id INT AUTO_INCREMENT PRIMARY KEY,
        book_name VARCHAR(255) NOT NULL,
        author VARCHAR(255) NOT NULL,
        details TEXT
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Users (
        user_id INT AUTO_INCREMENT PRIMARY KEY,
        email VARCHAR(255) NOT NULL,
        first_name VARCHAR(255) NOT NULL,
        last_name VARCHAR(255) NOT NULL
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS Wishlist (
        user_id INT,
        book_id INT,
        PRIMARY KEY (user_id, book_id),
        FOREIGN KEY (user_id) REFERENCES Users(user_id),
        FOREIGN KEY (book_id) REFERENCES Books(book_id)
    )
''')

# Function to display the main menu
def show_menu():
    print("Menu:")
    print("1. View Books")
    print("2. View Store Locations")
    print("3. My Account")
    print("4. Exit Program")

# Function to display the books
def show_books(cursor):
    cursor.execute("SELECT * FROM Books")
    books = cursor.fetchall()
    print("Books:")
    for book in books:
        print(f"{book[0]}. {book[1]} by {book[2]} - {book[3]}")

# Function to display store locations
def show_locations(cursor):
    cursor.execute("SELECT * FROM Locations")
    locations = cursor.fetchall()
    print("Store Locations:")
    for location in locations:
        print(f"{location[0]}. {location[1]}")

# Function to validate user and return user_id
def validate_user(cursor):
    user_id = input("Enter your user_id: ")
    cursor.execute("SELECT * FROM Users WHERE user_id=%s", (user_id,))
    user = cursor.fetchone()
    if user:
        return user_id
    else:
        print("Invalid user_id. Please try again.")
        return validate_user(cursor)

# Function to display account menu
def show_account_menu():
    print("Account Menu:")
    print("1. Wishlist")
    print("2. Add Book")
    print("3. Main Menu")

# Function to display user's wishlist
def show_wishlist(cursor, user_id):
    cursor.execute("SELECT Books.* FROM Books INNER JOIN Wishlist ON Books.book_id = Wishlist.book_id WHERE Wishlist.user_id=%s", (user_id,))
    wishlist = cursor.fetchall()
    print("Wishlist:")
    for book in wishlist:
        print(f"{book[0]}. {book[1]} by {book[2]} - {book[3]}")

# Function to display books not in the user's wishlist
def show_books_to_add(cursor, user_id):
    cursor.execute("SELECT * FROM Books WHERE book_id NOT IN (SELECT book_id FROM Wishlist WHERE user_id=%s)", (user_id,))
    books_to_add = cursor.fetchall()
    print("Books to Add:")
    for book in books_to_add:
        print(f"{book[0]}. {book[1]} by {book[2]} - {book[3]}")

# Function to add a book to the user's wishlist
def add_book_to_wishlist(cursor, user_id, book_id):
    cursor.execute("INSERT INTO Wishlist (user_id, book_id) VALUES (%s, %s)", (user_id, book_id))
    print("Book added to Wishlist!")

# Main Program
while True:
    show_menu()
    choice = input("Enter your choice: ")

    if choice == '1':
        show_books(cursor)
    elif choice == '2':
        show_locations(cursor)
    elif choice == '3':
        user_id = validate_user(cursor)
        while True:
            show_account_menu()
            account_choice = input("Enter your choice: ")

            if account_choice == '1':
                show_wishlist(cursor, user_id)
            elif account_choice == '2':
                show_books_to_add(cursor, user_id)
                book_id_to_add = input("Enter the book_id to add to your Wishlist: ")
                add_book_to_wishlist(cursor, user_id, book_id_to_add)
            elif account_choice == '3':
                break
            else:
                print("Invalid choice. Please try again.")
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please try again.")

# Close the database connection
conn.close()
