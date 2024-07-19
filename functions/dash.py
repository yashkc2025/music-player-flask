import db.database as db
from flask import render_template, request
import ast
import json


def song_info(songID):
    song = db.fetchDB(
        "Select NAME, ARTIST, ALBUMNAME, LYRICS from songs where UID = ?", (songID,)
    )
    return render_template("hero/view_song.html", data=song)


def playlist_info(playID):
    playlist = db.fetchDB("Select * from playlists where UID =  ?", (playID,))
    songsUID = ast.literal_eval(playlist[0][3])
    # every element inside songsUID is a song UID but in string format. We need to convert it to int
    songsUID = tuple(map(int, songsUID))
    if(len(songsUID) == 0):
        songs = []
    else:
        songs = db.fetchDB("SELECT * FROM songs WHERE UID IN " + str(songsUID)[:-2] + str(songsUID)[-1:])
    return render_template("hero/view_playlist.html", data=playlist, datas=songs)


def album_info(albumID):
    album = db.fetchDB("Select * from albums where UID =  ?", (albumID,))
    songs = db.fetchDB("Select * from songs where ALBUMID =  ?", (albumID,))
    return render_template("hero/view_album.html", albumData=album, datas=songs)


def downvote(songID):
    if request.method == "POST":
        db.insertDB(
            "UPDATE songs SET DOWNVOTES = DOWNVOTES + 1 WHERE UID =  ?", (int(songID),)
        )
        return json.dumps({"status": "OK"})


def upvote(songID):
    if request.method == "POST":
        db.insertDB(
            "UPDATE songs SET UPVOTES = UPVOTES + 1 WHERE UID =  ?", (int(songID),)
        )
        return json.dumps({"status": "OK"})


def list_albums():
    albums = db.fetchDB("Select * from albums")
    return render_template("hero/albums.html", datas=albums)


def list_playlists():
    playlists = db.fetchDB("Select * from playlists")
    return render_template("hero/playlists.html", datas=playlists)


def index():
    data = db.fetchDB("SELECT * FROM songs ORDER BY UPVOTES DESC")
    return render_template("hero/index.html", datas=data)


def search():
    if request.method == "POST":
        search = request.form["search"]
        songs = db.fetchDB(
            "select * from songs where NAME like ?", ("%" + search + "%",)
        )
        albums = db.fetchDB(
            "select * from albums where ALBUMNAME like ?", ("%" + search + "%",)
        )

        return render_template("hero/search.html", datas=songs, album_data=albums)
    return render_template("hero/search.html")

def get_song_name(fileID):
    if request.method == "POST":
        song = db.fetchDB("select NAME from songs where SONGFILE = ?", (fileID,))
        return json.dumps({"status": "OK", "name": song[0][0]})