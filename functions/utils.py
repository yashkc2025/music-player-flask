import re

emailRegex = "[^@]+@[^@]+\.[^@]+"
passwordRegex = r"^(?=.*\d)(?=.*[a-zA-Z]).{4,}$"
file_extensions = ['mp3']


def validateRegister(email, password, name, confirm_password):
    if (re.match(emailRegex, email) == None):
        return "Invalid email"
    if (re.match(passwordRegex, password) == None):
        return "Password must be at least 8 characters long and contain at least one letter and one numbers"
    if (name == "" or name == None):
        return "Invalid name"
    if (password != confirm_password):
        return "Passwords do not match"
    return None

def validateLogin(email, password):
    if (re.match(emailRegex, email) == None):
        return "Invalid email"
    # if (re.match(passwordRegex, password) == None):
    #     return "Invalid password"
    return None

def allowed_extensions(file_name):
    return '.' in file_name and file_name.rsplit('.', 1)[1].lower() in file_extensions