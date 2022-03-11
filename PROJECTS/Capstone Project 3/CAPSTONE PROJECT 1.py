import sqlite3
#Creating a database for the book store
conn = sqlite3.connect('ebookstore.db')
c = conn.cursor()#creating a cursor object
#Creating the Table
#c.execute('''CREATE TABLE books(
#               id INTEGER PRIMARY KEY,
#                Title TEXT,
#               Author TEXT,
#               Qty INTEGER
#  ) ''')
#BOOK ENTRIES-Populating the Bookstore table

#c.execute("INSERT INTO books VALUES (3001,'A Tale of Two Cities','Charles Dickens',30)")
#c.execute("INSERT INTO books VALUES(3002,'Harry Potter and the Philosopher Stone','J.K Rowling',40)")
#c.execute("INSERT INTO books VALUES(3003,'The Lion, the Witch and the Wardrobe','C.S Lewis',25)")
#c.execute("INSERT INTO books VALUES(3004,'The Lord of the Rings','J.R.R Tolkien',37)")
#c.execute("INSERT INTO books VALUES(3005,'Alice Wonderland','Lewis Carroll',12)")

#To add more books into the database User will need to execute the code above with the new details for books
#Will need to comment out the execute commands above such that we wont get an error of recreating the books table
def view():
    c.execute("SELECT * FROM books")
    rows=c.fetchall()
    conn.close()
    return rows #To check all the Book Entries that have been entered into the Database ,
# USER can execute the above  to retrieve
#Defining a search and delete  criteria
def search (id="",title="",Author="", Qty=""):
    c.execute("SELECT*FROM books WHERE if=? OR title=? OR Author=? OR Qty=?")
    rows=c.fetchall()
    conn.close()
    return rows

def delete(id):
    c.execute("DELETE FROM books WHERE id=?",(id))
    conn.commit()
    conn.close()
    

#UPDATING BOOK ENTRIES
def update(id="",title="",Author="", Qty=""):
    c.execute("UPDATE books SET title=?,Author=?, Qty=? WHERE id=?",(id,title,Author,Qty))


conn.commit()

conn.close()


#Yet to figure out how to bring out the menu for the USER

