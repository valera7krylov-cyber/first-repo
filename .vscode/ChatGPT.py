name = input("Enter your name: ")

while True:
    print("\nMenu:")
    print("1 - age info")
    print("2 - full info")
    print("3 - exit")

    choice = input("Choose option: ")

    if choice == "1":
        while True:
            age_input = input("Enter your age: ")

            if age_input.isdigit():
                age = int(age_input)
                age5 = age + 5
                print(f"In 5 years you will be {age5} years old")
                break
            else:
                print("Error: enter a valid number")

    elif choice == "2":
        if "age" in locals():
            print(f"Hello, {name}! You are {age} years old.")
        else:
            print("Age not set yet. Choose option 1 first.")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid option, try again")