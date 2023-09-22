
def enter_pass():
    print('Password Hider\n')
    print('This script is a place to store passwords and have them be replaced by dots.\n'
          'With this method it allows users to sharescreen and whenever they need access to their password it isnt revealed to anyone')

    print()
    user_title = input('Enter a title: ')

    while True:

        user_pass = input('Enter a password: ')
        check_pass = input('Check password: ')
        if user_pass == check_pass:
            print('Both passwords match!')
            with open('storage.txt', 'a') as f: # the a stands for append in other words the existing contents of the file won't be overwritten
                print('# ' + user_title, file=f) # the hashtag is an indication that what comes after it is a title
                print(user_pass, file=f)
            break
        elif user_pass != check_pass:
            print('Passwords did not match, please try again')

if __name__ == "__main__":
    enter_pass()

