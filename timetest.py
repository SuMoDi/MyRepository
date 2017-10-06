import re
from datetime import datetime,timedelta,timezone

def to_timestamp(dt_str,tz_str):
    date1 = datetime.strptime(dt_str,'%Y-%m-%d %H:%M:%S')
    req = re.compile(r'^UTC([+-]\d+)')
    tz = re.match(req,tz_str)
    tz = tz.group(1)
    tz = int(tz)
    tz_shiqu = timezone(timedelta(hours=tz))
    date2 = date1.replace(tzinfo=tz_shiqu)
    return date2.timestamp()

t1 = to_timestamp('2015-5-31 16:10:30', 'UTC-09:00')
print (t1)
