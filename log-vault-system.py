import sqlite3



# AI comment:
# In this specific code you just ran, there is no person entering data yet.
# What the mechanic (cursor) is doing here is purely the physical construction of the empty safe.


# Via sqlite3, connect to the vault ("vault.db")
connection = sqlite3.Connection("vault.db")


# Create the mechanic (cursor)
cursor = connection.cursor()


# Instruct the mechanic to build an SQL database named (LOGS)
cursor.execute("""
CREATE TABLE IF NOT EXISTS LOGS (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    message TEXT
)
""")
# The mechanic lays the foundation and with CREATE TABLE he bricks the empty rooms (id and message) into the wall



# Instruct the technician to leave a message in the table
cursor.execute("""
INSERT INTO LOGS (message)
VALUES ('MASKY is learning in the good way!')
""")



# Send the technician to retrieve the entire LOGS table
# Send the technician to retrieve only data from (Incident 1)
cursor.execute("SELECT * FROM LOGS WHERE id = 1")

# Accept all items from the mechanic
# Take the items from (Incident 1) from the mechanic
specific_logs = cursor.fetchall()

# Print the data live in the Terminal
# Print the data from (Incident 1) in the terminal
print("\n--- LASER SCAN: DATA FROM INCIDENT 1 ---")
print(specific_logs)
print("---------------------------------")



# Save everything
connection.commit()
# As soon as that empty structure is in place, the mechanic presses commit() to let the cement harden.
# The empty safe is now ready on your hard drive forever.

print("SQL-Vault build successfully!")

# disconnect
connection.close()
