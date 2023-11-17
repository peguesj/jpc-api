# Jamf Locations Module



This module provides functions for updating the location information of a 
computer in Jamf Pro.



## Author

Jeremiah Pegues

Email: jeremiah@pegues.io



## License

Restricted use. All rights reserved. Exclusive license.



## Version

1.0.0



## Usage

Import the `jamf_locations` module and use the `update_computer_location` 
function to update the location information of a computer in Jamf Pro.



Example:



```python

import jamf_locations

import jamf_auth

import os



# Load credentials from environment variables or a .env file

username = os.environ.get("JAMF_USERNAME")

password = os.environ.get("JAMF_PASSWORD")

jamf_url = os.environ.get("JAMF_URL")



# Authenticate and obtain authorization headers

auth_headers = jamf_auth.authenticate_jamf(username, password, jamf_url)



if auth_headers:

# Update computer location

computer_id = 123  # Specify the computer ID

username = "user123"  # Specify the username for the location

success = jamf_locations.update_computer_location(jamf_url, auth_headers, 
computer_id, username)



if success:

print(f"Successfully updated computer location for computer ID 
{computer_id}")

else:

print(f"Failed to update computer location.")

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

