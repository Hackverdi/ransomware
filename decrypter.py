import os 
from cryptography.fernet import Fernet
dir_file = os.listdir()
file_list = []

for file in dir_file:
    if ".py" in file or ".json" in file or file == "generatedkey.key":
        continue
    if os.path.isfile(file):
        file_list.append(file)

with open("generatedkey.key","rb") as generatedkey:
    secret_key = generatedkey.read()

for file in file_list:
    with open(file,"rb") as the_file:
        contents = the_file.read()
    contents_decrypted = Fernet(secret_key).decrypt(contents)
    with open(file,"wb") as the_file:
        the_file.write(contents_decrypted) 



