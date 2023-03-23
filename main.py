import smtplib
my_email = "newemailjustforproject@gmail.com"
password = "atcbbgmbgwazjkje"

# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email,password=password)
#     connection.sendmail(from_addr=my_email,
#                         to_addrs="gauravcool.mishra365@gmail.com",
#                         msg= "Subject:Hello\n\n hello buddy you are doing great")
#     connection.close()
    #we can actually avoid this line of code just like open with
list1 = ["monday","tuesday","wednesday","thrusday","friday","saturday","sunday"]
import datetime as dt
import random
now =  dt.datetime.now()
day_of_the_week = now.weekday()

today = list1[day_of_the_week]


with open("quotes.txt","r") as datafiles:
    datafiles = list(datafiles)
    #or datafiles = datafiles.readlines()


x = random.choice(datafiles)
if today == "saturday":
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email,password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="gauravcool.mishra365@gmail.com",
                            msg= f"Subject:youBEtterREadThis\n\n{x} ")


