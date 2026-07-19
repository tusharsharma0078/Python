   #now i want to read onlyone line
from pathlib import Path
with open(Path(__file__).parent/"Demo.txt","r") as abc:
     data=abc.readline()
     print(data)