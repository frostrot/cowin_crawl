import requests
import datetime
import json
import telegram_send

def sendSOS(name:str,date:str):
	telegram_send.send(messages=[f"SOS!!!!! \n Slot available at {name} on {date}"])
	return

def fetch(url):
	print("pinged the site!!")
	response = requests.get(url)
	status = json.loads(response.text)
	available = False

	for item in status['centers']:
		if item['name'].upper().find("BURARI")!=-1:
			for session in item['sessions']:
				if session['min_age_limit']==45 and session['available_capacity']>0:
					available=True
					sendSOS(item['name'],session['date'])
					print("found!!!!")
					break
			if available:
				break
				


if __name__ == "__main__":
	base = datetime.datetime.today()
	district =141
	url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id={}&date={}".format(district,base.strftime("%d-%m-%Y"))
	fetch(url)