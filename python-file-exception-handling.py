def integer_number():
    try:
        num = int(input("Enter an integer number: "))
        result = 100 / num

        print("Result:", result)

        with open("Student.txt", "w") as file:
            file.write(f"Number entered: {num}\n")
            file.write(f"Result: {result}\n")

    except ValueError:
        print("Invalid input! Please enter a valid integer.")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    except Exception as e:
        print("Unexpected error occurred:", e)
    finally:
        print("Execution completed.\n")


integer_number()

# Reading file
try:
    with open("Student.txt", "r") as file:
        print("File Content:")
        print(file.read())
except FileNotFoundError:
    print("File not found.")
