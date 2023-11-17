# Jamf Users Module



This module provides functions for working with user-related data in Jamf Pro.



## Author

Jeremiah Pegues

Email: jeremiah@pegues.io



## License

Restricted use. All rights reserved. Exclusive license.



## Version

1.0.0



## Usage

Import the `jamf_users` module and use the `get_user_by_email` function to 
retrieve a user by email from Jamf Pro.



Example:



```python

import jamf_users

import jamf_auth

import os



# Load credentials from environment variables or a .env file

username = os.environ.get("JAMF_USERNAME")

password = os.environ.get("JAMF_PASSWORD")

jamf_url = os.environ.get("JAMF_URL")



# Authenticate and obtain authorization headers

auth_headers = jamf_auth.authenticate_jamf(username, password, jamf_url)



if auth_headers:

# Get a user by email

email = "user@example.com"

user = jamf_users.get_user_by_email(jamf_url, auth_headers, email)



if user:

print(f"User Name: {user['name']}")

else:

print(f"User not found for email: {email}")

else:

print("Authentication failed.")

```



## Requirements

- Python 3

- Requests library (install with `pip install requests`)

- Environment manager like `dotenv` or a credentials store



## Compatibility

- Jamf Pro Classic API

- Minimum Jamf Pro Version: [Specify Minimum Version]



For more details on the Jamf Pro Classic API, refer to the [Jamf Pro API 
Reference](https://developer.jamf.com/jamf-pro/v10.44.0/reference).

