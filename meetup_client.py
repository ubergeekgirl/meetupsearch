import meetup.api
import datetime

client = meetup.api.Client()
client.api_key = 'YOUR_KEY_HERE'

event = client.GetEvent(id=238146759)
print("Name:", event.name)
t = datetime.datetime.fromtimestamp(event.time/1000)
try:
    d = event.duration
except:
    d = 2 * 60 * 60 * 1000
d = datetime.datetime.fromtimestamp((event.time+d)/1000)
print("Time:", t, "to", d)
print("Place: %s, %s, %s" % (event.venue['city'], event.venue['state'], event.venue['country']))
print("Description:")
print(event.description)
