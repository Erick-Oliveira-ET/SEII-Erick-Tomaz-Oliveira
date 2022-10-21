import datetime
import pytz


print(datetime.date(2021, 12, 27))
print(datetime.date.today()) 
print(datetime.date.today().weekday()) 
print(datetime.date.today().isoweekday) 


tday = datetime.date.today()
tdelta = datetime.timedelta(days=7)
print(tday + tdelta)

tday = datetime.date.today()
bday = datetime.date(2022, 8, 21)
till_bday = bday - tday
print(till_bday.total_seconds())

t = datetime.time(9, 30, 45, 100000)
dt = datetime.time(2022, 8, 17, 5, 12, 7, 100000)
tdelta = datetime.timedelta(hour=12)
print(t.hour)
print(dt+tdelta)

dt = datetime.datetime(2016,  8, 17, 5, 12, 7, 100000)
tdelta = datetime.timedelta(days=7)
print(dt + tdelta)

dt_today = datetime.datetime.today()
dt_now = datetime.datetime.now()
dt_utcnow = datetime.datetime.utcnow()
print(dt_today)
print(dt_now)
print(dt_utcnow)

dt = datetime.datetime(2022, 8, 17, 5, 12, 7, tzinfo=pytz.UTC)
print(dt)
dt_now = datetime.datetime.now(tz=pytz.UTC)
print(dt_now)
dt_utcnow = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)
print(dt_utcnow)
dt_mtn = dt_utcnow.astimezone(pytz.timezone('US/Mountain'))
print(dt_mtn)
dt_mtn = datetime.datetime.now()
mtn_tz = pytz.timezone('US/Mountain')
dt_mtn = mtn_tz.localize(dt_mtn)
print(dt_mtn)
dt_east = dt_mtn.astimezone(pytz.timezone('US/Eastern'))
print(dt_east)
print(dt_mtn.strftime('%B %d, %Y'))
dt_str = 'March 15, 2021'
dt = datetime.datetime.strptime(dt_str, '%B %d, %Y')
print(dt)


