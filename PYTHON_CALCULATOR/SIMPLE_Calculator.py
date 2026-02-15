def calculator():
    print("*** Simple Calculator ***")
    print("-----> Display Menu <-----")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 5:
        print("Exiting calculator...")
        return

    if choice in [1, 2, 3, 4]:
        num_1, num_2 = map(int, input("Enter two numbers (a b): ").split())

        if choice == 1:
            print("Addition:", num_1 + num_2)

        elif choice == 2:
            print("Subtraction:", num_1 - num_2)

        elif choice == 3:
            print("Multiplication:", num_1 * num_2)

        elif choice == 4:
            if num_2 == 0:
                print("Error: Division by zero is not allowed.")
            else:
                print("Division:", num_1 / num_2)

    else:
        print("Invalid choice.")

calculator()
