from pathlib import Path

with open(Path(__file__).parent/"newfile.txt","w") as abc:
    abc.write("hey,TUSHAR this side")

    # but one thing i write this in new empty file but when you new write 
    # in already existing file then previous content will be removed