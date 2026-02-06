# Palindrome Program (String)

# METHOD 1: Without slicing
text = input("Enter a string: ").lower()
rev = ""

for ch in text:
    rev = ch + rev

if rev == text:
    print(f"'{text}' is a Palindrome")
else:
    print(f"'{text}' is not a Palindrome")


# METHOD 2: With slicing

text = input("\nEnter a string: ").lower()

if text == text[::-1]:
    print(f"'{text}' is a Palindrome")
else:
    print(f"'{text}' is not a Palindrome")
