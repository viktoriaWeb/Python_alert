import sqlite3
import requests

TG_TOKEN = '<>'
bot_name = 'https://t.me/AlertPython3000Bot'

# Create or connect to a SQLite database
db_conn = sqlite3.connect("DB.db")
cursor = db_conn.cursor()
channel_id = '-1001701550581'


# Define the query
query = """

SELECT 
count(hanging_orders.order_id) as hanging_orders_count,
o.merchant_id 
from (SELECT  DISTINCT order_id
from Transactions
where 
datetime(created_date) < strftime('%Y-%m-%d %H:%M:%S', 'now', '-7 days') 
and datetime(created_date) > strftime('%Y-%m-%d %H:%M:%S', 'now', '-10 days')
and transaction_type = 'auth'
EXCEPT
SELECT  DISTINCT order_id
from Transactions
where datetime(created_date) > strftime('%Y-%m-%d %H:%M:%S', 'now', '-7 days')
and transaction_type != 'auth') as hanging_orders
join Orders o on o.order_id = hanging_orders.order_id
group by o.merchant_id

"""

# Execute the query
result = cursor.execute(query)

# Fetch all rows
query_result = result.fetchall()
# Fetch column names
column_names = [description[0] for description in result.description]

# Close the database connection
db_conn.close()

# Print column names
print("\t".join(column_names))

# Print the result
alerts = [dict(zip(column_names, row)) for  row in query_result]

data = '\n'.join(map(str, alerts))
alert_message = f"Alerts! hanging orders found: {data}"



def send_message(message, channel_id):
    payload = {
        "chat_id": channel_id,
        "text": message
    }
    url = f"https://api.telegram.org/bot{TG_TOKEN}/sendMessage"
    response = requests.post(url, json=payload)
    return response

send_message(alert_message, channel_id)