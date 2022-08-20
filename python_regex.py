import re

# string = "Enter your name in the chat"
# # Search for name in the string
# match = re.search(r'name', string)

greetings = 'hexxxxxo'
match = re.search(r'he.{5}o', greetings)

# phone_number = "09123456789"
# phone_number_string = input("Enter your phone number : ")
# match = re.search(r'^\d{11}$', phone_number_string)
# if match:
#     print("Your phone number is valid:", match.group())
# else:
#     print(f'{phone_number_string} is not a valid phone number')

full_name_string = "Samuel Chibuez"
match = re.search(r'^[a-zA-Z]+\s[a-zA-Z]+$', full_name_string)
if match:
    print(f'{full_name_string} is valid. congrats!')
else:
    print(f'{full_name_string} is NOT valid')


string = "NIIT Classroom"
result = re.split(r'\s', string)
print(result)

new_str = re.sub(r'\s', '-', string)
print('My new word : ', new_str)