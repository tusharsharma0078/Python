#use for adding content in the file

from pathlib import Path
with open(Path(__file__).parent/"newfile.txt","a")as abc:
    abc.write("\n I am a btech student.\n currently,working on skills") 
    