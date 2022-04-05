import random
import string
import json


template = {
    "tags": [

    ],
    "usernames": [

    ],
    "passwords": [

    ]
}


def generate_password():  # add something to let user choose length and character types
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(characters) for i in range(15))
    print(f"Generated password: {password}")
    return password


def create_template_file(file):
    with open(file, "w") as write_file:
        json.dump(template, write_file, indent=0)


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
        print("Would you like to generate a random password? Type Y or N:")
        user_input = input("> ")
        if user_input.lower() == "y":
            password_entry = generate_password()
        else:
            password_entry = input("Input a password: ")
        self.user, self.tag, self.password = username_entry, tag_entry, password_entry
        self.write_info()

    def user_search(self, file, remove):
        self.file = file
        tag_search = input("Input a tag: ")
        with open(self.file, "r") as read_file:
            data = json.load(read_file)
        for entry in range(len(data["tags"])):
            if data["tags"][entry] == tag_search:
                print("TAG: " + data["tags"][entry])
                print("USERNAME: " + data["usernames"][entry])
                print("PASSWORD: " + data["passwords"][entry])
                if remove:
                    self.remove_entry(file, entry)
                else:
                    print("Press enter to return to the main menu.")
                    input()
                    menu()
            elif entry == len(data["tags"]) - 1:
                print("NOT FOUND")
                print("Press enter to return to the main menu.")
                input()
                menu()

    def remove_entry(self, file, entry):
        self.file = file
        print("Are you sure you want to remove this? Type Y or N:")
        user_input = input("> ")
        if user_input.lower() == "y":
            with open(self.file, "r") as read_file:
                data = json.load(read_file)
                del data["tags"][entry]
                del data["usernames"][entry]
                del data["passwords"][entry]
                with open(self.file, "w") as write_file:
                    write_file.seek(0)
                    json.dump(data, write_file, indent=0)
                print("Entry deleted.")
                menu()
        else:
            menu()

    def write_info(self):
        with open(self.file, "r+") as read_file:
            data = json.load(read_file)
            data["tags"].append(self.tag)
            data["usernames"].append(self.user)
            data["passwords"].append(self.password)

            read_file.seek(0)
            # convert back to json.
            json.dump(data, read_file, indent=0)
            print("Entry added.")
            print("Press enter to return to the main menu.")
            input()
            menu()


def menu():
    print(
        f"Please select a menu option by its number:"
        f"\n1) New entry"
        f"\n2) Search by tag"
        f"\n3) Remove entry"
        f"\n0) Quit")
    user_input = input("> ")
    try:
        if int(user_input) == 1:
            Entry().user_input("data.json")
        elif int(user_input) == 2:
            Entry().user_search("data.json", False)
        elif int(user_input) == 3:
            Entry().user_search("data.json", True)
        elif int(user_input) == 0:
            quit()
        else:
            print("Invalid selection")
            menu()
    except Exception as e:
        print(f"[!] ERROR: {e}")
        menu()


if __name__ == "__main__":
    try:
        with open("data.json", "r"):
            pass
    except Exception as e:
        print(f"[!] ERROR: {e}")
        print(f"JSON DATA NOT FOUND")
        print(f"CREATING DATA.JSON...")
        create_template_file("data.json")
    menu()
