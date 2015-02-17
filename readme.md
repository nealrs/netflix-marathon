My friends I were joking last night about how we liked to mainline entire seasons of TV via Netflix -- especially while in bed. The thing is, eventually you want snacks, (gummi bears, a fancy soda, maybe a pint of Cherry Garcia). But, you don't want to put on pants, switch apps, go outside, or order the same thing from Seamless  _again_.

Honestly, it's a big missed opportunity for Netflix. They could enable in-app purchasing & drive up revenue a bajillion percent. And in New York, Amazon Prize Now is a pretty great option for delivery. I bet Postmates would work really well too.

So I thought to myself, why not regularly monitor my online viewing activity to determine if I'm marathoning and trigger some helpful alerts / calls-to-action? Imagine getting this text:

![](https://github.com/nealrs/netflix-marathon/raw/master/screens/nflx2.png)

Note: my broheim [Devin Mancuso](http://www.devinmancuso.com/) and I have been trading browser automation hacks using Python / Selenium and Node/ phantomJS for the past couple weeks, and it's been super fun. If you haven't tried it, you're missing out.

## What works

1. Logging into Netflix account using Selenium & PhantomJS
2. Parsing activity history with BeautifulSoup
3. Checking if last 3 shows watched are from same series (marathon) and updating local tinyDB to avoid repeat triggers on same day.
4. Sending SMS / MMS via Twilio - when marathon conditions are met - with prompt & link to Amazon Prime Now for SNACK DELIVERY, (which is great for Manhattan / NYC)
5. Light [Twitter shaming](https://twitter.com/nealrs/status/567531566868742144)
6. Deployed to Digital Ocean & running every 10 minutes via cron.

  ![](https://github.com/nealrs/netflix-marathon/raw/master/screens/nflx1.png)

  _Console output case 1: new marathon detected (with MMS alert) and case 2: 'old' marathon detected / no alert sent_

## To do

1. Add front end for user registration & hide sensitive user data.
2. Deep links / API integrations for other apps & APIs 'marathon supplies' (Postmates / Seamless / Delivery.com / Amazon Prime now)

## Installation & usage

- First, install the dependencies (and yes, you _should_ really install homebrew)

```bash
pip install selenium tinydb twilio beautifulsoup4 python-twitter
brew install phantomjs
```

- Then, put your Netflix + Twilio login details & API keys into the `keys_ex.py` & rename it `keys.py`

- And finally, run the script

```bash
python nflx.py
```
