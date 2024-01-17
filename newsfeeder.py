from pygooglenews import GoogleNews
import json
import time

gn = GoogleNews()
buisness =gn.topic_headlines('business')
tech =gn.topic_headlines('TECHNOLOGY')
entries = buisness["entries"]
articles = tech["entries"]
count = 0
for entry in articles:
  count = count+1
  print(
    str(count) + ". " + entry["title"] + entry["published"] +" URLS:"+entry["link"]
  )
  time.sleep(0.125)

for entry in entries:
  count = count+1
  print(
    str(count) + ". " + entry["title"] + entry["published"] +" URLS:"+entry["link"]
  )
  time.sleep(0.125)

