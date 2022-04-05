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
            # This new_entry should only be used if you have a sorting tag to insert each dict underneath
            # Such an entry might take the form of name or something so your file format would look like
            # name:
            #   tags: tag
            #   username: username
            #   password: password
            # Then repeat...
            #
            # new_entry = {
            #     "tags": self.tag,
            #     "usernames": self.user,
            #     "passwords": self.password
            # }
            # // The error was happening here because this is appending a dictionary where the "Tags" were
            # // needs instead to append each of the inputs to proper spot.. so instead of:
            # data.append(new_entry)
            #  We should have this:
            data["tags"].append(self.tag)
            data["usernames"].append(self.user)
            data["passwords"].append(self.password)

            read_file.seek(0)
            # convert back to json.
            json.dump(data, read_file, indent=0)
            print(data)


if __name__ == "__main__":
    Entry().user_input("data.json")

