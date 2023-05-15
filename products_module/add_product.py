import sqlite3,requests
import base64
from flask import jsonify
def add(request):
    try:
        # Get the data from the request body
        data = request.get_json()

        # Connect to the database
        conn = sqlite3.connect('petshop.db')
        cursor = conn.cursor()
        # print('HELLOOO',data.get('image'))
        # image = download_and_convert_to_base64(data.get['image'])
        # print(image)
        # Create a new product record
        cursor.execute("INSERT INTO Product (name, description, price, category, image, stock) VALUES (?, ?, ?, ?, ?, ?)",
                       (data.get('name'), data.get('description'), data.get('price'), data.get('category'), data.get('image'), data.get('stock')))
        conn.commit()

        # Close the database connection
        conn.close()

        return jsonify({'success': True, 'message': 'Product added successfully'}), 200

    except Exception as e:
        return jsonify({'success': False, 'message': str(e)}), 400
    
def download_and_convert_to_base64(image_url):
    try:
        # Download the image
        print('WORLDDD')
        response = requests.get(image_url)
        response.raise_for_status()

        # Convert the image to base64 encoding
        image_base64 = base64.b64encode(response.content).decode('utf-8')

        return image_base64

    except Exception as e:
        # Handle any errors that occur during the process
        print(f"Error: {str(e)}")
        return None