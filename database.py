import sqlite3

conn = sqlite3.connect("mydb.db")
c = conn.cursor()

def read_users():
    c.execute("SELECT * FROM users")
    for user in c.fetchall():
        print(user)
        print("===================")

def insert_user(firstName, lastName, age, salary):
    c.execute("INSERT INTO users VALUES (?, ?, ?, ?)",(firstName, lastName, age, salary))
    conn.commit()

def update_user(firstName,salary):
    c.execute("""UPDATE users SET salary = :salary
    WHERE first_name = :firstName
    """,{'firstName':firstName,'salary':salary})
    conn.commit()

def delete_user(firstName,lastName):
    c.execute("DELETE FROM users WHERE first_name = :firstName OR last_name = :lastName",{'firstName':firstName,'lastName':lastName})
    conn.commit()

#insert_user("Arman","Avetisyan",26,1525.75)
#update_user("Arman",1850)
delete_user("Jacob","Frye")
read_users()

conn.close()