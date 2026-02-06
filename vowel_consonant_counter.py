"""
Program: Vowel and Consonant Counter
Description: Counts vowels, consonants, and total characters in a word
"""

def count_vowels_consonants(word: str):
    vowels = ('a', 'e', 'i', 'o', 'u')
    vowel_count = 0
    consonant_count = 0

    for ch in word:
        if ch.isalpha():  # count only letters
            if ch in vowels:
                vowel_count += 1
            else:
                consonant_count += 1

    return vowel_count, consonant_count


if __name__ == "__main__":
    word = input("Enter the word: ").lower()

    v_count, c_count = count_vowels_consonants(word)

    print("Number of vowels:", v_count)
    print("Number of consonants:", c_count)
    print("Total characters:", len(word))
