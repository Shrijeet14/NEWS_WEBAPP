import requests
from send_mail import send_message

api_key="894a70f412c540c78ccc07bcfa7cf860"

url="https://newsapi.org/v2/top-headlines?country=in&apiKey=894a70f412c540c78ccc07bcfa7cf860"

request = requests.get(url)

content= request.json()

message_content=""

for index , article in enumerate(content["articles"]):   
    if article["title"] is  not None:
        if article["description"] is  not None:
            message_content=message_content + f'{index+1}) {article["title"]}\n{article["description"]}\n{article["url"]}\n\n'

message=f'''\
Subject : NEWS TODAY
{message_content}
'''
message= message.encode("utf-8")

file=open("subscribers.txt","r")
email_addresses=file.readlines()

for email_address in email_addresses:
    send_message(message,email_address)

file.close()
