import smtplib, ssl
import random

otp = "".join([str(random.randint(0,9)) for i in range(4)])
port = 465
smtp_server = 'smtp.gmail.com'
sender_email = 'demobot86@gmail.com'
password = 'yskncchmyioqotdj'
user_name = input('Enter the account User_name: ')
reciver_email = input('Reciver Email: ')
message = f'''
Hey {user_name} this is your Python Verification code {otp}
'''

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, reciver_email, f'Subject: Python Verification Code \n\n\n {message}')

verify = input('Enter Your Verification code: ')
if verify == otp:
    print('\nYour Accound Has Been Successfully Created.')
else:
    print('You Have Entered Wrong Verification Code.')