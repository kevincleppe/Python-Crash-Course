filename= '10_3.txt'
prompt=input("What would you like to write to the file: ")
with open(filename, 'w') as file_object:
    file_object.write(f"\n{prompt}")
    