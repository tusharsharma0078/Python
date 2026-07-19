 #now i want to read first 5 charcters from the file
from pathlib import Path
with open(Path(__file__).parent/ "Demo.txt","r") as abc:
 # when we use with then file will close automatically
    data=abc.read(5)
    print(data)