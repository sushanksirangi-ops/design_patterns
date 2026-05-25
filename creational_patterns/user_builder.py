class User:

    def __init__(self, builder):
        self.name = builder.name
        self.email = builder.email
        self.age = builder.age
        self.phone = builder.phone
        self.address = builder.address

    def display(self):
        print("\nUser Details")
        print("Name:", self.name)
        print("Email:", self.email)
        print("Age:", self.age)
        print("Phone:", self.phone)
        print("Address:", self.address)


class UserBuilder:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.age = None
        self.phone = None
        self.address = None

    def set_age(self, age):
        self.age = age
        return self

    def set_phone(self, phone):
        self.phone = phone
        return self

    def set_address(self, address):
        self.address = address
        return self

    def build(self):
        return User(self)