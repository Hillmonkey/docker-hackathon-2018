#!/usr/bin/python3

import contacts
import time
from twilio.rest import Client

def hammer_sms(s, to, from_="+14158773164"):
    """notice proper formatting of US phone numbers
    """

    # Account SID from twilio.com/console
	account_sid = os.environ['TWILIO_ID']
    # Auth Token from twilio.com/console
	auth_token = os.environ['TWILIO_SECRET']
    client = Client(account_sid, auth_token)

    for word in s.split():    
        message = client.messages.create(
            to=to, 
            from_=from_,
            body=word)
        print(message.sid)
        time.sleep(3)

def multi_hammer(s, contact_dict, from_="+14158773164"):
    """notice proper formatting of US phone numbers
    """

    # Account SID from twilio.com/console
	account_sid = os.environ['TWILIO_ID']
    # Auth Token from twilio.com/console
	auth_token = os.environ['TWILIO_SECRET']
    client = Client(account_sid, auth_token)

    for word in s.split():
        for key in contact_dict:    
            message = client.messages.create(
                to=contact_dict[key], 
                from_=from_,
                body=word)
            print(message.sid)
        time.sleep(3)

if __name__ == "__main__":
    to="+14154818386"
    # hammer_sms("getting so crazy at holberton right now", to)
    multi_hammer("getting so crazy at holberton right now", contacts.d)
    
