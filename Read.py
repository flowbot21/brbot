import string

def getUser(line):
    separate = line.split(":", 2)
    user = separate[1].split("!", 1)[0]
    return user

def getMsg(line):
    separate = line.split(":", 2)
    if len(separate) < 3:
        message = "null"
    else:
        message = separate[2]
    message = message.lower()
    return message

def getUserLevel(line):
    separate = line.split(":", 2)
    separate = separate[0].split(";", 11)
    separate = separate[0].split("/")
    separate = separate[0].split("=")
    if len(separate) < 2:
        user_level = "null"
    else:
        user_level = separate[1]
    return user_level