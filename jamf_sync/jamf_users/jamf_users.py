import requests

# Jamf Users Module

def get_user_by_email(jamf_url, headers, email):
    """
    Retrieve a user by email from Jamf Pro.

    :param jamf_url: URL of the Jamf Pro server.
    :param headers: Authorization headers for API requests.
    :param email: Email address of the user to retrieve.
    :return: User object or None if not found.
    """
    try:
        # Define the API endpoint to get a user by email
        user_endpoint = f"{jamf_url}/JSSResource/users/email/{email}"

        # Make the request to get the user by email
        response = requests.get(user_endpoint, headers=headers)

        if response.status_code == 200:
            users = response.json()["users"]

            if users:
                return users[0]
            else:
                print(f"User not found for email: {email}")
                return None
        else:
            print(f"Error fetching user information: {response.status_code} - {response.text}")
            return None

    except Exception as e:
        print(f"Error: {str(e)}")
        return None

# End of jamf_users.py module
