import glob2
import datetime
"""
This is the file from udemy. It needs to be located correctly in the SEPARATE FOLDER before running.
"""
filenames=glob2.glob("*.txt")

with open(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f")+".txt", 'w') as file:
    for filename in filenames:
        with open(filename,"r") as f:
            file.write(f.read()+"\n")
