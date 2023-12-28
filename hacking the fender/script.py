

import csv
import json

# Initialize an empty list to store compromised user names
compromised_users = []

# Open the 'passwords.csv' file and store it in a file object called password_file
with open('passwords.csv', mode='r') as password_file:
    # Create a CSV reader object
    csv_reader = csv.DictReader(password_file)

    # Iterate through each row in the CSV file
    for password_row in csv_reader:
        # Extract the username and add it to compromised_users list
        compromised_users.append(password_row['Username'])

# Exiting the with block for "passwords.csv"

# Start a new with block to open 'compromised_users.txt' in write mode
with open('compromised_users.txt', mode='w') as compromised_user_file:
    # Inside this block, you can write to compromised_user_file
    # Write each username from compromised_users to the file
    for user in compromised_users:
        compromised_user_file.write(user + '\n')

# Create a Python dictionary for the boss message
boss_message_dict = {
    "recipient": "The Boss",
    "message": "Mission Success"
}

# Encoding the boss_message_dict as JSON and writing to a file 'boss_message.json'
with open('boss_message.json', 'w') as boss_message:
    json.dump(boss_message_dict, boss_message)

# Exiting the with block for 'boss_message.json'

# Slash Null's signature
slash_null_sig = """
 _  _     ___   __  ____             
/ )( \\   / __) /  \\(_  _)            
) \\/ (  ( (_ \\(  O ) )(              
\\____/   \\___/ \\__/ (__)             
 _  _   __    ___  __ _  ____  ____  
/ )( \\ / _\\  / __)(  / )(  __)(    \\ 
) __ (/    \\( (__  )  (  ) _)  ) D ( 
\\_)(_)/\\_/\\_/ \\___)(__\\_)(____)(____/ 
        ____  __     __   ____  _  _ 
 ___   / ___)(  )   / _\\ / ___)/ )( \\
(___)  \\___ \\/ (_/\\/    \\\\___ \\) __ (
       (____/\\____/\\_/\\_/(____/\\_)(_/
 __ _  _  _  __    __                
(  ( \\/ )( \\(  )  (  )               
/    /) \\/ (/ (_/\\/ (_/\\             
\\_)__)\\____/\\____/\\____/
"""

# Start a new with block to open 'new_passwords.csv' in write mode
with open('new_passwords.csv', mode='w') as new_passwords_obj:
    # Write Slash Null's signature to 'new_passwords.csv'
    new_passwords_obj.write(slash_null_sig)

# Now, 'new_passwords.csv' contains Slash Null's signature
