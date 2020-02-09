file_handle = open("user_number.txt","r")
lines = file_handle.read()
print(lines.splitlines()[-1])

file_handle.close()
