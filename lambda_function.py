import os
import requests
import random
from lib import create_message


line_token = os.environ['LINE_TOKEN']
Service_account_json_file = 'json_file.json'
calendarId = os.environ['CALENDARID']
            

def lambda_handler(event, context):
    message_data = {'message': create_message(Service_account_json_file, calendarId)}
    return_data = requests.post("https://notify-api.line.me/api/notify", headers={"Authorization": "Bearer %s" % line_token}, data=message_data)