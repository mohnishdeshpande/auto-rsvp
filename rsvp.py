import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# CONFIG Variables
RSVP_LIMIT = 5
CHROME_DRIVER = '/home/mohnish/Downloads/chromedriver_linux64/chromedriver'
groupIDs = ['melbourne-azure-nights', 'melbournewebmob', 'linux-users-of-victoria']
baseURL = 'https://www.meetup.com/'
with open('creds.txt', 'r') as f:
	username, password = f.readlines()
username=username[:-1]
password=password[:-1]


def login():
	# authenticate if not logged in, else pass
	try:
		driver.find_element(By.ID, 'login-link').click()
		driver.find_element(By.ID, 'email').send_keys(username)
		driver.find_element(By.ID, 'current-password').send_keys(password)
		driver.find_element(By.NAME, 'submitButton').click()
	except:
		pass


def RSVP():
	# RSVP for the event if not already, else pass
	try:
		driver.find_element(By.XPATH, "//button[text()[contains(., 'Attend')]]").click()
	except:
		pass

def unRSVP():
	# un-RSVP if already RSVP'ed, else pass
	try:
		driver.find_element(By.XPATH, "//button[text()[contains(., 'Edit RSVP')]]").click()
		driver.find_element(By.XPATH, "//button[text()[contains(., 'Not going')]]").click()
	except:
		pass


if __name__=='__main__':
	# keep the browser windows open after execution
	options = Options()
	options.add_experimental_option('detach', True)

	# webdriver for the configured browser and options
	driver = webdriver.Chrome(service=Service(CHROME_DRIVER), options=options)

	# homepage - meetup.com
	driver.get(baseURL)
	driver.maximize_window()

	# login and authenticate
	login()
	time.sleep(2)

	# for each group in configured groups [groudIDs]
	for groupID in groupIDs:
		# upcoming events page
		driver.get(baseURL+groupID+'/events')
		time.sleep(1)

		# get the hyperlinks for the all the upcoming events
		events = driver.find_elements(By.XPATH, "//ul[contains(@class, 'eventList-list')]//a[contains(@class, 'eventCard--link')]")
		events = [event.get_attribute('href') for event in events]

		# counter for RSVP_LIMIT
		cnt=1

		# for each event in upcoming events
		for event in events:
			# break, if crossing the limit
			# if cnt>RSVP_LIMIT:
			# 	break
			# cnt+=1

			# navigate to the event
			driver.get(event)
			time.sleep(2)

			# RSVP or un-RSVP for the event
			RSVP()
			# unRSVP()

	print('Successful!')