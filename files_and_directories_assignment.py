import os
os.path.isfile('/file.txt')
os.path.isdir('dir')
os.path.exists('file.txt')

#line 7-10, getting directory and file input from user
directory = input("Enter the name of the directory you want to save your file:")
print(directory)

file = input(f"Enter the name of your file you want to save in {directory}:")
print(file)

#Whenever I input my own directory or file, the program would run fine. If I tried using a directory like main.py it would error out saying it already existed. I made this while loop and try catch to help with the error and it no longer came up.
while True:
  if not os.path.isdir(directory):
    try:
      os.makedirs(directory)
    except:
      print("Enter your information down below:")
    break

path = directory + file

#appending so it will add the requested items
contact_info = open(path,'a')

#getting user contact info
name = input("Enter your name:")
contact_info.write(name + ',')
address = input("Enter your address:")
contact_info.write(address + ',')
phone_number = input("Enter your phone number:")
contact_info.write(phone_number)
contact_info.close()

#displaying user input to the user
display_contact_info = open(path, 'r')
display = display_contact_info.read()
print(f"Here is the information that you entered: {display}")

#Os module in python with examples. GeeksforGeeks. (2022, June 16). Retrieved August 4, 2022, from https://www.geeksforgeeks.org/os-module-python-examples/ 