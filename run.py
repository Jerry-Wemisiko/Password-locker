#!/usr/bin/env python3
from passwd import User
from passwd import Credential
def create_new_user(user_name,password):

    new_user = User(user_name,password)
    return new_user

def save_user(user):

    user.save_user()

def delete_user(user):

    user.delete_user()

# def display_user():

#     return User.display_user()

def login_user(user_name,password):

    confirm_user = Credential.assert_user(user_name,password)
    return confirm_user

def create_new_credential(site,username,password):

    new_credential =Credential(site,username,password)
    return new_credential

def save_credential(credentials):

    credentials.save_credentials()

def delete_credential(credentials):

    credentials.delete_credentials()

def find_credential(username):

    return Credential.find_by_username(username)

def generate_password():

    gen_passwd= Credential.generate_password()
    return gen_passwd

def display_credentials():

    return Credential.display_credentials()

def check_existing_credential():
    return Credential.do_credential_exist

def main():
    print("Ssup ,welcome to Password locker.\n Select  a short code:\n ca - create account, \n lg -login")
    # print("Use the short codes:ca - create account, lg -login ")
    short_code = input().lower()
    print('\n')
    if short_code =='ca':
            print("To create an account")
    
            print("Create a user name")
            user_name = input("Enter username:")
            while True:
                print(" op -Create your password ,gp - generate password")
                pref_password = input()
                if pref_password == 'op':
                    password = input("Enter your password")
                    break
                elif pref_password == 'gp':
                    password = generate_password()
                    break
                else:
                    print('Wrong password,Use a special character and achive a length of 8')

                save_user(create_new_user(user_name,password))
                print(f"{user_name},account successful ready for login ,Use {password} as your password")
        
    elif short_code =="lg":
            print("Input login details")
            user_name = input("Your username:")
            password = input("Saved password:")
            userinfo= login_user(user_name,password)

            if login_user == userinfo:
                print(f"Welcome {user_name}")
                print('\n')
            else:
                print("You have not made a selection")
                print('\n')

    while True:
        print("To access your account use the short codes:cc- create credential \n  dc- display credential \n fc -find credential \n gp-generate password\n dc- delete credential \n ex-exit the application ") 
        short_code= input().lower() 
        print('\n')

        if short_code == 'cc':
            print("Create a new credential")
            print('\n')
            print("Enter name of site")
            site = input()
            print("Type username")
            username= input()
            print("Paste a password")
            password =input()
        
    
            save_credential(create_new_credential(site,username,password))
            print(f"Credential for {site} saved")
            print('\n')

        elif short_code == 'dc':

                    if display_credentials():
                        print("Below is a list of your credential")
                        print('\n')

                        for credential in display_credentials():
                            print(f"{credential.site} {credential.username} {credential.password}")
                            print('\n')

                    else:
                        print('\n')
                        print("Credential have not been saved in the application")
                        print('\n')

        elif short_code == 'fc':
                    print("Enter  a username to continue search")
                    print('\n')

                    search_username = input()
                    if check_existing_credential(search_username):
                        search_username =find_credential(search_username)
                        print('-'*50)
                        print(f"Site: {search_username.site}")
                        print('\n')
                        print(f"Username: {search_username.username}")
                        print('\n')
                        print(f"Password: {search_username.password}")
                    else:
                        print("The credential does not exist")


        elif short_code == 'dc':
                    print("Are you sure you want to delete the credential Y-yes N- no?")
                    print('\n')
                    short_code = input().upper
                    
                    while True:

                        if short_code == 'Y':
                            to_del_username = input()
                            if check_existing_credential(to_del_username):
                                to_del_username=delete_credential(to_del_username)

                            else:
                                print("cool")
                        elif short_code == 'N':
                            print("Action cancelled")
                            break
                        else:
                            print("Select an option")
                    
        elif short_code == 'ex':
         print("Bye")
        break
    else:
        print("Enter input again")

if __name__=='__main__':
     main()


 # print("Insert credential for deletion")
                         
    # elif short_code == 'N':
   #     print("Action cancelled succesfully")





 














