# Palindrome Programs (Multiple Methods)

# METHOD 3: Using function (with print)
def palindrome_print(text):
    rev = ""
    for ch in text:
        rev = ch + rev

    if rev == text:
        print(f"'{text}' is a Palindrome")
    else:
        print(f"'{text}' is not a Palindrome")


text = input("Enter a string: ").lower()
palindrome_print(text)


# METHOD 4: Using function with return value
def palindrome_return(text):
    rev = ""
    for ch in text:
        rev = ch + rev
    return rev == text


text = input("\nEnter a string: ").lower()

if palindrome_return(text):
    print(f"'{text}' is a Palindrome")
else:
    print(f"'{text}' is not a Palindrome")


# METHOD 5: Palindrome check for number
def palindrome_number(num):
    temp = num
    rev = 0

    while num > 0:
        rev = rev * 10 + num % 10
        num //= 10

    return temp == rev


num = int(input("\nEnter a number: "))

if palindrome_number(num):
    print(f"{num} is a Palindrome")
else:
    print(f"{num} is not a Palindrome")
