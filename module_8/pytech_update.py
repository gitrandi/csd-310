import mysql.connector

# Database configuration
config = {
    'user': 'randi',
    'password': 'Basecode!257s',
    'host': 'localhost',
    'database': 'pysports',
    'raise_on_warnings': True,
}

try:
    # Connect to the MySQL database
    db = mysql.connector.connect(**config)
    print("\nConnected to the MySQL database")

    # Create a cursor
    cursor = db.cursor()

    # SELECT query for the team table
    team_query = "SELECT team_id, team_name, mascot FROM team"

    # Execute the team query
    cursor.execute(team_query)

    # Display the results for the team table
    print("\n--- Team Table ---")
    for (team_id, team_name, mascot) in cursor:
        print(f"Team ID: {team_id}, Team Name: {team_name}, Mascot: {mascot}")

    # SELECT query for the player table
    player_query = "SELECT player_id, first_name, last_name, team_id FROM player"

    # Execute the player query
    cursor.execute(player_query)

    # Display the results for the player table
    print("\n--- Player Table ---")
    for (player_id, first_name, last_name, team_id) in cursor:
        print(f"Player ID: {player_id}, Name: {first_name} {last_name}, Team ID: {team_id}")

except mysql.connector.Error as err:
    print(f"Error: {err}")

finally:
    # Close the cursor and connection
    if 'cursor' in locals() and cursor:
        cursor.close()
    if 'db' in locals() and db:
        db.close()
        print("\nConnection to the MySQL database closed")
