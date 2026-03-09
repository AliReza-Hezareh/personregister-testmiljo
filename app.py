import sqlite3
import os
from faker import Faker


fake = Faker()

def init_database():
    db_path = os.getenv('DATABASE_PATH', 'test_users.db')
    if os.path.exists(db_path):
        os.remove(db_path)
        
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """)
    

    cursor.execute('SELECT COUNT(*) FROM users')
    count = cursor.fetchone()[0]

    if count == 0:
        test_users = [
            ('Sara Lind', 'sara@test.se'),
            ('Omar Hassan', 'omar@test.se'),
            ('Linnea Karlsson', 'linnea@test.se'),
            ('Erik Svensson', 'erik@test.se'),
            ('Fatima Ali', 'fatima@test.se')
        ]

        cursor.executemany(
            'INSERT INTO users (name, email) VALUES (?, ?)', test_users
        )

        print("Database initialized with test users")
    else:
        print(f"Database already contains {count} users")

    conn.commit()
    conn.close()
    
def reset_database():
    db_path = os.getenv('DATABASE_PATH', 'test_users.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("DELETE FROM users")

    conn.commit()
    conn.close()
    
def generate_fake_users(count):
    db_path = os.getenv('DATABASE_PATH', 'test_users.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
     # RESET DATABASE
    cursor.execute("DELETE FROM users")
    # Reset auto increment ID
    cursor.execute("DELETE FROM sqlite_sequence WHERE name='users'")


    for _ in range(count):
        name = fake.name()
        email = fake.email()

        cursor.execute(
            "INSERT INTO users (name, email) VALUES (?, ?)",
            (name, email)
        )

    conn.commit()
    conn.close()

    print(f"{count} fake users created")

def generate_test_users():
    db_path = os.getenv('DATABASE_PATH', 'test_users.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    users = [
        ("Sara Lind", "sara@test.se"),
        ("Omar Hassan", "omar@test.se"),
        ("Linnea Karlsson", "linnea@test.se"),
        ("Erik Svensson", "erik@test.se"),
        ("Fatima Ali", "fatima@test.se")
    ]

    cursor.executemany(
        "INSERT INTO users (name, email) VALUES (?, ?)",
        users
    )

    conn.commit()
    conn.close()

    print("Synthetic test users generated.")
    
    
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
    

    
def anonymize_user():
    db_path = os.getenv('DATABASE_PATH', 'test_users.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("UPDATE users SET name = 'Anonymous User', email = 'hidden@test.se'")

    conn.commit()
    conn.close()

    print("All user names have been anonymized (GDPR compliant)")
    #eget funktion som testar anonymisering av data, i det här fallet byter vi ut alla namn mot "Anonym Användare".
    
    
def add_user(name, email):
    db_path = os.getenv('DATABASE_PATH', 'test_users.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO users (name, email) VALUES (?, ?)",
        (name, email)
    )

    conn.commit()
    conn.close()

    print("User added successfully")


def clear_test_data():
    db_path = os.getenv('DATABASE_PATH', 'test_users.db')
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute('DELETE FROM users')

    conn.commit()
    conn.close()

    print("All test data has been cleared (GDPR compliant)")




if __name__ == "__main__":
    init_database()
    reset_database()
    generate_fake_users(10)
    display_users()

    print("\nContainer is running. Press Ctrl+C to exit.")

    try:
        while True:
            pass
    except KeyboardInterrupt:
        print("\nShutting down...")