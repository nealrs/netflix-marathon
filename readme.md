# You marathoning bruh? (YMB)

Netflix marathons are very real --  especially sitting in bed, watching on your tablet. The point of YMB is to identify potential marathon sessions and (in the future) facilitate delivery of 'marathon supplies.'

Author: [Neal Shyam](http://nealshyam.com)  &middot; [@nealrs](http://twitter.com/nealrs)

## Complete

1. Log into Netflix account using Selenium & PhantomJS
2. Parse viewing activity with BeautifulSoup
3. Check if last 3 shows watched are from same series (marathon) and update local tinyDB to avoid repeat triggers on same day.
4. If marathon detected is, send SMS / MMS via Twilio with prompt & link to Amazon Prime Now for SNACK DELIVERY, (which is great for Manhattan / NYC).

## To do

1. Deep links / API integrations for other apps & APIs 'marathon supplies' (Postmates / Seamless / Delivery.com / Amazon Prime now)
2. Setup cron job that runs every 30 minutes to check marathon status.
3. Add frontend for user registration & hide sensitive user data.

## Requirements

Selenium, tinyDB, beautiful soup, phantomjs, and twilio keys & libs.

## Installation & Usage

Obviously this is unfinished, but:

1. Put your authorization / API keys into the keys_ex.py & rename is keys.py
2. run python nflx.py
