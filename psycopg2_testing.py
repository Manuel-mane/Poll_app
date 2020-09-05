import psycopg2

url = "postgres://kqnmmsbu:aD-BkYMGJx8JlqOcXqo5a7pHHfGvEDt3@lallah.db.elephantsql.com:5432/kqnmmsbu"
connection = psycopg2.connect(url)

cursor = connection.cursor()
cursor.execute("SELECT * FROM users")
first_user = cursor.fetchone()

print(first_user)

connection.close()