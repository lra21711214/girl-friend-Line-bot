import random
from lib import Calendars

def create_message(Service_account_json_file, calendarId):
    calendar_message = []
    start_message = random.choice(['\nおはよ〜\n朝だよ。起きてる〜？？\n\n','\n朝だよ、起きて！！\n\n'])
    end_message = random.choice(['\n\n今日も1日頑張ってね。'])
    
    calendars = Calendars(Service_account_json_file, calendarId).get()
    if calendars:
        calendars_num = 0
        calendars_len = len(calendars) - 1
        for calendar in calendars:
            if 'OneDay' in calendar['time']:
                message_content = calendar['summary'] + 'が1日'
            else:
                message_content = calendar['summary'] + 'が' + calendar['time']['start'] + 'から' + calendar['time']['end'] + 'まで'
                
            if calendars_num == 0 and calendars_num != calendars_len:
                calendar_message.append('今日は、' + message_content)
            if calendars_num == 0 and calendars_num == calendars_len:
                calendar_message.append('今日は、' + message_content + 'あるみたいね。')
            elif calendars_num != 0 and calendars_num < calendars_len:
                calendar_message.append('と' + message_content)
            elif calendars_num == calendars_len:
                calendar_message.append('と' + message_content + 'あるみたいね。')
                
            calendars_num+=1
    else:
        calendar_message.append('今日は予定がないみたいね。')
    
    message = start_message + ''.join(calendar_message) + end_message
    return message