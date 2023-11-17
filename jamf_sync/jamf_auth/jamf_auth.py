import requests
import base64

# Jamf Authentication Module

def authenticate_jamf(username, password, jamf_url):
    """
    Authenticate with the Jamf Pro Classic API and obtain authorization headers.

    :param username: Jamf Pro username.
    :param password: Jamf Pro password.
    :param jamf_url: URL of the Jamf Pro server.
    :return: Authorization headers as a dictionary.
    """
    try:
        # Combine the username and password for basic authentication
        api_credentials = f"{username}:{password}"

        # Encode API credentials in base64
        api_credentials_base64 = base64.b64encode(api_credentials.encode()).decode()

        # Set headers for authentication request
        auth_headers = {
            "Authorization": f"Basic {api_credentials_base64}",
            "Content-Type": "application/x-www-form-urlencoded"
        }

        # Define authentication endpoint URL
        auth_endpoint = f"{jamf_url}/api/v1/auth/token"

        # Make the request to obtain the access (bearer) token
        auth_response = requests.post(auth_endpoint, headers=auth_headers)

        if auth_response.status_code == 200:
            # Extract the access token from the response
            access_token = auth_response.json().get("token")

            if access_token:
                # Set headers with the access token for subsequent API requests
                headers = {
                    "Authorization": f"Bearer {access_token}",
                    "Content-Type": "application/json",
                    "Accept": "application/json"
                }

                return headers
            else:
                print("Access token not found in the authentication response.")
                return None
        else:
            print(f"Error obtaining access token: {auth_response.status_code} - {auth_response.text}")
            return None

    except Exception as e:
        print(f"Authentication error: {str(e)}")
        return None

# End of jamf_auth.py module
