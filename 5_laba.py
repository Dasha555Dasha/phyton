import os

def check_file_access(path):
    if os.access(path, os.R_OK | os.W_OK):
        return True
    else:
        return False

path = input("Введите путь к файлу: ")
access = check_file_access(path)

if access:
    print("Файл доступен для чтения и записи")
else:
    print("Файл недоступен для чтения и записи")
