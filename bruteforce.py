def check_password(password):
    correct_password = "Academy24"
    if password == correct_password:
        return True
    return False

def brute_force(password_list):
    for password in password_list:
        print(checking password {password})
        if check_password(password):
            print(access granted {password})
            return password
        print(access denied)
        return None

with open('passwords.txt', 'r') as file:
    passwords = file.readlines()
 
passwords = [password.strip()for password in passwords]

brute_force(passwords)