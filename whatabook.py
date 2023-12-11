import mysql.connector
from mysql.connector import Error

def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            passwd="Basecode!257s",
            database="whatabook"
        )
        return connection, connection.cursor()
    except Error as e:
        print(f"Error connecting to the database: {e}")
        return None, None

def close_database_connection(connection, cursor):
    if connection.is_connected():
        cursor.close()
        connection.close()

def create_tables():
    connection, cursor = connect_to_database()
    if connection:
        try:
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS User (
                    UserID INT AUTO_INCREMENT PRIMARY KEY,
                    Email VARCHAR(255) NOT NULL,
                    FirstName VARCHAR(255) NOT NULL,
                    LastName VARCHAR(255) NOT NULL
                )
            ''')

            # Create other tables (Book, Wishlist, Location) similarly...

        except Error as e:
            print(f"Error creating tables: {e}")
        finally:
            close_database_connection(connection, cursor)

def register_user(email, first_name, last_name):
    connection, cursor = connect_to_database()
    if connection:
        try:
            cursor.execute('''
                INSERT INTO User (Email, FirstName, LastName)
                VALUES (%s, %s, %s)
            ''', (email, first_name, last_name))

            connection.commit()
        except Error as e:
            print(f"Error registering user: {e}")
        finally:
            close_database_connection(connection, cursor)

def view_books():
    connection, cursor = connect_to_database()
    if connection:
        try:
            cursor.execute('SELECT * FROM Book')
            books = cursor.fetchall()

            for book in books:
                print(book)
        except Error as e:
            print(f"Error viewing books: {e}")
        finally:
            close_database_connection(connection, cursor)

def add_to_wishlist(user_id, book_id):
    connection, cursor = connect_to_database()
    if connection:
        try:
            # Add logic to check business rules before adding to the wishlist
            cursor.execute('''
                INSERT INTO Wishlist (UserID, BookID)
                VALUES (%s, %s)
            ''', (user_id, book_id))

            connection.commit()
        except Error as e:
            print(f"Error adding to wishlist: {e}")
        finally:
            close_database_connection(connection, cursor)

def view_store_locations():
    connection, cursor = connect_to_database()
    if connection:
        try:
            cursor.execute('SELECT * FROM Location')
            locations = cursor.fetchall()

            for location in locations:
                print(location)
        except Error as e:
            print(f"Error viewing store locations: {e}")
        finally:
            close_database_connection(connection, cursor)


# Example usage:
create_tables()
register_user('user@example.com', 'John', 'Doe')
view_books()
add_to_wishlist(1, 1)  # Example wishlist addition
view_store_locations()






