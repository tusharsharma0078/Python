from pathlib import Path

word = input("Enter the word: ")

with open(Path(__file__).parent / "newfile.txt", "r") as abc:
    lines = abc.readlines()

found = False

for i in range(len(lines)):
    if word in lines[i]:
        print("Word found at line", i + 1)
        print(lines[i])
        found = True
        break

if found == False:
    print("Word not found")