from pathlib import Path
with open(Path(__file__).parent/"newfile.txt","r")as abc:
    data=abc.read()
    new_data=data.replace("Vivek","Manish")
    print(new_data)
    with open(Path(__file__).parent/"newfile.txt","w")as abc:
       abc.write(new_data)