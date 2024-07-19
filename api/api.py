from functions.manage import (
    add_album,
    add_song,
    add_playlist,
    edit_song,
    edit_album,
    edit_playlist,
    delete_song,
    delete_album,
    delete_playlist,
)

from flask import (
    Blueprint,
    render_template,
    make_response,
    request,
    redirect,
    flash,
    session,
    jsonify,
    Response,
)
import db.database as db
from flask_restful import Resource
headers = {"Content-Type": "text/html"}

class AddAlbum(Resource):
    def post(self):
        try:
            data = request.form
            albumname = data["albumName"]
            artist = data["artistName"]
            genre = data["genre"]

            add_album(albumname, artist, genre)
            return redirect("/manage/albums")
        except Exception as e:
            return Response(str(e), status=500)

    def get(self):

        return make_response(render_template("manage/add_album.html"), 200, headers)


class AddSong(Resource):
    def post(self):
        try:
            data = request.form
            songname = data["songName"]
            albumID = data["albumID"]
            artistName = data["artistName"]
            lyrics = data["lyrics"]
            file = request.files["songFile"]

            add_song(songname, albumID, artistName, lyrics, file)
            flash("Song added successfully")
            return redirect("/manage/songs")
        except Exception as e:
            return Response(str(e), status=500)

    def get(self):
        albums = db.fetchDB("SELECT ALBUMNAME, UID FROM albums")
        return make_response(render_template("manage/add_song.html", albumsList=albums), 200, headers)  


class AddPlaylist(Resource):
    def post(self):
        try:
            data = request.form
            playlistName = data["playlistName"]
            songs = str(data.getlist("songs"))

            add_playlist(playlistName, songs)
            flash("Playlist added successfully")
            return redirect("/playlists")
        except Exception as e:
            return Response(str(e), status=500)

    def get(self):
        songs = db.fetchDB("SELECT * FROM songs")

        return make_response(render_template("hero/add_playlist.html", songs=songs), 200, headers)


class EditSong(Resource):
    def post(self, songID):
        try:
            data = request.form
            songName = data["songName"]
            albumID = data["albumID"]
            artistName = data["artistName"]
            lyrics = data["lyrics"]

            edit_song(songID, songName, albumID, artistName, lyrics)
            flash("Song edited successfully")
            return redirect("/manage/songs")
        except Exception as e:
            return Response(str(e), status=500)

    def get(self, songID):
        albums = db.fetchDB("SELECT ALBUMNAME, UID FROM albums")
        data = db.fetchDB(
            "SELECT UID, NAME, ALBUMNAME, ARTIST, LYRICS FROM songs WHERE UID = ?",
            (songID,),
        )
        return make_response(render_template("manage/edit_song.html", datas=data, albumsList=albums), 200, headers)


class EditAlbum(Resource):
    def post(self, albumID):
        try:
            data = request.form
            albumName = data["albumName"]
            artistName = data["artistName"]
            genre = data["genre"]

            edit_album(albumID, albumName, artistName, genre)
            flash("Album edited successfully")
            return redirect("/manage/albums")
        except Exception as e:
            return Response(str(e), status=500)

    def get(self, albumID):
        data = db.fetchDB("SELECT * FROM albums WHERE UID = ?", (albumID,))
        return make_response(render_template("manage/edit_album.html", datas=data), 200, headers)


class EditPlaylist(Resource):
    def post(self, playID):
        try:
            data = request.form
            playlistName = data["playlistName"]
            songs = str(data.getlist("songs"))

            edit_playlist(playID, playlistName, songs)
            flash("Playlist edited successfully")
            return redirect("/playlists")
        except Exception as e:
            return Response(str(e), status=500)

    def get(self, playID):
        data = db.fetchDB("SELECT UID,PLAYLISTNAME, SONGS FROM playlists WHERE UID = ?", (playID,))
        songs = db.fetchDB("SELECT * FROM songs")
        return make_response(render_template("hero/edit_playlist.html", data=data, songs=songs), 200, headers)


class DeleteSong(Resource):
    def get(self, songID):
        try:
            delete_song(songID)
            flash("Song deleted successfully")
            return redirect("/manage/songs")
        except Exception as e:
            return Response(str(e), status=500)


class DeleteAlbum(Resource):
    def get(self, albumID):
        try:
            delete_album(albumID)
            flash("Album deleted successfully")
            return redirect("/manage/albums")
        except Exception as e:
            return Response(str(e), status=500)


class DeletePlaylist(Resource):
    def get(self, playID):
        try:
            delete_playlist(playID)
            flash("Playlist deleted successfully")
            return redirect("/playlists")
        except Exception as e:
            return Response(str(e), status=500)
