import pywhatkit # pip install pywhatkit (windows)
try: 
    pywhatkit.sendwhatmsg("+91**********", "Sent via python OMG amazing", 16, 55) 
    print("Successfully Sent!") 
except: 
    print("An Unexpected Error!")

'''
Message is sent through whatsapp web so before
executing this code make sure you've logged in in your whatsapp web!

Phone Number is receiver
16 is 4PM written in 25 hr format
55 is minutes so 4:55 PM
In this way any time can be written
'''
# Pro tip:
# You can even enter your own number and message will be send to you yourself
# Isn't that amazing?