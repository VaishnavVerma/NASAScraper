def is_leap_year(year):
    """Check if a year is a leap year."""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

def generate_apod_urls(base_url, year):
    days_in_month = {
        1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
        7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    }

    days_in_month[2] = 29 if is_leap_year(year) else 28

    urls = []
    for month in range(1, 13):
        for day in range(1, days_in_month[month] + 1):
            formatted_month = f"{month:02d}"
            formatted_day = f"{day:02d}"
            url = f"{base_url}{formatted_month}{formatted_day}.html"
            urls.append(url)

    return urls