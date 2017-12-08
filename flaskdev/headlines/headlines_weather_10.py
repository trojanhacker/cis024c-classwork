import feedparser
from flask import Flask
from flask import render_template
from flask import request

api_key = "cb932829eacb6a0e9ee4f38bfbf112ed"

import json
import urllib2
import urllib
def get_weather(query):
    api_url = "http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid="+api_key
    print "api_url:",api_url

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


app = Flask(__name__)

RSS_FEEDS = {'bbc': 'http://feeds.bbci.co.uk/news/rss.xml',
             'techcrunch': 'http://feeds.feedburner.com/TechCrunch/startups'
			}

@app.route("/", methods=['GET', 'POST'])
def get_news():
        query = request.form.get("publication")
        if not query or query.lower() not in RSS_FEEDS:
                publication = "bbc"
        else:
                publication = query.lower()
        feed = feedparser.parse(RSS_FEEDS[publication])
        weather=get_weather("San Jose,US")
        return render_template("home_weather.html",articles=feed["entries"],weather=weather)

if __name__ == "__main__":
    app.run(port=5000, debug=True)