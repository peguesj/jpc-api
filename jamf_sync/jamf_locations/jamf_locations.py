import requests
import xml.etree.ElementTree as ET

# Jamf Locations Module

def update_computer_location(jamf_url, headers, computer_id, username):
    """
    Update the location information of a computer in Jamf Pro.

    :param jamf_url: URL of the Jamf Pro server.
    :param headers: Authorization headers for API requests.
    :param computer_id: ID of the computer to update.
    :param username: Username for the computer location.
    :return: True if successful, False otherwise.
    """
    try:
        # Define the API endpoint to update the computer location
        computer_endpoint = f"{jamf_url}/JSSResource/computers/id/{computer_id}"

        # Create a dictionary with the location payload
        computer_location_payload = {
            "location": {
                "username": username
            }
        }

        # Convert dictionary to XML
        def dict_to_xml(parent, dic):
            for key, value in dic.items():
                if isinstance(value, dict):
                    child = ET.SubElement(parent, key)
                    dict_to_xml(child, value)
                else:
                    ET.SubElement(parent, key).text = str(value)

        root = ET.Element("computer")
        dict_to_xml(root, computer_location_payload)
        computer_location_payload_as_xml = ET.tostring(root, 'utf-8')

        # Modify headers to accept XML (instead of JSON)
        headers["Content-Type"] = "application/xml"
        headers["Accept"] = "application/xml"

        # Make the request to update the computer location
        response = requests.put(
            computer_endpoint,
            headers=headers,
            data=computer_location_payload_as_xml
        )

        if response.status_code == 200:
            return True
        else:
            print(f"Error updating computer location: {response.status_code} - {response.text}")
            return False

    except Exception as e:
        print(f"Error: {str(e)}")
        return False

# End of jamf_locations.py module
