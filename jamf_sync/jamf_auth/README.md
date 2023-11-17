# Jamf Authentication Module



This module provides functions for authenticating with the Jamf Pro Classic API 
and obtaining authorization headers.



## Author

Jeremiah Pegues

Email: jeremiah@pegues.io



## License

Restricted use. All rights reserved. Exclusive license.



## Version

1.0.0



## Usage

Import the `jamf_auth` module and use the `authenticate_jamf` function to 
authenticate and obtain authorization headers for Jamf Pro API requests.



Example:



```python

import jamf_auth



# Define Jamf Pro API credentials

username = "your_username"

password = "your_password"

jamf_url = "https://your_jamf_url.com"



# Authenticate and obtain authorization headers

auth_headers = jamf_auth.authenticate_jamf(username, password, jamf_url)



if auth_headers:

# Use auth_headers for Jamf Pro API requests

# ...

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





---



# Jamf Auth Module



This Python module provides authentication for interacting with the Jamf Pro 
API.



## Usage



```python

from jamf_auth import JamfAuth



# Define the Jamf Pro API URL and API credentials

jamf_pro_url = "https://mdm.19parkinc.com:8443"

api_credentials = "dW5kZWZpbmVkOnVuZGVmaW5lZA=="



# Initialize the JamfAuth object

jamf_auth = JamfAuth(jamf_pro_url, api_credentials)



# Use the jamf_auth object for API requests

headers = jamf_auth.get_headers()

# Now, you can use the 'headers' in your API requests for authentication.

```



## Author



- Author: Jeremiah Pegues

- Email: jeremiah@pegues.io

- License: Restricted use, all rights reserved, exclusive license.

- Version: 1.0



For more information on the Jamf Pro API, please refer to the [Jamf Pro API 
Reference](https://developer.jamf.com/jamf-pro/v10.44.0/reference).

