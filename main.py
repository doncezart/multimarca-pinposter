import requests
import time

ACCESS_TOKEN = 'YOUR_ACCESS_TOKEN'
BOARD_ID = 'BOARD_ID'

def bulk_pin_upload_sequence():
    headers = {
        'Authorization': f'Bearer {ACCESS_TOKEN}',
        'Content-Type': 'application/json',
    }
    
    base_url = "https://raw.githubusercontent.com/doncezart/test/refs/heads/main/"
    description = "DESCRIPTION"
    link = "REDIRECT URL"  # Add your destination URL here
    
    for i in range(1, 117):
        image_url = f"{base_url}{str(i).zfill(3)}.jpg"
        
        data = {
            'board_id': BOARD_ID,
            'media_source': {
                'source_type': 'image_url',
                'url': image_url
            },
            'description': description,
            'link': link  # Added link parameter
        }
        
        response = requests.post(
            'https://api.pinterest.com/v5/pins',
            headers=headers,
            json=data
        )
        
        if response.status_code == 201:
            print(f"Successfully pinned image: {i}")
        else:
            print(f"Failed to pin image: {i}")
            print(f"Error: {response.text}")
        
        time.sleep(1)  # Delay to avoid rate limiting
