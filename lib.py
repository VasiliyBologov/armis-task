from datetime import datetime

def validate_datetime(value):
    """
    Function for validate and convert datetime input from string to datetime object.
    :param value: datetime or string
    :return: datetime
    """
    if value is not None:
        if isinstance(value, datetime):
            return value
        try:
            result = datetime.fromisoformat(value)
            return result
        except:
            pass
        for frmt in ('%Y-%m-%dT%H:%M:%S.%fZ', '%Y-%m-%dT%H:%M:%S', '%b %d %y', '%m% %d %y', '%Y/%m/%d',
                     '%m/%d/%Y', '%m/%d/%y', '%Y-%m-%d', '%Y.%m.%d', '%d.%m.%Y', '%d/%m/%Y', '%Y%m%d'):
            try:
                date_obj = datetime.strptime(value, frmt)
                return datetime.fromisoformat(date_obj.isoformat())
            except ValueError:
                pass
        raise ValueError('Invalid date format')
    return None