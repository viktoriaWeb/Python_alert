import sqlite3

# Create or connect to a SQLite database
db_conn = sqlite3.connect("DB.db")
cursor = db_conn.cursor()

# Create the Orders table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Orders (
    id INTEGER PRIMARY KEY,
    created_date TEXT,
    merchant_id INTEGER
)
""")

# Create the Transactions table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Transactions (
    id INTEGER PRIMARY KEY,
    created_date TEXT,
    transaction_type TEXT,
    order_id INTEGER,
    transaction_status TEXT,
    FOREIGN KEY (order_id) REFERENCES Orders(id)
)
""")

# Sample data for Orders
orders_data = [
    ("5/15/2023 17:48", 1),
    ("5/16/2023 1:06", 2),
    ("5/16/2023 12:46", 2),
    ("5/16/2023 22:44", 3)
]

# Insert sample Orders data
cursor.executemany("INSERT INTO Orders (created_date, merchant_id) VALUES (?, ?)", orders_data)
db_conn.commit()

# Sample data for Transactions
transactions_data = [
    ("5/15/2023 17:48", "auth", 1, "success"),
    ("5/16/2023 1:06", "auth", 2, "success"),
    ("5/16/2023 12:46", "auth", 3, "success"),
    ("5/16/2023 22:44", "auth", 4, "success"),
    ("5/19/2023 18:57", "settle", 1, "fail"),
    ("5/20/2023 3:50", "void", 2, "success"),
    ("5/21/2023 7:21", "settle", 3, "success")
]

# Insert sample Transactions data
cursor.executemany("INSERT INTO Transactions (created_date, transaction_type, order_id, transaction_status) VALUES (?, ?, ?, ?)", transactions_data)
db_conn.commit()

# Close the database connection
db_conn.close()

print("Tables populated with sample data.")
