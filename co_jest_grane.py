import datetime
import pprint
import requests

from_date = datetime.datetime.today()
to_date = from_date + datetime.timedelta(days=30)

print(from_date)
print(to_date)

from_date_as_str = f'{from_date.strftime("%Y-%m-%d")}T00:00:00.000'
to_date_as_str = f'{to_date.strftime("%Y-%m-%d")}T00:00:00.000'
print(from_date_as_str)
print(to_date_as_str)

params = {
    'hasEnded': False,
    'no_earlier_than': from_date_as_str,
    'no_later_than': to_date_as_str
}

groups = ['hs3city', 'Toastmasters-in-Poznan']

events = []
for group in groups:
    r = requests.get(f'https://api.meetup.com/{group}/events', params=params)
    payload = r.json()

    print(f"Tyle mamy wydarzeń w grupie {group}:", len(payload))
    print(payload[0])

    events.extend(payload)

def event_date_time(event):
    return (event['local_date'], event['local_time'])

events.sort(key=lambda x: (x['local_date'], x['local_time']))

print('m00!')

print("{} | {} | {} | {} | {}".format("Nazwa".ljust(60), "Data".ljust(10), "Godzina", "Ile osób?", "Online?"))
print("".ljust(100, "-"))
for event in events:
    online_indicator = 'X'
    if event['is_online_event']:
        online_indicator = 'O'
    print("{} | {} | {} | {} | {}".format(event['name'].ljust(60), event['local_date'], event['local_time'].ljust(7), event['yes_rsvp_count'], online_indicator))
