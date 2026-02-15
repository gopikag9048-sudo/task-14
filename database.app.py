import sqlite3
def create_connection():
    return sqlite3.connect("users.db")
def create_table(conn):
    conn.execute("CREATE TABLE IF NOT EXISTS users(id INTEGER PRIMARY KEY AUTOINCREMENT,name TEXT NOT NULL,age INTEGER,email TEXT UNIQUE)")
    conn.commit()
def insert_user(conn,name,age,email):
    conn.execute("INSERT INTO users(name,age,email)VALUES(?,?,?)",(name,age,email))
    conn.commit()
def fetch_users(conn):
    cursor=conn.execute("SELECT*FROM users")
    records=cursor.fetchall()
    print("ID|Name|Age|Email")
    print("-"*30)
    for row in records:
        print(f"{row[0]}|{row[1]}|{row[2]}|{row[3]}")
def update_user(conn,user_id,name,age,email):
    conn.execute("UPDATE users SET name=?,age=?,email=? WHERE id=?",(name,age,email,user_id))
    conn.commit()
def delete_user(conn,user_id):
    conn.execute("DELETE FROM users WHERE id=?",(user_id,))
    conn.commit()
def main():
    conn=create_connection()
    create_table(conn)
    while True:
        print("1.Insert 2.View 3.Update 4.Delete 5.Exit")
        choice=input("Enter choice:")
        if choice=="1":
            name=input("Name:")
            age=int(input("Age:"))
            email=input("Email:")
            try:
                insert_user(conn,name,age,email)
                print("Inserted")
            except sqlite3.IntegrityError:
                print("Email must be unique")
        elif choice=="2":
            fetch_users(conn)
        elif choice=="3":
            user_id=int(input("User ID:"))
            name=input("New Name:")
            age=int(input("New Age:"))
            email=input("New Email:")
            update_user(conn,user_id,name,age,email)
            print("Updated")
        elif choice=="4":
            user_id=int(input("User ID:"))
            delete_user(conn,user_id)
            print("Deleted")
        elif choice=="5":
            conn.close()
            print("Closed")
            break
        else:
            print("Invalid")
if __name__=="__main__":
    main()