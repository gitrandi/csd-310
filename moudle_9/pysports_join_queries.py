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

    # INNER JOIN query
    inner_join_query = """
    SELECT player.player_id, player.first_name, player.last_name, player.team_id, team.team_name
    FROM player
    INNER JOIN team ON player.team_id = team.team_id
    """

    # Execute the INNER JOIN query
    cursor.execute(inner_join_query)

    # Display the results for INNER JOIN
    print("\n--- INNER JOIN ---")
    for (player_id, first_name, last_name, team_id, team_name) in cursor:
        print(f"Player ID: {player_id}, Name: {first_name} {last_name}, Team ID: {team_id}, Team Name: {team_name}")

    # LEFT OUTER JOIN query
    left_outer_join_query = """
    SELECT player.player_id, player.first_name, player.last_name, player.team_id, team.team_name
    FROM player
    LEFT OUTER JOIN team ON player.team_id = team.team_id
    """

    # Execute the LEFT OUTER JOIN query
    cursor.execute(left_outer_join_query)

    # Display the results for LEFT OUTER JOIN
    print("\n--- LEFT OUTER JOIN ---")
    for (player_id, first_name, last_name, team_id, team_name) in cursor:
        print(f"Player ID: {player_id}, Name: {first_name} {last_name}, Team ID: {team_id}, Team Name: {team_name}")

    # RIGHT OUTER JOIN query
    right_outer_join_query = """
    SELECT player.player_id, player.first_name, player.last_name, player.team_id, team.team_name
    FROM player
    RIGHT OUTER JOIN team ON player.team_id = team.team_id
    """

    # Execute the RIGHT OUTER JOIN query
    cursor.execute(right_outer_join_query)

    # Display the results for RIGHT OUTER JOIN
    print("\n--- RIGHT OUTER JOIN ---")
    for (player_id, first_name, last_name, team_id, team_name) in cursor:
        print(f"Player ID: {player_id}, Name: {first_name} {last_name}, Team ID: {team_id}, Team Name: {team_name}")

    # WHERE clause query
    where_clause_query = """
    SELECT player.player_id, player.first_name, player.last_name, player.team_id
    FROM player
    WHERE player.team_id = 1
    """

    # Execute the WHERE clause query
    cursor.execute(where_clause_query)

    # Display the results for WHERE clause
    print("\n--- WHERE Clause ---")
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
