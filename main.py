import json
import os


class Entry:
    def __init__(self):
        self.user = ""
        self.tag = ""
        self.password = ""
        self.dict = {
                "tags": self.tag,
                "usernames": self.user,
                "passwords": self.password
            }


    def user_input(self):
        tag_entry = input("Input a tag: ")
        username_entry = input("Input a username: ")
        password_entry = input("Input a password: ")
        self.user, self.tag, self.password = username_entry, tag_entry, password_entry


        # tags.append(tag_entry)
        # usernames.append(username_entry)
        # passwords.append(password_entry)
        self.write_info()


    def write_info(self):
        with open(file, "r+") as read_file:
            data = json.load(read_file)
            print(data)
            new_entry = {
                "tags": self.tag ,
                "usernames": self.user,
                "passwords": self.password
            }

            data.append(new_entry)
            read_file.seek(0)
            # convert back to json.
            json.dump(data, read_file, indent=0)
            print(data)




file = "data.json"
tags = []
usernames = []
passwords = []



def read_info():
    with open(file, "r") as read_file:
        data = json.load(read_file)
        print(data)




def debug_info():
    print(
        tags,
        usernames,
        passwords)


if __name__ == "__main__":

    Entry().user_input()

debug_info()

read_info()
debug_info()
