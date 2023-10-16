



"""enteredUsername = input('Please enter your login ')
enteredPassword = input('Please enter your password ')

def check(username, password, enteredUsername, enteredPassword):

    if username == enteredUsername and password == enteredPassword:
        return print('Your are logged in!')

    else: return print('Your credentials are wrong')

check(username, password, enteredUsername, enteredPassword)"""

class Login:
    def login(self):
        username = input('Please enter your username ')
        password = input('Please enter your password ')

        print('Your account has been created\nYour login is '+username+'\nYour password is '+password)
        print('Login now')

        enteredUsername = input('Please enter your login ')
        enteredPassword = input('Please enter your password ')

        if username == enteredUsername and password == enteredPassword:
           print('Your are logged in!')

        else:
            print('Your credentials are wrong')




from Encapsulation import Computer
obj = Computer()
