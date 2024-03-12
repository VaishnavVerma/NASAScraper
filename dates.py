def is_leap_year(year):
    # Leap year logic: divisible by 4, but not divisible by 100 unless divisible by 400
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def generate_apod_urls(year):
    base_url = "https://apod.nasa.gov/apod/ap"
    days_in_month = {
        1: 31,  # January
        2: 29 if is_leap_year(year) else 28,  # February
        3: 31,  # March
        4: 30,  # April
        5: 31,  # May
        6: 30,  # June
        7: 31,  # July
        8: 31,  # August
        9: 30,  # September
        10: 31,  # October
        11: 30,  # November
        12: 31  # December
    }

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

# Example usage:
year = 2020  # Replace with the desired year
urls = generate_apod_urls(year)

