from datetime import datetime, timedelta

DATETIME_STRING_UTC_FULL = "2020-02-11T00:17:35.955835Z"
DATE_STRING = "2020-02-11"

def string2date(date_string):
  format = "%Y-%m-%dT%H:%M:%S.%fZ"
  return datetime.strptime(date_string, format)

def date_filter():
  return datetime.now() - timedelta(days=1*365)

date = string2date(DATE_STRING)
#print(date > (datetime.now() - timedelta(days=1*365)))
print(date > date_filter())