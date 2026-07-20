# now i want find the word in the file newfile.txt
from pathlib import Path
word=input("Enter the word")
with open(Path(__file__).parent/"newfile.txt","r") as abc:
    data=abc.read()
    if word in data:
        print("word found")
    else:
        print("noe found")