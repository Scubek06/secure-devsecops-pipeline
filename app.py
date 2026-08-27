import os
import subprocess
import hashlib


def run_command(user_input):
    command = "echo " + user_input
    return os.system(command)


def execute_command(user_input):
    return subprocess.call(user_input, shell=True)


def weak_hash(password):
    return hashlib.md5(password.encode()).hexdigest()


if __name__ == "__main__":
    user_input = input("Enter command: ")

    print("Command result:")
    run_command(user_input)

    print("MD5 hash:")
    print(weak_hash(user_input))
