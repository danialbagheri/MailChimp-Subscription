
import requests
import json

"""
This is a simple code to subscibe certain mailing list on Mailchimp. 
You can easilt adopt it to Django by changing the subscriber section

Written by: Danial Bagheri 
github.com/danialbagheri
"""
subscriber = raw_input("what's your email ")
# subscriber = "bagheri.danial@gmail.com"
# authorisation
api_key = '' # Your API key goes Here
list_id = '' # Your list ID goes Here
subdomain = '' # the letters after the dash in your api key. This is different for different account like US14
rooturl = "https://{}.api.mailchimp.com/3.0/".format(subdomain)
listurl = "lists/{}/members".format(list_id)


payload = {"type" : "string",
"email_address" : subscriber,
"status": "subscribed",
}
# Since we are making a simple html auth request, we only need the api and the username could be anything (anyuser) according to MailChimp API documents
mail = requests.post(rooturl+listurl, auth=('anyuser', api_key), data=json.dumps(payload))

# This checks if the subscriber is already a member of any list or if there is any error, you can render the result to any html file if you wish.
if mail.json()["status"] == 400:
	print mail.json()["title"]
else:
	print"You have been subscribed"


