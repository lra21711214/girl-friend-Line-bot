import json
import datetime
import httplib2
from apiclient import discovery
import oauth2client
from oauth2client.service_account import ServiceAccountCredentials

class Calendars():
    def __init__(self, json_file, calendarId):
        self.calendarId = calendarId
        self.credentials = ServiceAccountCredentials.from_json_keyfile_name(json_file, 'https://www.googleapis.com/auth/calendar')
        self.start_time = datetime.datetime.now(datetime.timezone(datetime.timedelta(hours=9)))
        self.end_time = self.start_time.replace(hour=23, minute=59, second=59)
        
    def request(self):
        http = self.credentials.authorize(httplib2.Http())
        service = discovery.build('calendar', 'v3', http=http)
        events = service.events().list(
            calendarId=self.calendarId, 
            timeMin=self.start_time.isoformat(), 
            timeMax=self.end_time.isoformat(), 
            singleEvents=True, 
            orderBy='startTime'
        ).execute()
        
        return events['items']
        
    def get(self):
        calendar_list = []
        calendars = self.request()
        for calendar in calendars:
            if "summary" in calendar:
                summary = calendar['summary']
            else:
                summary = "未記入の予定"
    

            if "dateTime" in calendar['start']:
                start_time = datetime.datetime.strptime(calendar['start']['dateTime'], '%Y-%m-%dT%H:%M:%S+09:00')
                end_time = datetime.datetime.strptime(calendar['end']['dateTime'], '%Y-%m-%dT%H:%M:%S+09:00')
                
                show_start_time = str(start_time.hour) + '時' + str(start_time.minute) + '分'
                show_end_time = str(end_time.hour) + '時' + str(end_time.minute) + '分'
                
                time = {'start' : show_start_time, 'end' : show_end_time}
            elif "date" in calendar['start']:
                time = "OneDay"

            calendar_list.append({'summary' : summary, 'time' : time})
        return calendar_list