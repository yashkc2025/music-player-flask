CREATE TABLE sqlite_sequence(name,seq);
CREATE TABLE IF NOT EXISTS "songs" (
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
);
CREATE TABLE IF NOT EXISTS "users" (
	"UID"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"EMAIL"	TEXT,
	"PASSWORD"	TEXT,
	"TYPE"	INTEGER,
    "NAME"  TEXT,
	"BLOCKED"	INTEGER NOT NULL DEFAULT 0,
	"DATE CREATED" NOT NULL DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE IF NOT EXISTS "albums" (
	"UID"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"ALBUMNAME"	TEXT,
	"ARTIST"	TEXT,
	"GENRE"	TEXT,
	"DATE CREATED" NOT NULL DEFAULT CURRENT_TIMESTAMP,
	"USER" INTEGER
);
CREATE TABLE IF NOT EXISTS "playlists" (
	"UID"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"PLAYLISTNAME"	TEXT,
	"DATE CREATED" NOT NULL DEFAULT CURRENT_TIMESTAMP,
	"SONGS" TEXT,
	"USER" INTEGER
);
