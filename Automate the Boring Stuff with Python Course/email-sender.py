import smtplib
import time

connection = smtplib.SMTP('smtp.gmail.com', 587)

print("Starting communication with SMTP server...")
time.sleep(5)
connection.ehlo()

print("Starting TLS encryption...")
time.sleep(5)
connection.starttls()

print("Logging in...")
time.sleep(5)
connection.login('maguswyvern@gmail.com', 'rboizfpamhwgqmob')

connection.sendmail('maguswyvern@gmail.com', 'maguswyvern@gmail.com', 'Subject: Test\n\nThis is a test message.')

print("Closing connection...")
connection.quit()