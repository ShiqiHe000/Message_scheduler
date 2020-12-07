from twilio_credentials import account_sid, auth_token, twilio_num, cellphone
from lyric import morning_lyrics
from twilio.rest import Client
import schedule
import random
import time


# Sent preset messages using API send message (the API is offered by Twilio) ---------------
# Your Account Sid and Auth Token from twilio.com/console
def send_message(morning_message_list = morning_lyrics):
    client = Client(account_sid, auth_token)
    message_id = random.randint(0, len(morning_lyrics))
    message = client.messages.create(
                         body=morning_message_list[message_id],
                         from_=twilio_num,
                         to=cellphone
                     )
# ---------------------------------------------------------------------------------------------

# Use library that can schedule text to be sent at certain time.
schedule.every().day.at("07:00").do(send_message)

while True:
    schedule.run_pending()
    time.sleep(1)

#send_message(morning_messages[1])
