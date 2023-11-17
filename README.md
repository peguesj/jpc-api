# Jamf Connect All Users Sync Script



This Python script is designed to synchronize user information with Jamf Pro. It 
retrieves computer information from Jamf Pro and associates each computer with 
its corresponding user based on a specified extension attribute.



## Author

Jeremiah Pegues

Email: jeremiah@pegues.io



## License

Restricted use. All rights reserved. Exclusive license.



## Version

1.0.0



## Usage

1. Import the necessary [modules](modules/README.md):

- `jamf_auth` for Jamf Pro authentication.

- `jamf_computers` for working with computer data.

- `jamf_users` for working with user data.

- `jamf_locations` for updating computer location.



2. Authenticate to Jamf Pro using `jamf_auth.authenticate_jamf` to obtain 
authorization headers.



3. Use `jamf_computers.get_computers` to retrieve a list of all computers with 
extension attributes.



4. Iterate through the computers and extract the user information.



5. Verify if the user information is an email address.



6. Use `jamf_users.get_user_by_email` to find the user's ID by email.



7. Add the computer to the user using `jamf_users.add_computer_to_user`.



8. If the user is not found, update the computer location using 
`jamf_locations.update_computer_location`.



Example:



```python

import jamf_auth

import jamf_computers

import jamf_users

import jamf_locations

import os



# Load credentials from environment variables or a .env file

username = os.environ.get("JAMF_USERNAME")

password = os.environ.get("JAMF_PASSWORD")

jamf_url = os.environ.get("JAMF_URL")



# Authenticate and obtain authorization headers

auth_headers = jamf_auth.authenticate_jamf(username, password, jamf_url)



if auth_headers:

# Get a list of all computers

computers = jamf_computers.get_computers(jamf_url, auth_headers)



for computer in computers:

# Extract computer information and user information

computer_id = computer["id"]

computer_name = computer["name"]

extension_attributes = computer["extension_attributes"]

user_information = None



for attribute in extension_attributes:

if attribute["id"] == extension_attribute_id:

user_information = attribute["value"]

break



if user_information:

# Verify if the value is an email address

if re.match(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}", 
user_information):

# Use the email to find the user's ID

user_email = user_information

user_id = jamf_users.get_user_by_email(jamf_url, auth_headers, 
user_email)



if user_id:

# Add the computer to the user using their ID

jamf_users.add_computer_to_user(jamf_url, auth_headers, 
user_id, computer_id)

else:

# User not found, update computer location

computer_username = user_email.split('@')[0]

jamf_locations.update_computer_location(jamf_url, 
auth_headers, computer_id, computer_username)

else:

print(f"Value is not an email address: {user_information}")

else:

print(f"No user information found for computer {computer_name}")

else:

print("Authentication failed.")

```



## Requirements

- Python 3

- Requests library (install with `pip install requests`)

- Environment manager like `dotenv` or a credentials store



## Compatibility

- Jamf Pro Classic API

- Jamf Pro Version: 10.44.0 or later

- Jamf Connect Version: 2.24.0 or later



For more details on the Jamf Pro Classic API, refer to the [Jamf Pro API 
Reference](https://developer.jamf.com/jamf-pro/v10.44.0/reference).





---



# Jamf Scripts and Modules



This directory contains [scripts](scripts/README.md) and [modules](modules/README.md) for interacting with Jamf Pro and 
Jamf Connect.



## Contents



- [Scripts](./[scripts](scripts/README.md)): Contains [scripts](scripts/README.md) for specific tasks.

- [Modules](./[modules](modules/README.md)): Contains reusable Python [modules](modules/README.md) for Jamf Pro interaction.



## Requirements



- Python 3.6+

- Requests library for Python (`pip install requests`)



## Usage



### Scripts



- `getJamfConnectUserEA.sh`: Retrieves the current Jamf Connect user and sets it as an Extension Attribute in Jamf Pro.

- `jamfConnectAllUsersSync.py`: Syncs user information between Jamf Pro and Jamf Connect.



### Modules



- `jamf_auth.py`: Provides authentication to the Jamf Pro API.

- `jamf_computers.py`: Handles computer-related actions in Jamf Pro.

- `jamf_locations.py`: Manages computer location information in Jamf Pro.

- `jamf_users.py`: Deals with user-related actions in Jamf Pro.



## Attribution



- Author: Jeremiah Pegues

- Email: jeremiah@pegues.io

- License: Restricted use, all rights reserved, exclusive license.



For more information on the Jamf Pro API, please refer to the [Jamf Pro API 
Reference](https://developer.jamf.com/jamf-pro/v10.44.0/reference).



This project is compatible with Jamf Pro Classic API and Jamf Connect version 
2.24.0 or later.

