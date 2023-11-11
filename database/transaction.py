import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect("health_fitness_app.db")
cursor = conn.cursor()

try:
    # Begin the transaction
    conn.execute("BEGIN")

    # Example: Insert a new user with age (assuming you have a table named 'Users')
    new_user = {
        "UserName": "JohnDoe",
        "Age": -25,  # Negative age (intentional to cause a transaction failure)
        "Gender": "Male",
        # Add other user attributes here
    }

    # Check for negative age
    if new_user["Age"] < 0:
        raise ValueError("Age cannot be negative")

    cursor.execute("""
    INSERT INTO Users (UserName, Age, Gender)
    VALUES (?, ?, ?);
    """, (new_user["UserName"], new_user["Age"], new_user["Gender"]))

    # Commit the transaction
    conn.commit()
    print("User insertion successful.")

except sqlite3.Error as e:
    # Handle the error and rollback the transaction on failure
    print("Error:", e)
    conn.rollback()
    print("User insertion failed due to negative age.")

finally:
    # Close the database connection
    conn.close()
