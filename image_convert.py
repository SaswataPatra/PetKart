import base64
import requests

def download_and_convert_to_base64(image_url):
    try:
        # Download the image
        response = requests.get(image_url)
        response.raise_for_status()

        # Convert the image to base64 encoding
        image_base64 = base64.b64encode(response.content).decode('utf-8')

        return image_base64

    except Exception as e:
        # Handle any errors that occur during the process
        print(f"Error: {str(e)}")
        return None
