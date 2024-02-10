import datetime
import pytz
import iso8601

def convert_date_to_company_format(date_iso_str):
    """
    Convert an ISO 8601 datetime string to the company's standard format in US/Eastern time zone.
    Args:
    date_iso_str (str): ISO 8601 format datetime string.
    
    Returns:
    str: Datetime in company's standard format '%d-%m-%Y %H:%M:%S %p' in US/Eastern time zone.
    """
    try:
        # Parse the ISO 8601 string to datetime object
        date_obj = iso8601.parse_date(date_iso_str)

        # Convert to US/Eastern time zone
        eastern = pytz.timezone('US/Eastern')
        tz_date_obj = date_obj.astimezone(eastern)

        # Format date to company's standard
        company_format = '%d-%m-%Y %H:%M:%S %p'
        formatted_date = tz_date_obj.strftime(company_format)
        return formatted_date

    except Exception as e:
        print("Error in date conversion:", e)
        return None

# Test the function
date_str_iso = '2019-07-01T00:00:00Z'
print('Initial date:', date_str_iso)
print('Converted date:', convert_date_to_company_format(date_str_iso))
