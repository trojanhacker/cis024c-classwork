import feedparser
from flask import Flask
from flask import render_template

app = Flask(__name__)

RSS_FEEDS = {'bbc': 'http://feeds.bbci.co.uk/news/rss.xml',
             'techcrunch': 'http://feeds.feedburner.com/TechCrunch/startups'
			}

@app.route("/")
@app.route("/bbc")
def bbc():
    return get_news('bbc')

@app.route("/techcrunch")
def techcrunch():
    return get_news('techcrunch')

def get_news(publication="bbc"):
  feed = feedparser.parse(RSS_FEEDS[publication])
  first_article = feed['entries'][0]
  return render_template("home_dyn.html",title=first_article.get("title"),published=first_article.get("published"),summary=first_article.get("summary"))


if __name__ == "__main__":
  app.run(port=5000, debug=True)
