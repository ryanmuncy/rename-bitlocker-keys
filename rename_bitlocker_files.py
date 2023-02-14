import os
import re

files = os.listdir(".")

unitNumberPattern = r"[DU]\d{4}"

bitLockerPattern = r"BitLocker Recovery Key [A-Z0-9]{8}-[A-Z0-9]{4}-[A-Z0-9]{4}-[A-Z0-9]{4}-[A-Z0-9]{12}"

userNamePattern = r"[A-Z][A-Za-z]*[A-Z]"

for file in files:
    matchUnitNumber = re.search(unitNumberPattern, file) 
    matchBitLocker  = re.search(bitLockerPattern, file)
    matchUser = re.search(userNamePattern, file)
    if(matchUnitNumber and matchBitLocker and matchUser):
    	print(f"{file}:\n{matchUnitNumber.group(0)}\n{matchBitLocker.group(0)}\n{matchUser.group(0)}\n")
    	new_filename = f"{matchUnitNumber.group(0)} - {matchUser.group(0)} - {matchBitLocker.group(0)}.txt"
    	os.rename(file, new_filename)
    else:
        print(f"\n{file} Has naming errors\n\nSkipping...\n")

