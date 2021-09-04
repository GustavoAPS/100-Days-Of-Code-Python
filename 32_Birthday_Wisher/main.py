import smtplib
import datetime as dt
import random


def generate_quote():
    with open("quotes.txt") as data:
        contents = data.read()
        my_quotes = contents.split('\n')
        return random.choice(my_quotes)


def send_email():
    my_email = "jamesbondmalevola@gmail.com"
    my_password = "codorna123"
    motivational_message = generate_quote()

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=my_password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="gugustavo137@gmail.com",
            msg=f"Subject:Remember\n\n{motivational_message}")
        connection.close()
        print("Email sent")


now = dt.datetime.now()

# if now.weekday() == 5:
send_email()
