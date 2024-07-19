import db.database as db
from flask import request, render_template, session, redirect, url_for, flash
from functions.user import getUserID
from functions.utils import allowed_extensions
import uuid
from mutagen.mp3 import MP3

music_folder = "static/music/"

def index_manage():
    return render_template("manage/index.html")

# Add Functions

def add_album(albumName, artistName, genre):
    userId = getUserID()

    db.insertDB(
        "INSERT INTO albums (ALBUMNAME, ARTIST, GENRE, USER) VALUES (?, ?, ?, ?)",
        (albumName, artistName, genre, userId),
    )



def add_song(songName, albumID, artistName, lyrics, file):

    uid = getUserID()
    albumName = db.fetchDB("SELECT ALBUMNAME FROM albums WHERE UID = ?", (albumID,))[0][0]

    if file and allowed_extensions(file.filename):
        filename = uuid.uuid4().hex + "." + file.filename.rsplit(".", 1)[1].lower()
        file.save(music_folder + filename)
        duration = MP3(music_folder + filename).info.length
        db.insertDB(
            "INSERT INTO songs (NAME, ALBUMNAME, ALBUMID, ARTIST, LYRICS, SONGFILE, USER, DURATION) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
            (songName, albumName, albumID, artistName, lyrics, filename, uid, duration),
        )


def add_playlist(playlistName, songs):
    uid = getUserID()

    db.insertDB(
        "INSERT INTO playlists (PLAYLISTNAME, SONGS, USER) VALUES (?, ?, ?)",
        (playlistName, songs, uid),
    )

    flash("Playlist added successfully")
    return redirect("/playlists")

# Edit Functions

def edit_song(songID,songName, albumID, artistName, lyrics ):
    albumName = db.fetchDB("SELECT ALBUMNAME FROM albums WHERE UID = ?", (albumID,))[0][0]

    db.insertDB(
        "UPDATE songs SET NAME = ?,ALBUMID = ?,  ALBUMNAME = ?, ARTIST = ?, LYRICS = ? WHERE UID = ?",
        (songName,albumID, albumName, artistName, lyrics, songID),
    )


def edit_album(albumID, albumName, artistName, genre):
    db.insertDB(
        "UPDATE albums SET ALBUMNAME = ?, ARTIST = ?, GENRE = ? WHERE UID = ?",
        (albumName, artistName, genre, albumID),
    )

    flash("Album edited successfully")
    return redirect("/manage/albums")

def edit_playlist(playID, playlistName, songs):

    db.insertDB(
        "UPDATE playlists SET PLAYLISTNAME = ?, SONGS = ? WHERE UID = ?",
        (playlistName, songs, playID),
    )
# Delete Functions

def delete_song(songID):
    db.insertDB("DELETE FROM songs WHERE UID = ?", (songID,))
    
def delete_album(albumID):
    db.insertDB("DELETE FROM albums WHERE UID = ?", (albumID,))

def delete_playlist(playID):
    db.insertDB("DELETE FROM playlists WHERE UID = ?", (playID,))

    
def list_albums_edit():
    uid = str(getUserID())
    data = db.fetchDB("SELECT * FROM albums where USER = " + uid )
    return render_template("manage/list_albums.html", datas=data)

def list_songs_edit():
    uid = str(getUserID())
    data = db.fetchDB("SELECT * FROM songs where USER = " + uid )
    return render_template("manage/list_songs.html", datas=data)

def admin():
    datas = db.fetchDB("Select * from songs")
    user_count = db.fetchDB("SELECT COUNT(*) FROM users where TYPE = 0")[0][0]
    song_count = db.fetchDB("SELECT COUNT(*) FROM songs")[0][0]
    album_count = db.fetchDB("SELECT COUNT(*) FROM albums")[0][0]
    playlist_count = db.fetchDB("SELECT COUNT(*) FROM playlists")[0][0]
    creator_count = db.fetchDB("SELECT COUNT(*) FROM users WHERE TYPE = 1")[0][0]
    count = {
        "users": user_count,
        "songs": song_count,
        "albums": album_count,
        "playlists": playlist_count,
        "creators": creator_count,
    }
    return render_template("admin/index.html", datas=datas, count=count)

def admin_users():
    # datas = db.fetchDB("SELECT * FROM users where TYPE = 0 or TYPE = 1")
    datas = db.fetchDB("SELECT UID, NAME, EMAIL, BLOCKED FROM users ")
    return render_template("admin/users.html", datas=datas)

def admin_albums():
    data = db.fetchDB("SELECT * FROM albums")
    return render_template("manage/list_albums.html", datas=data)