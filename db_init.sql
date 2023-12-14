-- Create the 'books' table
CREATE TABLE books (
    book_id INT PRIMARY KEY,
    title VARCHAR(255),
    genre VARCHAR(50),
    author VARCHAR(100)
);

-- Insert data into the 'books' table
INSERT INTO books (book_id, title, genre, author)
VALUES
    (1, 'The Enigma Code', 'Thriller', 'Alexander Smith'),
    (2, 'Beyond the Stars', 'Space', 'Jonathan Carter'),
    (3, 'Whispers in the Dark', 'Suspense', 'Emily Davis'),
    (4, 'Lost in Time', 'Time-travel', 'Michael Anderson'),
    (5, 'Eternal Love', 'Romance', 'Sophia Miller'),
    (6, 'The Quantum Conundrum', 'Mystery', 'David Turner'),
    (7, 'City of Shadows', 'Detective', 'Jessica Knight'),
    (8, 'Forgotten Realms', 'Fantasy', 'Ryan Mitchel'),
    (9, 'Silent Harmony', 'Romance', 'Oliva Reed');

-- Create the 'store' table
CREATE TABLE store (
    store_id INT PRIMARY KEY,
    store_name VARCHAR(255)
);

-- Insert data into the 'store' table
INSERT INTO store (store_id, store_name)
VALUES (1, 'Bookstore');

-- Create the 'users' table
CREATE TABLE users (
    user_id INT PRIMARY KEY,
    user_name VARCHAR(255)
);

-- Insert data into the 'users' table
INSERT INTO users (user_id, user_name)
VALUES
    (1, 'Ram Valentine'),
    (2, 'Randi Jabroni'),
    (3, 'Mike Elf');

-- Create the 'wishlist' table
CREATE TABLE wishlist (
    wishlist_id INT PRIMARY KEY,
    user_id INT,
    book_id INT,
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (book_id) REFERENCES books(book_id)
);

-- Insert data into the 'wishlist' table
INSERT INTO wishlist (wishlist_id, user_id, book_id)
VALUES
    (1, 1, 3),
    (2, 2, 7),
    (3, 3, 6);
