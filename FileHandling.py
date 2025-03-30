#1
import os
filename = input("Enter filename: ")
print("Exists:", os.path.exists(filename))

#2
file = open("sample.txt", "r")
try:
    for line in file:
        print(line.strip())
finally:
    file.close()

#3
name = input("Enter your name: ")
age = input("Enter your age: ")
city = input("Enter your city: ")

file = open("user_info.txt", "w")
try:
    file.write(f"Name: {name}\nAge: {age}\nCity: {city}\n")
finally:
    file.close()

print("Info written to user_info.txt")

#4
source=open("FirstFile.txt","r")
destination=open("SecondFile.txt","w")

try:
    data=source.read()
    destination=source.write(data)

finally:
    source.close()
    destination.close()

print("File copied to destination.txt")

#5
import shutil

shutil.move("file_to_move.txt", "target_folder/file_to_move.txt")
print("File moved successfully")

#6
import os

filename = input("Enter the filename to delete: ")

if os.path.exists(filename):
    os.remove(filename)
    print(f"{filename} has been deleted.")
else:
    print("File does not exist.")

#7
import os
import shutil

if not os.path.exists("data.txt"):
    f = open("data.txt", "w")
    try:
        f.write("This is some default text.\n")
    finally:
        f.close()
    print("data.txt created with default text.")
else:
    f = open("data.txt", "r")
    try:
        content = f.read()
        print("data.txt content:\n", content)
    finally:
        f.close()

# Copy to backup
src = open("data.txt", "r")
dest = open("data_backup.txt", "w")
try:
    dest.write(src.read())
finally:
    src.close()
    dest.close()

# Ask to delete backup
ans = input("Do you want to delete the backup file? (yes/no): ")
if ans.lower() == "yes":
    if os.path.exists("data_backup.txt"):
        os.remove("data_backup.txt")
        print("Backup deleted.")
    else:
        print("Backup file not found.")
else:
    print("Backup kept.")
