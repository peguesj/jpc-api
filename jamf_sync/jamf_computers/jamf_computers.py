# Author: Jeremiah Pegues
# Email: jeremiah@pegues.io
# License: Restricted use, all rights reserved, exclusive license.

import requests

class JamfComputers:
    def __init__(self, jamf_pro_url, api_credentials):
        self.jamf_pro_url = jamf_pro_url
        self.api_credentials = api_credentials
        self.headers = {
            "Authorization": f"Basic {api_credentials}",
            "Content-Type": "application/json",
            "Accept": "application/json"
        }

    def get_computers(self):
        try:
            response = requests.get(
                f"{self.jamf_pro_url}/JSSResource/computers",
                headers=self.headers
            )
            response.raise_for_status()
            return response.json()["computers"]
        except requests.exceptions.RequestException as e:
            print(f"Error fetching computer information: {e}")
            return []

    def get_computer_extension_attributes(self, computer_id):
        try:
            response = requests.get(
                f"{self.jamf_pro_url}/JSSResource/computers/id/{computer_id}/subset/extension_attributes",
                headers=self.headers
            )
            response.raise_for_status()
            return response.json()["computer"]["extension_attributes"]
        except requests.exceptions.RequestException as e:
            print(f"Error fetching extension attributes for computer: {e}")
            return []

    def update_computer_location(self, computer_id, location_payload):
        try:
            response = requests.put(
                f"{self.jamf_pro_url}/JSSResource/computers/id/{computer_id}",
                headers=self.headers,
                json=location_payload
            )
            response.raise_for_status()
            return True
        except requests.exceptions.RequestException as e:
            print(f"Error updating computer location: {e}")
            return False
