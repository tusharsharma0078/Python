# IN the r+ we read and write together
from pathlib import Path
with open(Path(__file__).parent/"newfile.txt","r+")as abc:
    print(abc.read())
    abc.write("\n and my friend name is Vivek")
 #with this method we can read and write the file together without deleting
 #existing content 