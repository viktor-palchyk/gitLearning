import time
from datetime import datetime as dt

hosts_temp="hosts"
hosts_path="etc/hosts"
redirect_to='127.0.0.1'
websites_list=['www.facebook.com', 'facebook.com', 'gmail.com', 'www.gmail.com', 'pravda.com.ua']

while True:
	if dt(dt.now().year, dt.now().month, dt.now().day,8) < dt.now() < dt(dt.now().year, dt.now().month, dt.now().day,18):
	 	print("Working hours...")
	 	with open(hosts_temp, 'r+') as file:
	 		content=file.read()
	 		for website in websites_list:
	 			if website in content:
	 				pass
	 			else:
	 				file.write(redirect_to + " "+website + "\n")
	else:
		with open(hosts_temp, 'r+') as file:
			content=file.readlines()
			file.seek(0)
			for line in content:
				if not any(website in line for website in websites_list):
					file.write(line)
			file.truncate()
		print("Fun hours...")
	time.sleep(5)
