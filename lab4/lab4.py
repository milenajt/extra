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
            has_other_sym = all(map(lambda x: x.isalnum(), password))
            if all((has_upper, has_lower, has_digit, has_other_sym)):
                return password
            else:
                print('The password should contain A-Z, a-z, 0-9.')
        else:
            print('The length of the password should be more than 8 characters.')


def create_user():
    return {
        'Name': input('Name: ').title(),
        'Surname': input('Surname: ').title(),
        'Age': input('Age: '),
        'Address': input('Address: ').title(),
        'Username': check_username(),
        'Password': check_password(),
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
        print(f'There is no user named {username}.')


def authorization(username, password):
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
    match option:
        case '1':
            new_user = create_user()
            users_list.append(new_user)
            print("This user is created successfully!")
        case '2':
            show_list()
        case '3':
            username = input('Enter the username: ').lower()
            delete_user(username)
        case '4':
            username = input('Enter your username: ')
            password = input('Enter your password: ')
            authorization(username, password)
        case '5':
            print("Bye!")
            break
        case _:
            print("There is no such option, please enter again.")
    print()
