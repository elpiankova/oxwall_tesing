class User:
    def __init__(self, username="", password="", real_name="", email="", gender=None, birthday=None, is_admin=False):
        self.username = username
        self.password = password
        self.real_name = real_name
        self.email = email
        self.gender = gender
        self.birthday = birthday
        self.is_admin = is_admin

    def __str__(self):
        return f"{self.__class__} object: username={self.username}, real_name={self.real_name}"

    def __repr__(self):
        return f"{self.__class__} object: username={self.username}, password={self.password}, real_name={self.real_name}"

    def __eq__(self, other):
        if self.email != "" or other.email != "":
            return self.username == other.username and self.real_name == other.real_name and self.email == self.email
        return self.username == other.username and self.real_name == other.real_name

