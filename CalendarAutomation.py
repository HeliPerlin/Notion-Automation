from __future__ import print_function
import datetime
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request


class CalendarAutomation:
    # TODO: token.pickle and credentials.json are individual per user.
    #  they should be given as arguments in the constructor, but be

    def __init__(self):
        scopes = ['https://www.googleapis.com/auth/calendar.readonly']
        self.creds = None

        if os.path.exists('token.pickle'):
            with open('token.pickle', 'rb') as token:
                creds = pickle.load(token)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials.json', scopes)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open('token.pickle', 'wb') as token:
                pickle.dump(creds, token)
        # service is a Resource object that represents a calendar
        service = build('calendar', 'v3', credentials=creds)

        now = datetime.datetime.utcnow().isoformat() + 'Z'
        events_result = service.events().list(calendarId='primary', timeMin=now
                                              , maxResults=10,
                                              singleEvents=True,
                                              orderBy='startTime').execute()
        self.events = events_result.get('items', [])

    def get_events(self):
        return self.events
