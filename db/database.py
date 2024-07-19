import sqlite3 as sql


def fetchDB(query, *args):
    print(query, args)
    with sql.connect("db/database.db") as con:
        try:
            cur = con.cursor()
            cur.execute(query, *args)
            rows = cur.fetchall()
            cur.close()
        except Exception as e:
            print("Error " + query + " " + str(args))
            print(e)
            con.rollback()
            rows = None
            raise Exception(e)
    return rows


def fetchUID(email):
    uid = fetchDB("SELECT * FROM users WHERE EMAIL  = ? ",  (email,))
    return uid

def insertDB(query, *args):
    print(query, args)
    with sql.connect("db/database.db") as con:
        try:
            cur = con.cursor()
            cur.execute(query, *args)
            con.commit()
            cur.close()
        except Exception as e:
            print("Error " + query + " " + str(args))
            con.rollback()
            rows = None
            raise Exception(e)
    return cur.lastrowid

def createUser(email, password, name, userType):
    insertDB("INSERT INTO users (EMAIL, PASSWORD, TYPE, NAME) VALUES (?, ?, ?, ?)", (email, password, userType, name))    
    uid =  fetchDB("SELECT * FROM users WHERE EMAIL = ?", (email,))
    return uid    