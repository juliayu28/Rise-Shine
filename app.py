from twilio.rest import Client
import requests
from bs4 import BeautifulSoup
import random
import schedule
import time

searchTerms = ["dog", "cat", "kitty", "corgi-puppy", "samoyed-puppy", "husky-puppy"]
searchTerm = random.choice(searchTerms)
searchUrl = "https://unsplash.com/s/photos/{}".format(searchTerm)
soup = BeautifulSoup(requests.get(searchUrl).text, "html.parser")

img_urls = []
for img in soup.find_all("img"):
	link = img.get("src")
	width = img.get("width")
	if link and link[:33] == "https://images.unsplash.com/photo":
		img_urls.append(link)

# Real account_sid and auth_token omitted for public Github posting
account_sid = "exampleAccountSid"
auth_token = "exampleAuthToken"

client = Client(account_sid, auth_token)

# Real phone number and Twilio number omitted for public Github posting
def job():
	client.messages.create(
		to = "+11234567890",
		from_ = "+11234567890",
		body = "Rise and shine! Here's a cute animal photo to kickstart your day!",
		media_url = random.choice(img_urls))

schedule.every().day.at("9:00").do(job)

while True:
	schedule.run_pending()
	time.sleep(1)