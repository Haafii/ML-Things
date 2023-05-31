import sys
import string

if len(sys.argv) != 2:
    print("Error: Please provide the filename as a command line argument.")
    sys.exit()

filename = sys.argv[1]

try:
    with open(filename) as file:
        letter_frequency = {}
        for letter in string.ascii_lowercase:
            letter_frequency[letter] = 0

        for line in file:
            line = line.lower().translate(str.maketrans('', '', string.punctuation + string.digits + ' '))
            for letter in line:
                if letter in letter_frequency:
                    letter_frequency[letter] += 1

        print("Letter Frequency:")
        for letter, frequency in letter_frequency.items():
            print(f"{letter}: {frequency}")

except FileNotFoundError:
    print(f"Error: File '{filename}' does not exist.")
