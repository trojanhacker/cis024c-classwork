import feedparser
from flask import Flask
from flask import render_template
from flask import request

# weather API key
api_key_weather  = "cb932829eacb6a0e9ee4f38bfbf112ed"
api_key_currency = "76335cb38ddc45feaab03af24cd9d7f7"

# currency API key
CURRENCY_URL="https://openexchangerates.org//api/latest.json?app_id=" + api_key_currency

#76335cb38ddc45feaab03af24cd9d7f7

import json
import urllib2
import urllib
def get_weather(query):
    api_url = "http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid="+api_key_weather

    query = urllib.quote(query)
    url = api_url.format(query)
    data = urllib2.urlopen(url).read()
    parsed = json.loads(data)
    weather = None
    if parsed.get("weather"):
        weather = {"description":parsed["weather"][0]["description"],
                   "temperature":parsed["main"]["temp"],
                   "city":parsed["name"],
                   'country':parsed['sys']['country']
                  }
    return weather

def get_rate(frm,to):
    all_currency=urllib2.urlopen(CURRENCY_URL).read()

    parsed=json.loads(all_currency).get('rates')
    frm_rate=parsed.get(frm.upper())
    to_rate=parsed.get(to.upper())
    return (to_rate/frm_rate,parsed.keys())


app = Flask(__name__)

RSS_FEEDS = {'bbc': 'http://feeds.bbci.co.uk/news/rss.xml',
             'techcrunch': 'http://feeds.feedburner.com/TechCrunch/startups'
			}

DEFAULTS = {'publication':'bbc',
            'city': 'London,UK',
            'currency_from':'GBP',
            'currency_to':'USD'
}

@app.route("/", methods=['GET', 'POST'])
def get_news():
        query = request.form.get("publication")
        if not query or query.lower() not in RSS_FEEDS:
                publication = DEFAULTS['publication']
        else:
                publication = query.lower()
        feed = feedparser.parse(RSS_FEEDS[publication])

        city=request.args.get('city')
        if not city:
            city=DEFAULTS['city']
        weather=get_weather(city)

        # get customized currency based on user input or default
        currency_from=request.args.get("currency_from")
        if not currency_from:
            currency_from=DEFAULTS['currency_from']
        currency_to=request.args.get("currency_to")
        if not currency_to:
            currency_to=DEFAULTS['currency_to']
        rate,currencies=get_rate(currency_from,currency_to)

        return render_template("home_all_currencies.html",articles=feed["entries"],weather=weather,
                               currency_from=currency_from,currency_to=currency_to,rate=rate,currencies=sorted(currencies))

if __name__ == "__main__":
    app.run(port=5000, debug=True)