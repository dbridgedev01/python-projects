import smtplib
from random import choice
import datetime as dt
import calendar

days_list = list(calendar.day_name)

#
# with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
#     # Opening A Secure Connection Using Transport Layer Security
#     connection.starttls()
#     connection.login(user=mail_id, password=password)
#     connection.sendmail(from_addr=mail_id,
#                         to_addrs="",
#                         msg="Subject:Hello\n\nHello and Welcome!"
#                         )


with open("quotes.txt") as quotes_file:
    quotes_list = quotes_file.readlines()

now = dt.datetime.now()
quote = choice(quotes_list)
weekday = now.weekday()


with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=mail_id, password=password)
    connection.sendmail(from_addr=mail_id, to_addrs="",
                        msg=f"Subject:{days_list[weekday]} Motivation\n\nGood Morning,\n\n"
                            f"Here's Your Quote For The Day:\n\n{quote}\n\n"
                            f"Have A Great Day!")

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=mail_id, password=password)
    connection.sendmail(from_addr=mail_id, to_addrs="",
                        msg=f"Subject:{days_list[weekday]} Motivation\n\nGood Morning Abdul,\n\n"
                            f"Here's Your Quote For The Day:\n\n{quote}\n\n"
                            f"Have A Great Day!")
