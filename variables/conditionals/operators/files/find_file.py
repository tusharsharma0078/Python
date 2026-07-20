# now i want find the word in the file newfile.txt
from pathlib import Path

word = input("Enter the word: ")

file_path = Path(__file__).parent / "file_i" / "newfile.txt"

with open(file_path, "r") as abc:
    data = abc.read()

if word in data:
    print("Word found")
else:
    print("Word not found")