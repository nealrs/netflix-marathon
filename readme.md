# You marathoning bruh? (YMB)

My friends I were joking last night about how we liked to mainline entire seasons of TV via Netflix -- especially while in bed. The problem is, eventually you need snacks, (gummi bears, a fancy soda, maybe a pint of Cherry Garcia). But, you don't want to get out of bed, switch apps, go outside, or order the same thing from Seamless  _again_. 

Honestly, it's a pretty big missed opportunity for Netflix. They could enable in-app purchasing & drive up revenue a bajillion percent. And in New York, Amazon Prize Now is a pretty great option for delivery. I bet Postmates would work really well too.

So I thought to myself, why not use my online viewing activity to determine if I'm marathoning and trigger some helpful alerts / calls-to-action? Imagine getting this text: 

> You've watch 4 eps of Arrested Development today. How about some gummy bears and a soda? Amazon can get there in less than 60 mins!

## Complete

1. Log into Netflix account using Selenium & PhantomJS
2. Parse viewing activity with BeautifulSoup
3. Check if last 3 shows watched are from same series (marathon) and update local tinyDB to avoid repeat triggers on same day.
4. If marathon is detected, send SMS / MMS via Twilio with prompt & link to Amazon Prime Now for SNACK DELIVERY, (which is great for Manhattan / NYC)

  ![](screens/nflx1.png)

  _Console output case 1: new marathon detected (with MMS alert) and Case 2: 'old' marathon detected / no alert sent_

  ![](screens/nflx2.png)

  _Example of MMS alert with animated GIF (doesn't work on Nexus 5) + link to Amazon Prime Now_

## To do

1. Deep links / API integrations for other apps & APIs 'marathon supplies' (Postmates / Seamless / Delivery.com / Amazon Prime now)
2. Setup cron job that runs every 30 minutes to check marathon status.
3. Add frontend for user registration & hide sensitive user data.

## Installation & Usage

- First, install the dependencies

```bash
pip install selenium tinydb twilio beautifulsoup4
brew install node
curl https://www.npmjs.org/install.sh | sh
npm install phantomjs
```

- Then, put your Netflix + Twilio login details & API keys into the `keys_ex.py` & rename it `keys.py`

- Uncomment this line in `nflx.py`

```python
ds = str(n.month) + "/" + str(n.day) + "/" + str(n.year)[2:]
```

- And finally, run the script 

```bash
python nflx.py
```