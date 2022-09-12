import sys
from dbhelper import Dbhelper

class Flipkart:
    def __init__(self):
        # connect to the database\
        self.db = Dbhelper()
        self.menu()

    def menu(self):

        user_input = input("""
        1. Enter 1 to register
        2. Enter 2 to login
        3. Anything else to leave
        """)

        if user_input == '1':
            self.register()
        elif user_input == '2':
            self.login()
        else:
            sys.exit(1000)


    def login_menu(self):
        input("""
        1. Enter 1 to see profile
        2. Enter 2 to edit profile
        3. Enter 3 to delete profile
        4. Enter 4 to Logout
        """)

    def register(self):
        name = input("Enter the name")
        email = input("Enter the email id")
        password = input("Enter the password")

        response = self.db.register(name, email, password)

        if response:
            print("Registration successful")

        else:
            print("Registration failed")

        self.menu()


    def login(self):
        email= input("Enter Email")
        password = input("Enter Password")

        data = self.db.search(email, password)         # Search() is present in dbhelper.py file. data accepts a list of tupples (sent by search()) with the values inside - ID, Name, Email id and password if the entered mail id and password is correct.

        if not data:                                    # data will be empty is the search() is not able to find the item we were looking for. Hence if data == 0 means login failed
            print("Incorrect email id or password")
            self.login()

        else:
            print("Hello", data[0][1])                  # if data is not empty then that means user logged in by entering correct email id and pwd. In that case we display "Hello NameofUser".
            self.login_menu()

obj = Flipkart()


