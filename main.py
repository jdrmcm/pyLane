import json
import os


class Entry:
    def write_info(self, tags, usernames, passwords):
        with open(file, "w") as write_file:
            data = {
                "tags": tags,
                "usernames": usernames,
                "passwords": passwords
            }
            json.dump(data, write_file)

    def input_info(self, tag, user, pw):
        tags.append(tag)
        usernames.append(user)
        passwords.append(pw)
        self.write_info(tags, usernames, passwords)


file = "data.json"
tags = []
usernames = []
passwords = []

entry = Entry()

template = {
    "tags": [],
    "usernames": [],
    "passwords": []
}

if os.path.exists(file):
    pass
else:
    with open(file, "w") as f:
        json.dump(template, f)


def read_info():
    with open(file, "r") as read_file:
        data = json.load(read_file)
        tags = data.get("tags")
        usernames = data.get("usernames")
        passwords = data.get("passwords")


def debug_info():
    print(
        tags,
        usernames,
        passwords)


def user_input():
    tag = input("Input a tag: ")
    user = input("Input a username: ")
    pw = input("Input a password: ")
    entry.input_info(tag, user, pw)


debug_info()
user_input()
read_info()
debug_info()
