users_list = []


def greeting():
    print('''Choose one option:\n1. Create user\n2. Show list of users\n3. Delete user from List\n4. Authorization\n5. Exit''')


def check_username():
    while True:
        username = input('Username: ').lower()
        username_taken = False

        for user in users_list:
            if username == user['Username'].lower():
                print("This username is already taken.")
                username_taken = True
                break

        if not username_taken:
            return username


def check_password():
    while True:
        password = input('Password: ')
        if len(password) >= 8:
            has_upper = any(map(lambda x: x.isupper(), password))
            has_lower = any(map(lambda x: x.islower(), password))
            has_digit = any(map(lambda x: x.isdigit(), password))
            if all((has_upper, has_lower, has_digit)):
                return password
            else:
                print('The password should contain A-Z, a-z, 0-9.')
        else:
            print('The length of the password should be more than 8 characters.')


def create_user():
    name = input('Name: ')
    surname = input('Surname: ')
    age = int(input('Age: '))
    address = input('Address: ')
    username = check_username()
    password = check_password()
    return {
        'Name': name,
        'Surname': surname,
        'Age': age,
        'Address': address,
        'Username': username,
        'Password': password,
    }


def show_list():
    for user in users_list:
        for k, v in user.items():
            if k != 'Password':
                print(f'{k}: {v}', end='; ')
        print()


def delete_user(username):
    for user in users_list:
        if username == user['Username']:
            users_list.remove(user)
            print(f"User {username} is deleted successfully.")
            break
        else:
            print('There is no such username.')


def authorization():
    while True:
        username = input('Enter your username: ')
        password = input('Enter your password: ')
        for user in users_list:
            if username.lower() == user['Username'] and password == user['Password']:
                print("You are successfully logged in to the system.")
                print(f"Welcome back, {user['Name']}!")
                return True
        else:
            print('Your username or password is wrong.')


while True:
    greeting()
    option = input()
    if option == '1':
        new_user = create_user()
        users_list.append(new_user)
        print("This user is created successfully!")
    elif option == '2':
        show_list()
    elif option == '3':
        username = input('Enter the username: ').lower()
        delete_user(username)
    elif option == '4':
        authorization()
    elif option == '5':
        print("Bye!")
        break
    else:
        print("There is no such option, please enter again.")
    print()
