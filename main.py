# import smtplib

# my_email = "erhardbr@gmail.com"
# password = "python1429$$"

# with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email, to_addrs=my_email,
#                         msg="Subject:Hello\n\nThis is the body of my email")

import datetime as dt

# get current data and time
now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()


date_of_birth = dt.datetime(year=1987, month=10, day=26, hour=7, minute=15)
print(date_of_birth)
