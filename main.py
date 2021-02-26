from NotionAutomation import NotionAutomation
from CalendarAutomation import CalendarAutomation
import sys

if __name__ == '__main__':
    if len(sys.argv) != 3:
        exit(-1)
    calendar_object = CalendarAutomation()
    # first arg is users url, second arg is databases url
    notion_object = NotionAutomation(sys.argv[1], sys.argv[2])

    for event in calendar_object.get_events():
        event_description = event['summary']
        # event_time = event
        notion_object.add_row(event_description)

