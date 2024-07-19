from flask import render_template, request, flash, session, redirect
from functions.utils import validateLogin, validateRegister
import db.database as db
import functions.utils as utils

#  Auth Functions


def login():
    if request.method == "POST":
        email = request.form["userEmail"]
        password = request.form["userPassword"]

        error = utils.validateLogin(email, password)
        if error != None:
            flash(error)
            return render_template("auth/login.html")

        user = db.fetchUID(email)
        print(user)
        if user == None or len(user) == 0:
            flash("User does not exist")
            return render_template("auth/login.html")

        user = user[0]

        if user[5] == 1:
            flash("User is blocked")
            return render_template("auth/login.html")

        if user[2] != password:
            flash("Incorrect password")
            return render_template("auth/login.html")

        session["user"] = user[0]
        session["type"] = user[3]

        flash("Logged in successfully")

    return render_template("auth/login.html")


def register():
    if request.method == "POST":
        email = request.form["userEmail"]
        password = request.form["userPassword"]
        confirm_password = request.form["userConfirmPassword"]
        name = request.form["userName"]

        error = utils.validateRegister(email, password, name, confirm_password)
        if error != None:
            flash(error)
            return render_template("auth/register.html")

        user_id = db.createUser(email, password, name, 0)
        print(user_id)

        session["user"] = user_id[0][0]
        session["type"] = user_id[0][3]

        flash( " registered successfully")

        return redirect("/")

    print(request.method)
    return render_template("auth/register.html")


def forgot_password():
    if request.method == "POST":
        email = request.form["userEmail"]

        user

    return render_template("auth/forgot.html")


def delete_user():
    if request.method == "POST":
        email = request.form["userEmail"]

        db.insertDB("DELETE FROM users WHERE EMAIL = ?", email)

        flash("User deleted successfully")
        return redirect("/")


def logout():
    session.pop("user", None)
    return redirect("/")


def account():
    pass


# Utility Functions


def switch_to_creator():
    if request.method == "POST":
        db.insertDB("UPDATE users SET TYPE = 1 WHERE UID = ?", (session["user"],))
        session["type"] = 1
        flash("Swithed to creator account")
        return redirect("/")
    return render_template("manage/switch.html")


def edit_account():
    if request.method == "POST":
        email = request.form["userEmail"]
        old_password = request.form["userPassword"]
        new_password = request.form["userNewPassword"]
        name = request.form["userName"]

        error = utils.validateRegister(email, new_password, name, new_password)
        if error != None:
            flash(error)
            return render_template("auth/register.html")

        # cheeck if old password is correct
        pss = db.fetchDB("SELECT PASSWORD FROM users WHERE UID = ?", (session["user"],))
        if pss != old_password:
            flash("Incorrect password")
            redirect("/edit-account")

        db.insertDB(
            "UPDATE users SET EMAIL = ?, PASSWORD = ?, NAME = ? WHERE UID = ?",
            (email, new_password, name, session["user"]),
        )

        flash("Account updated successfully")
        return redirect("/")

    data = db.fetchDB("SELECT * FROM users WHERE UID = ?", (session["user"],))
    return render_template("manage/edit-account.html", data=data[0])


def getUserID():
    if "user" in session:
        return session["user"]
    else:
        return None


def block_user(userID):
    db.insertDB("UPDATE users SET BLOCKED = 1 WHERE UID = ?", (userID,))
    flash("User blocked successfully")
    return redirect("/admin/users")


def unblock_user(userID):
    db.insertDB("UPDATE users SET BLOCKED = 0 WHERE UID = ?", (userID,))
    flash("User unblocked successfully")
    return redirect("/admin/users")


def delete_user(userID):
    db.insertDB("DELETE FROM users WHERE UID = ?", (userID,))
    flash("User deleted successfully")
    return redirect("/admin/users")


def admin_login():
    if request.method == "POST":
        email = request.form["userEmail"]
        password = request.form["userPassword"]

        error = utils.validateLogin(email, password)

        if error != None:
            flash(error)
            return render_template("auth/admin-login.html")

        user = db.fetchUID(email)

        if user == None or len(user) == 0:
            flash("User does not exist")
            return render_template("auth/admin-login.html")

        user = user[0]

        if user[2] != password:
            flash("Incorrect password")
            return render_template("auth/admin-login.html")

        if user[3] != 2:
            flash("User is not an admin")
            return render_template("auth/admin-login.html")

        session["user"] = user[0]
        session["type"] = user[3]

        flash("Logged in successfully")

        return redirect("/admin")

    return render_template("auth/admin_login.html")
