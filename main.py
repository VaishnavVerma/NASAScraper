import json
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from date_generator import generate_apod_urls

def process_response(response):
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')  # Specify parser explicitly
        paragraph_tag = soup.find('p')
        desired_text = paragraph_tag.get_text(strip=True).split('.')[0]

        image_tag = soup.find('img')
        if image_tag:
            image_url = urljoin(response.url, image_tag['src'])
            date = response.url[-11:-5]
            file_id = date

            data = {
                'id': file_id,
                'Archivepix': desired_text,
                'image_url': image_url,
                'web_page_url': response.url
            }

            json_data = json.dumps(data, indent=4)

            with open('image_data.json', 'a') as json_file:
                json_file.write(json_data + '\n')
            print("Image ID, URL, and webpage URL saved to 'image_data.json'.")
        else:
            print("No image found on the page.")
    else:
        print(f"Failed to retrieve the page. Status code: {response.status_code}")

# Example usage:
b_url = "https://apod.nasa.gov/apod/ap"
current_year = 2023
current_year_last = str(current_year)[-2:]  # Convert to string and extract the last two characters
base_url = f"https://apod.nasa.gov/apod/ap{current_year_last}"
urls = generate_apod_urls(base_url, current_year)

for url in urls:
    response = requests.get(url)
    process_response(response)
