import datetime
import pytz
import iso8601



date_str_iso = '2019-07-01T00:00:00Z'


date_str = str(iso8601.parse_date(date_str_iso)).split('+')[0]

print('initial date: ',date_str)


def convertdate ( dateVar ):
    """ this function translates date time into US/EU timezone with company standard formating """
    company_format = '%d-%m-%Y %H:%M:%S %p'

    date_obj = datetime.datetime.strptime(dateVar, '%Y-%m-%d %H:%M:%S')
    eastern = pytz.timezone('US/Eastern')
    tz_datetime_obj = eastern.localize(date_obj)
    # print(tz_datetime_obj)

    str_date = str(tz_datetime_obj)

    """store offset to hour and minute variable"""
    offset = str_date[19:]
    hours = int(offset.split(':')[0])
    minutes = int(offset.split(':')[1])
    print('offset: ', offset)

    """ return date in correct format"""
    result = tz_datetime_obj.replace(tzinfo=None)
    result_with_offset = result + datetime.timedelta(hours = hours, minutes = minutes)

    print(result_with_offset.strftime(company_format))


convertdate(date_str)

