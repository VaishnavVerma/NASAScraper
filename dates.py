base_url = "https://apod.nasa.gov/apod/ap96"

# Dictionary to store the number of days in each month
days_in_month = {
    1: 31,  # January
    2: 29,  # February (leap year is considered for simplicity)
    3: 31,  # March
    4: 30,  # April
    5: 31,  # May
    6: 30,  # June
    7: 31,  # July
    8: 31,  # August
    9: 30,  # September
    10: 31, # October
    11: 30, # November
    12: 31  # December
}

def generate_urls():
    urls = []
    for month in range(1, 13):
        for day in range(1, days_in_month[month] + 1):
            # Format the month and day to have leading zeros if needed
            formatted_month = f"{month:02d}"
            formatted_day = f"{day:02d}"
            
            # Construct the complete URL
            url = f"{base_url}{formatted_month}{formatted_day}.html"
            urls.append(url)

    return urls
