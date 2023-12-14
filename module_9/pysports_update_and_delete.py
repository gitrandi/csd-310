import mysql.connector
from mysql.connector import Error

connection = mysql.connector.connect(host="localhost",
user="root",
passwd="Basecode!257s",
db="whatabook")

try:
    # Connect to the MySQL database
    db = mysql.connector.connect(**config)
    print("\nConnected to the MySQL database")

    # Create a cursor
    cursor = db.cursor()

    # Insert a new record for Team Gandalf
    new_player_data = ('Frodo', 'Baggins', 1)  
    add_player_query = """
    INSERT INTO player (first_name, last_name, team_id)
    VALUES (%s, %s, %s)
    """
    cursor.execute(add_player_query, new_player_data)
    db.commit()
    print(f"Player added successfully for Team Gandalf: {new_player_data}")

    # Select query with INNER JOIN to display player records (verify insertion)
    select_query = """
    SELECT player.player_id, player.first_name, player.last_name, team.team_name
    FROM player
    INNER JOIN team ON player.team_id = team.team_id
    """
    cursor.execute(select_query)
    print("\n--- Player Records (After Insertion) ---")
    for (player_id, first_name, last_name, team_name) in cursor:
        print(f"Player ID: {player_id}, Name: {first_name} {last_name}, Team: {team_name}")

    # Update the newly inserted record to Team Sauron
    update_query = """
    UPDATE player
    SET team_id = 2
    WHERE first_name = 'Frodo' AND last_name = 'Baggins'
    """
    cursor.execute(update_query)
    db.commit()
    print("\nPlayer record updated successfully to Team Sauron")

    # Select query with INNER JOIN to display the updated record
    cursor.execute(select_query)
    print("\n--- Player Records (After Update) ---")
    for (player_id, first_name, last_name, team_name) in cursor:
        print(f"Player ID: {player_id}, Name: {first_name} {last_name}, Team: {team_name}")

    # Delete the updated record
    delete_query = """
    DELETE FROM player
    WHERE first_name = 'Frodo' AND last_name = 'Baggins'
    """
    cursor.execute(delete_query)
    db.commit()
    print("\nPlayer record deleted successfully")

    # Select query with INNER JOIN to display all player records
    cursor.execute(select_query)
    print("\n--- Player Records (After Deletion) ---")
    for (player_id, first_name, last_name, team_name) in cursor:
        print(f"Player ID: {player_id}, Name: {first_name} {last_name}, Team: {team_name}")

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    # Close the cursor and connection
    if 'cursor' in locals() and cursor:
        cursor.close()
    if 'db' in locals() and db:
        db.close()
        print("\nConnection to the MySQL database closed")
