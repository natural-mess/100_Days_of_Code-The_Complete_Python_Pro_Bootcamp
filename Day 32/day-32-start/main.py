# import smtplib
# from email.message import EmailMessage
#
# gmail = ""
# yahoo_email = "lelocminhphuc@yahoo.com.vn"
# password_gmail = ""
# password_yahoo = "udwtyxgyarrmfyul"
# yahoo_mail_host = "smtp.mail.yahoo.com"
# gmail_host = "smtp.gmail.com"
#
# msg = EmailMessage()
# msg["Subject"] = "TestPython"
# msg["From"] = yahoo_email
# msg["To"] = "lelocminhduc@gmail.com"
# msg.set_content("Test python code")
#
# with smtplib.SMTP(host=yahoo_mail_host, port=587) as connection:
#     connection.ehlo()
#     connection.starttls()
#     connection.ehlo()
#     connection.login(user=yahoo_email, password=password_yahoo)
#     connection.send_message(msg)

import datetime as dt

now = dt.datetime.now()
year = now.year
month = now.month
day_of_week = now.weekday()
print(year)
print(now)

date_of_birth = dt.datetime(year= 1995, month=3, day=13)
print(date_of_birth)