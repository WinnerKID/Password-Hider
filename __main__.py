import getpass

def hide_password(password):
    return '•' * len(password)

def reveal_password(hidden_password):
    return hidden_password.replace('•', '')

def enter_pass():
    print('Password Hider\n')
    print('This script is a place to store passwords and have them be replaced by dots.\n'
          'With this method, it allows users to share the screen, and whenever they need access to their password, it isn\'t revealed to anyone')

    print()
    user_title = input('Enter a title: ')

    while True:
        user_pass = getpass.getpass('Enter a password: ')
        check_pass = getpass.getpass('Check password: ')

        if user_pass == check_pass:
            print('Both passwords match!\n')
            with open('storage.txt', 'a') as f:
                hidden_password = hide_password(user_pass)
                print('# ' + user_title, file=f)
                print(hidden_password, file=f)
            break
        else:
            print('Passwords did not match, please try again')

def read_pass(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        for i in range(0, len(lines), 2):
            title = lines[i].strip('# ').strip()
            hidden_password = lines[i + 1].strip()
            password = reveal_password(hidden_password)
            print(f'Title: {title}')
            print(f'Password: {password}\n')

if __name__ == "__main__":
    while True:
        choice = input('Choose an option:\n1. Enter a new password\n2. Read passwords from file\n3. Exit\nEnter choice: ')
        if choice == '1':
            enter_pass()
        elif choice == '2':
            filename = 'storage.txt'
            read_pass(filename)
        elif choice == '3':
            break
        else:
            print('Invalid choice. Please select a valid option (1, 2, or 3).')
