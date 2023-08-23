import csv
import sqlite3

# Create or connect to a SQLite database
db_conn = sqlite3.connect("DB.db")
cursor = db_conn.cursor()

# Create the Orders table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Orders (
    order_id INTEGER PRIMARY KEY,
    created_date TEXT,
    merchant_id INTEGER
)
""")

# Create the Transactions table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Transactions (
    transaction_id INTEGER PRIMARY KEY,
    created_date TEXT,
    transaction_type TEXT,
    order_id INTEGER,
    transaction_status TEXT,
    FOREIGN KEY (order_id) REFERENCES Orders(id)
)
""")

# Sample data for Orders
# Insert sample Orders data
with open('Orders.csv', 'r', newline='') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        cursor.execute("""
        INSERT INTO Orders (order_id, created_date, merchant_id)
        VALUES (?, ?, ?)
        """, 
        (row['order_id'],row['created_date'],row['merchant_id']))

db_conn.commit()


# Insert sample Transactions data
with open('Transactions.csv', 'r', newline='') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        cursor.execute("""
        INSERT INTO Transactions (created_date,order_id,transaction_type,transaction_status)
        VALUES (?, ?, ?, ?)
        """, 
        (row['created_date'],row['order_id'],row['transaction_type'],row['transaction_status']))

db_conn.commit()

# Close the database connection
db_conn.close()

print("Tables populated with sample data.")
