import requests
import datetime
import json
import schedule

def sendSOS(name:str,date:str):
	text = f"SOS!!!!! \n Slot available at {name} on {date}"
	texturl = "https://api.telegram.org/bot1784546021:AAF3zg8uosdf1-fCrZAbRLpfDi7S2shI1Vc/sendMessage?chat_id=-1001159439658&text={}".format(text)
	requests.get(texturl)
	return

def fetch(url):
	print("pinged the site!!")
	response = requests.get(url)
	status = json.loads(response.text)
	available = False

	for item in status['centers']:
		if item['name'].upper().find("BURARI")!=-1:
			for session in item['sessions']:
				if session['min_age_limit']==18 and session['available_capacity']>0:
					available=True
					sendSOS(item['name'],session['date'])
					print("found!!!!")
					schedule.clear('fetch')
					break
			if available:
				break
				


if __name__ == "__main__":
	base = datetime.datetime.today()
	district =141
	url = "https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id={}&date={}".format(district,base.strftime("%d-%m-%Y"))
	schedule.every(1).minutes.do(fetch,url=url).tag('fetch')

	while True:
		schedule.run_pending()