#python script to access download folder and clear specific files ending with a specific extension

import os
import glob

home = os.getenv("HOME")

file_ext = input("enter the file extension you want to delete from the downloads file (ex: .pdf, .png) :")

path = home+"/Downloads/*"+str(file_ext)

file_path = glob.glob(path)

print("file path: ",file_path)

if len(file_path) > 0:
    for file in file_path: 
        if os.path.isfile(file):
            os.remove(file)
            print("File :"+str(file)+" has successfully been deleted")
        else:
            print("File :"+str(file)+" does not exist")
# else:
#     print("there is only 1 file..:", file_path)
#     if os.path.isfile(file_path):
#         os.remove(file_path)
#         print("File :"+str(file_path)+" has successfully been deleted")
#     else:
#         print("File :"+str(file_path)+" does not exist")