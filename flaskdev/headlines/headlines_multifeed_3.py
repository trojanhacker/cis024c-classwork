import feedparser
from flask import Flask

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

def get_news(publication):
  feed = feedparser.parse(RSS_FEEDS[publication])
  first_article = feed['entries'][0]
  return """<html>
    <body>
        <h1>Headlines </h1>
        <b>{0}</b> </ br>
        <i>{1}</i> </ br>
        <p>{2}</p> </ br>
    </body>
</html>""".format(first_article.get("title"), first_article.get("published"), first_article.get("summary"))


if __name__ == "__main__":
  app.run(port=5000, debug=True)
