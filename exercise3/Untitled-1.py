try:
    username = input("Enter username: ")
    age = int(input("Enter age: "))

    if username.strip() == "":
        raise ValueError("Username cannot be empty.")

    if age <= 0:
        raise ValueError("Age must be positive.")

    with open("users.txt", "a") as file:
        file.write(f"{username} - {age}\n")

    print("User saved successfully!")

except ValueError as e:
    print("Error:", e)

finally:
    try:
        print("\nSaved Users:")
        with open("users.txt", "r") as file:
            for line in file:
                print(line.strip())
    except FileNotFoundError:
        print("No users saved yet.")

    print("System complete.")   