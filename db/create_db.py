import sqlite3 as sql

# create songs table
con = sql.connect('db/database.db')
cur = con.cursor()
cur.execute("DROP TABLE IF EXISTS songs")

# Create songs table in databases/db_songs database
songsSQL = '''CREATE TABLE "songs" (
	"UID"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"NAME"	TEXT,
	"ALBUMID"	TEXT,
	"ALBUMNAME"	TEXT,
	"ARTIST" TEXT,
    "UPVOTES" INTEGER NOT NULL DEFAULT 0,
    "DOWNVOTES" INTEGER NOT NULL DEFAULT 0,
    "DURATION" INTEGER NOT NULL DEFAULT 0,
	"SONGFILE"	TEXT,
	"LYRICS"	TEXT,
	"DATE CREATED" NOT NULL DEFAULT CURRENT_TIMESTAMP,
	"USER" INTEGER
)'''
cur.execute(songsSQL)
con.commit()

# Create users table
cur.execute("DROP TABLE IF EXISTS users")

user_sql = '''CREATE TABLE "users" (
	"UID"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"EMAIL"	TEXT,
	"PASSWORD"	TEXT,
	"TYPE"	INTEGER,
    "NAME"  TEXT,
	"BLOCKED"	INTEGER NOT NULL DEFAULT 0,
	"DATE CREATED" NOT NULL DEFAULT CURRENT_TIMESTAMP
)'''

cur.execute(user_sql)
# create admin user
cur.execute("INSERT INTO users (EMAIL, PASSWORD, TYPE, NAME) VALUES (?, ?, ?, ?)", ("admin@admin.com", "admin", 2, "admin"))
con.commit()

# Create albums table
cur.execute("DROP TABLE IF EXISTS albums")
album_sql = '''CREATE TABLE "albums" (
	"UID"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"ALBUMNAME"	TEXT,
	"ARTIST"	TEXT,
	"GENRE"	TEXT,
	"DATE CREATED" NOT NULL DEFAULT CURRENT_TIMESTAMP,
	"USER" INTEGER
)'''
cur.execute(album_sql)
con.commit()

# Create playlists table
cur.execute("DROP TABLE IF EXISTS playlists")
playlist_sql = '''CREATE TABLE "playlists" (
	"UID"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"PLAYLISTNAME"	TEXT,
	"DATE CREATED" NOT NULL DEFAULT CURRENT_TIMESTAMP,
	"SONGS" TEXT,
	"USER" INTEGER
)'''
cur.execute(playlist_sql)
con.commit()
con.close()