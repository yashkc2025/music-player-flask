from flask import Flask, session, g, redirect, url_for, request, render_template, flash
from functions.appConfig import appConfig
import functions.user as user
import functions.dash as dash
import functions.manage as manage
import api.api as apiRoutes
from flask_restful import Api, Resource

def boot_app():
    app = Flask(__name__)
    app.config.from_object(appConfig)
    api = Api(app)
    app.app_context().push()
    return app, api


app, api = boot_app()


app.add_url_rule("/", view_func=dash.index, methods=["GET", "POST"])

# Auth Routes

app.add_url_rule("/auth/login", view_func=user.login, methods=["GET", "POST"])
app.add_url_rule("/auth/register", view_func=user.register, methods=["GET", "POST"])
app.add_url_rule(
    "/auth/forgot", view_func=user.forgot_password, methods=["GET", "POST"]
)
app.add_url_rule("/auth/logout", view_func=user.logout, methods=["GET", "POST"])
app.add_url_rule("/auth/delete", view_func=user.delete_user, methods=["GET", "POST"])
app.add_url_rule(
    "/switch-to-creator", view_func=user.switch_to_creator, methods=["GET", "POST"]
)
app.add_url_rule("/edit-account", view_func=user.edit_account, methods=["GET", "POST"])

app.add_url_rule("/admin", view_func=manage.admin, methods=["GET", "POST"])
app.add_url_rule("/admin/users", view_func=manage.admin_users, methods=["GET", "POST"])
app.add_url_rule(
    "/admin/albums", view_func=manage.admin_albums, methods=["GET", "POST"]
)
app.add_url_rule(
    "/auth/admin-login", view_func=user.admin_login, methods=["GET", "POST"]
)

app.add_url_rule(
    "/admin/block-user/<string:userID>",
    view_func=user.block_user,
    methods=["GET", "POST"],
)
app.add_url_rule(
    "/admin/unblock-user/<string:userID>",
    view_func=user.unblock_user,
    methods=["GET", "POST"],
)
app.add_url_rule(
    "/admin/delete-user/<string:userID>",
    view_func=user.delete_user,
    methods=["GET", "POST"],
)
# Dashboard Routes

app.add_url_rule(
    "/song/<string:songID>", view_func=dash.song_info, methods=["GET", "POST"]
)
app.add_url_rule(
    "/playlist/<string:playID>", view_func=dash.playlist_info, methods=["GET", "POST"]
)
app.add_url_rule(
    "/album/<string:albumID>", view_func=dash.album_info, methods=["GET", "POST"]
)
app.add_url_rule(
    "/api/downvote/<string:songID>", view_func=dash.downvote, methods=["GET", "POST"]
)
app.add_url_rule(
    "/api/upvote/<string:songID>", view_func=dash.upvote, methods=["GET", "POST"]
)
app.add_url_rule("/albums", view_func=dash.list_albums, methods=["GET", "POST"])
app.add_url_rule("/playlists", view_func=dash.list_playlists, methods=["GET", "POST"])
app.add_url_rule("/search", view_func=dash.search, methods=["GET", "POST"])

# Creator Routes

app.add_url_rule("/manage/", view_func=manage.index_manage, methods=["GET", "POST"])
app.add_url_rule("/manage/songs", view_func=manage.list_songs_edit, methods=["GET", "POST"])
app.add_url_rule("/manage/albums", view_func=manage.list_albums_edit, methods=["GET", "POST"])

api.add_resource(apiRoutes.AddAlbum, "/manage/add-album")
api.add_resource(apiRoutes.EditAlbum, "/manage/edit-album/<string:albumID>")
api.add_resource(apiRoutes.EditPlaylist, "/dash/edit-playlist/<string:playID>")
api.add_resource(apiRoutes.DeleteSong, "/manage/delete-song/<string:songID>")
api.add_resource(apiRoutes.DeleteAlbum, "/manage/delete-album/<string:albumID>")
api.add_resource(apiRoutes.DeletePlaylist, "/dash/delete-playlist/<string:playID>")
api.add_resource(apiRoutes.AddSong, "/manage/add-song")
api.add_resource(apiRoutes.AddPlaylist, "/manage/add-playlist")
api.add_resource(apiRoutes.EditSong, "/manage/edit-song/<string:songID>")

app.add_url_rule("/get_song_name/<string:fileID>", view_func=dash.get_song_name, methods=["GET", "POST"])

def main():
    app.run(debug=True)


@app.before_request
def before_request():
    if "user" not in session and request.endpoint not in (
        "login",
        "register",
        "forgot",
        "admin_login",
        "static",
    ):
        return redirect(url_for("login"))

    if request.endpoint == "static":
        return

    print(request.full_path)
    if request.full_path.startswith("/admi"):
        if session["type"] != 2:
            flash("You are not authorized to access this page")
            return redirect("/")

    if request.full_path.startswith("/manage/") and request.full_path != "/manage/?":
        if session["type"] == 0:
            return redirect("/switch-to-creator")

    # print("in")
    # if request.script_root == "/static":
    #     return
    # if 'user' in session:
    #     print("set")
    # else:
    #     if (request.endpoint == None):
    #         return "404"
    #     if (not (request.full_path.startswith("/auth"))):
    #         print(request.full_path)
    #         return redirect("/auth/login")


if __name__ == "__main__":
    app.run(host="0.0.0.0")
