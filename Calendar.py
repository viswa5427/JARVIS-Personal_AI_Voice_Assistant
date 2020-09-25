import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
import datetime
from datetime import timedelta, datetime
from RespondListen import respond, listen
import pytz

SCOPES = ['https://www.googleapis.com/auth/calendar']
IST = pytz.timezone("Asia/Kolkata")

def calendar_service():
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    
    service = build('calendar', 'v3', credentials=creds)
    return service
    
def Get_Min_Max_times(now):
    Min = now
    date = now.date()
    Max = (datetime(date.year, date.month, date.day, 0)+timedelta(days = 2)).astimezone(IST)
    return Min.isoformat(), Max.isoformat()

def calendar_events():
    service = calendar_service()
    now = datetime.now(IST)
    timeMin, timeMax = Get_Min_Max_times(now)
    print('Getting the upcoming events')
    event_results = service.events().list(calendarId='primary', timeMin=timeMin, 
                                          timeMax=timeMax, maxResults=10, 
                                          singleEvents=True, orderBy='startTime').execute()
    events = event_results.get('items', [])
    if not events:
        respond("No upcoming events found.")
    for event in events:
        start_time = event['start'].get('dateTime')
        date_time = start_time.split("T")
        event_date = date_time[0]
        event_time = date_time[1].split("+")
        respond("{} class is at {} {}".format(event['summary'], event_time[0], event_date))
    return 


def get_event_date():
    try:
        respond("event Date")
        date_ = (listen()).split()
        date = int(date_[1][0:2])
        return date
    except:
        respond("Pardon me,please say that again")
        get_event_date()

def get_event_time():
    try:
        respond("event time")
        event_time = listen().split()
        hour = int(event_time[0][0:2])
        minute = int(event_time[0][-2:])
        if event_time[1][0] == "p":
            hour = hour + 12 
        return hour, minute
    except:
        respond("Pardon me,please say that again")
        get_event_time()

def get_event_duration():
    try:
        respond("event duration")
        event_duration = listen().split()
        event_duration = int(event_duration[0])
        return event_duration
    except:
        respond("Pardon me, please say that again")
        get_event_duration()

def create_event():
    service = calendar_service()
    respond("summary of the event")
    summary = listen()
    year = datetime.now().year
    month = datetime.now().month
    date = get_event_date()
    hour, minute = get_event_time()
    event_duration = get_event_duration()
    start_day = datetime(year, month, date, hour, minute)
    start = start_day.isoformat()
    end = (start_day + timedelta(hours = event_duration)).isoformat()

    event = {
        'summary': summary,
        'start': {
            'dateTime': start,
            'timeZone': 'Asia/Kolkata',
        },
        'end': {
            'dateTime': end,
            'timeZone': 'Asia/Kolkata',
        },
        'attendees' : [
            {'email' : 'kvn8501979409@gmail.com'}
        ]
    }
    event = service.events().insert(calendarId='primary', body=event).execute()
    respond("event created successfully")
    return
