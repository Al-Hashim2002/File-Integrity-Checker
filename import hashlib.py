import hashlib
import builtins


def calculate_hash(filename):
    sha256 = hashlib.sha256()

    with open(filename, "rb") as file:
        while True:
            data = file.read(4096)

            if not data:
                break

            sha256.update(data)

    return sha256.hexdigest()


def create_baseline(filename):
    file_hash = calculate_hash(filename)

    with open("baseline.txt", "w") as file:
        file.write(file_hash)

    builtins.print("\nBaseline created successfully.")
    builtins.print("Original SHA-256:")
    builtins.print(file_hash)


def check_integrity(filename):
    current_hash = calculate_hash(filename)

    try:
        with open("baseline.txt", "r") as file:
            original_hash = file.read().strip()

    except FileNotFoundError:
        builtins.print("\nNo baseline found.")
        builtins.print("Create a baseline first.")
        return

    builtins.print("\nOriginal SHA-256:")
    builtins.print(original_hash)

    builtins.print("\nCurrent SHA-256:")
    builtins.print(current_hash)

    if original_hash == current_hash:
        builtins.print("\nSTATUS: File has NOT been modified.")
    else:
        builtins.print("\nSTATUS: WARNING - File has been modified!")


while True:

    builtins.print("\n================================")
    builtins.print("      FILE INTEGRITY CHECKER")
    builtins.print("================================")

    builtins.print("1. Create baseline")
    builtins.print("2. Check file integrity")
    builtins.print("3. Exit")

    choice = input("\nChoose an option: ")

    if choice == "1":

        filename = input("Enter file name: ")

        try:
            create_baseline(filename)
        except FileNotFoundError:
            builtins.print("\nError: File not found.")

    elif choice == "2":

        filename = input("Enter file name: ")

        try:
            check_integrity(filename)
        except FileNotFoundError:
            builtins.print("\nError: File not found.")

    elif choice == "3":

        builtins.print("\nExiting...")
        break

    else:

        builtins.print("\nInvalid option.")