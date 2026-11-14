
class PasswordManager:
    def __init__(self):
        self.__passwords = {}

    def add_password(self, website, password):
        self.__passwords[website] = password
        print("Password saved successfully")

    def get_password(self, website):
        if website in self.__passwords:
            return self.__passwords[website]

        return "Website not found"

    def show_websites(self):
        for website in self.__passwords:
            print(website)


manager = PasswordManager()

manager.add_password("Google", "google123")
manager.add_password("GitHub", "github456")

manager.show_websites()

print(manager.get_password("Google"))
