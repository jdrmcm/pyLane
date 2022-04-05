import json


class Entry:
    def __init__(self):
        self.user = ""
        self.tag = ""
        self.password = ""
        self.file = ""

    def user_input(self, file):
        self.file = file
        tag_entry = input("Input a tag: ")
        username_entry = input("Input a username: ")
        password_entry = input("Input a password: ")
        self.user, self.tag, self.password = username_entry, tag_entry, password_entry
        self.write_info()

    def write_info(self):
        with open(self.file, "r+") as read_file:
            data = json.load(read_file)
            data["tags"].append(self.tag)
            data["usernames"].append(self.user)
            data["passwords"].append(self.password)

            read_file.seek(0)
            # convert back to json.
            json.dump(data, read_file, indent=0)
            print(data)


if __name__ == "__main__":
    Entry().user_input("data.json")
