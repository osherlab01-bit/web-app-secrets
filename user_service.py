import mysql.connector

def get_user(username):
    conn = mysql.connector.connect(host='localhost', user='root', password='root123')
    cursor = conn.cursor()
    # VULNERABLE: SQL Injection
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)
    return cursor.fetchall()
