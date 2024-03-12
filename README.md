# NASAScraper

NASAScraper is a Python project designed to scrape data from NASA's Astronomy Picture of the Day (APOD) website. It retrieves information about the featured image, its description, and related details for a specified range of dates.

## Features

- Generates URLs for APOD images based on a given year.
- Scrapes image information, description, and URL from the APOD website.
- Saves scraped data in JSON format for further analysis or reference.

## Getting Started

### Prerequisites

- Python 3.x

Required Python packages can be installed using:

```bash
pip install -r requirements.txt
```

### Usage

1. Clone the repository:

```bash
git clone https://github.com/VaishnavVerma/NASAScraper.git
cd astroscraper
```

2. Run the project:

```bash
python main.py
```

### View the scraped data:

The scraped data is saved in the `image_data.json` file.

## Configuration

Adjust the `base_url` and `current_year` variables in `main.py` to set the desired NASA APOD URL and year.

## License

This project is licensed under the MIT License.

## Acknowledgments

- Beautiful Soup - HTML parsing library.
- Requests - HTTP library for making requests.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request.

## Author

Vaishnav Verma
