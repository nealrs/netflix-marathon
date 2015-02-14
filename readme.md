# You marathoning bruh? (YMB)

Netflix marathons are very real --  especially sitting in bed, watching on your tablet. The point of YMB is to identify potential marathon sessions and (in the future) facilitate delivery of 'marathon supplies.'

Author: [Neal Shyam](http://nealshyam.com)  &middot; [@nealrs](http://twitter.com/nealrs) 

## Complete

1. Log into Netflix account using Selenium & PhantomJS
2. Parse viewing activity with BeautifulSoup
3. Send SMS / MMS via Twilio if last 3 shows watched are from the same series (marathon danger zone)

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