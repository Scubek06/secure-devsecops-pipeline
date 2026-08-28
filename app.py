import hashlib
import subprocess


def run_command(user_input):
    result = subprocess.run(
        ["echo", user_input],
        capture_output=True,
        text=True,
        check=True
    )
    return result.stdout.strip()


def secure_hash(password):
    return hashlib.sha256(password.encode()).hexdigest()


if __name__ == "__main__":
    user_input = input("Enter text: ")

    print("Command result:")
    print(run_command(user_input))

    print("SHA-256 hash:")
    print(secure_hash(user_input))
