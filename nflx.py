#!/usr/bin/python

import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
from keys import *
from twilio.rest import TwilioRestClient
from tinydb import TinyDB, where

def run():
  #let's log in
  print('> Logging in as: '+ username)
  b = webdriver.PhantomJS()
  b.get('https://www.netflix.com/Login?locale=en-US')
  b.find_element_by_id('email').send_keys(username)
  b.find_element_by_id('password').send_keys(password)
  b.implicitly_wait(3) # 3 seconds
  b.find_element_by_id('login-form-contBtn').click()
  b.implicitly_wait(6) # 6 seconds

  # confirm page title
  assert b.current_url == 'http://www.netflix.com/WiHome'
  print '> Logged in successfully'

  # get a list of TV series watched today
  b.get('https://www.netflix.com/WiViewingActivity')
  assert b.current_url == 'https://www.netflix.com/WiViewingActivity'
  print '> Getting recent activity'

  n = datetime.date.today()
  ds = '1/24/15' # fake flag for my account so I can trigger alert
  #ds = str(n.month) + "/" + str(n.day) + "/" + str(n.year)[2:]

  s = BeautifulSoup(b.page_source)
  a=[] # array for show titles
  for r in s.find_all('li', class_='retableRow'):
      t = r.find('span', class_='seriestitle', text=True)
      d = r.find('div', class_='col date nowrap', text=True)
      if t and d.text == ds:
          print '   date: ' + d.text + ', title: ' + t.text
          a.append(t.text)

  # If the last 3 episodes watched were from the same series -- it's probably a marathon -- oh and make sure we didn't already trigger an alert today for this  show.
  if a[0] == a[1] and a[0] == a[2] and not checkDB(ds, username, a[0]):

      #set flag in db
      updateDB(ds, username, a[0])

      # Notifications & triggers
      m = 'That\'s '+ str(a.count(a[0])) +' eps of '+ str(a[0])+ ' today! Want some snacks? Amazon can deliver within 60 min: goo.gl/vjLIAw'
      print "> "+ m

      # TWILIO SMS/MMS & OTHER HOOKS / ACTIONS
      smsMms(m)

  else:
      # whatever, we already triggered an alert for this marathon condition
      print '> Yeah yeah, you love ' + str(a[0]) + '.'

  b.quit()

def checkDB(date,user,show):
    db = TinyDB('db.json')
    t = db.table('log')
    r = t.search((where('date') == date) & (where('user') == user) & (where('show') == show))
    return r

def updateDB(date,user,show):
    db = TinyDB('db.json')
    t = db.table('log')
    t.insert({'date': date, 'user': user, 'show': show})
    #print t.all()

def smsMms(m):
    c = TwilioRestClient(sid, token)
    if url !='':
        print "> sending MMS"
        tw = c.messages.create(to=phone, from_=fnum, body=m, media_url=url)
    else:
        print "> sending SMS"
        tw = c.messages.create(to=phone, from_=fnum, body=m)


if __name__ == '__main__':
  run()
