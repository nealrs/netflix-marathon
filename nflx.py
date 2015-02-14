'''
# You marathoning bruh? (YMB)

Netflix marathons are very real --  especially sitting in bed, watching on your tablet. The point of YMB is to identify potential marathon sessions and (in the future) facilitate delivery of 'marathon supplies.'

Author: Neal Shyam  | @nealrs | nealshyam.com

## Working

  1. Log into Netflix account using Selenium & PhantomJS
  2. Parse viewing activity with BeautifulSoup
  3. Sends MMS via Twilio if last 3 shows watched are from the same series (marathon danger zone)

## To do

  1. Hook up a delivery API (Postmates / Seamless / Delivery.com) to order marathon supplies (a pint of Cherry Garcia / dinner / booze)
  2. Setup cron job that runs every 30 minutes & tracks past alerts -- so you only get alerted once/day about marathoning a show
  3. Make it look better & handle user data better.

## Requirements

Selenium, beautiful soup, phantomjs, and twilio keys & libs.

## Installation & Usage

    Obviously this is unfinished, but:

    1. Put your authorization / API keys into the keys_ex.py & rename is keys.py
    2. run python nflx.py

'''

import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
from keys import *
from twilio.rest import TwilioRestClient

def run():
  #let's log in
  print('Logging in as: '+ username)
  b = webdriver.PhantomJS()
  b.set_window_size(1280, 768)
  b.get('https://www.netflix.com/Login?locale=en-US')
  b.find_element_by_id('email').send_keys(username)
  b.find_element_by_id('password').send_keys(password)
  b.implicitly_wait(3) # 3 seconds
  b.find_element_by_id('login-form-contBtn').click()
  b.implicitly_wait(6) # 6 seconds

  # confirm page title
  assert b.current_url == 'http://www.netflix.com/WiHome'
  print 'Logged in successfully'

  # get a list of TV series watched today
  b.get('https://www.netflix.com/WiViewingActivity')
  assert b.current_url == 'https://www.netflix.com/WiViewingActivity'
  print 'Getting recent activity'

  n = datetime.date.today()
  #ds = str(n.month) + "/" + str(n.day) + "/" + str(n.year)[2:]
  ds = '1/24/15' # fake flag for my account so I can trigger alert

  s = BeautifulSoup(b.page_source)
  a=[]
  for r in s.find_all('li', class_='retableRow'):
      t = r.find('span', class_='seriestitle', text=True)
      d = r.find('div', class_='col date nowrap', text=True)
      if t and d.text == ds:
          print 'date:', d.text, ', title:', t.text
          a.append(t.text)

  # If the last 3 episodes watched were from the same series -- it's probably a marathon
  if a[0] == a[1] and a[1] == a[2]:

      msg = 'That\'s '+ str(a.count(a[0])) +' episodes of '+ str(a[0])+ ' today -- you marathoning bruh?'
      print msg

      # and yes, yes we are sending a gif to the recipient.
      c = TwilioRestClient(sid, token)
      if url !='':
          m = c.messages.create(to=phone, from_=fnum, body=msg, media_url=url)
      else:
          m = c.messages.create(to=phone, from_=fnum, body=msg)

      # trigger delivery here
      # set flag here to suppress future show X alerts for today


  b.quit()

if __name__ == '__main__':
  run()
