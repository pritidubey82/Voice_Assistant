import sqlite3

# Connect to the database (or create it if it doesn't exist)
conn = sqlite3.connect("jarvis.db")
cursor = conn.cursor()

# Create the table if it doesn't already exist
query = """
CREATE TABLE IF NOT EXISTS sys_command(
    id INTEGER PRIMARY KEY, 
    name VARCHAR(100), 
    path VARCHAR(1000)
)
"""
cursor.execute(query)

# Insert the 'word' command into the sys_command table
query_word = """
INSERT INTO sys_command VALUES (
    null, 
    'word', 
    'C:\\\\Program Files\\\\Microsoft Office\\\\root\\\\Office16'
)
"""
cursor.execute(query_word)

# Insert the 'vscode' command into the sys_command table
query_vscode = """
INSERT INTO sys_command VALUES (
    null, 
    'vscode', 
    'C:\\Users\\Priti\\AppData\\Local\\Programs\\Microsoft VS Code'
)
"""
cursor.execute(query_vscode)

# Commit the changes to save them to the database
conn.commit()

# Close the connection (optional but recommended)
conn.close()

print("Entries successfully added to the database!")
