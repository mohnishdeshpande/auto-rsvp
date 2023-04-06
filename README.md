Author: Mohnish Deshpande

Name  : Meetup Auto-RSVP

Install python packages
  $ pip install -r requirements.txt

Run Auto-RSVP script
  $ python rsvp.py

Note:

- Make sure to configure all the Global variables.
  [Globals are used for the ease of testing]

- Credentials go in 'creds.txt'
  Username on 1st line
  Password on 2nd line
  
- As the program is designed to run once every hour,
  You can set the book upcoming events limit to 5, to save time.
  - Uncomment lines 77, 78, 79
  From my experience, some groups have upcoming events scheduled for next several years.

- The script also contains a counter method to RSVP() - unRSVP()
  It can be used to un-RSVP from all the RSVP'ed events
  - Comment out line 87, Uncomment line 88
