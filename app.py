import sqlite3
import os


def init_database():
    db_path = os.getenv('DATABASE_PATH', 'test_users.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL
        )
    ''')

    cursor.execute('SELECT COUNT(*) FROM users')
    count = cursor.fetchone()[0]

    if count == 0:
        test_users = [
            ('Anna Andersson', 'anna@test.se'),
            ('Bo Bengtsson', 'bo@test.se')
        ]

        cursor.executemany(
            'INSERT INTO users (name, email) VALUES (?, ?)', test_users
        )

        print("Database initialized with test users")
    else:
        print(f"Database already contains {count} users")

    conn.commit()
    conn.close()


def display_users():
    db_path = os.getenv('DATABASE_PATH', 'test_users.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM users')
    users = cursor.fetchall()

    print("\nCurrent users in database:")

    for user in users:
        print(f"ID: {user[0]}, Name: {user[1]}, Email: {user[2]}")

    conn.close()


def clear_test_data():
    db_path = os.getenv('DATABASE_PATH', 'test_users.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute('DELETE FROM users')

    conn.commit()
    conn.close()

    print("All test data has been cleared (GDPR compliant)")


def anonymize_data():
    db_path = os.getenv('DATABASE_PATH', 'test_users.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute('UPDATE users SET name = "Anonym Användare"')

    conn.commit()
    conn.close()

    print("All user names have been anonymized (GDPR compliant)")


if __name__ == "__main__":
    init_database()
    display_users()

    print("\nContainer is running. Press Ctrl+C to exit.")

    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("\nShutting down...")