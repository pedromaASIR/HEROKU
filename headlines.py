# -*- coding: utf-8 -*-
from flask import Flask
import feedparser
from flask import render_template

app= Flask(__name__)

RSS_FEED = { 'bbc':'http://feeds.bbci.co.uk/news/rss.xml',
             'abc':'http://sevilla.abc.es/rss/feeds/Sevilla_Sevilla.xml',
             'elm':'http://estaticos.elmundo.es/elmundo/rss/portada.xml'
}
Titles = {'bbc':'BBC headlines',
          'abc':'ABC: Sevilla',
          'elm':'El Mundo'
}

articles = {}
articles['bbc'] = feedparser.parse(RSS_FEED['bbc'])['entries'][:5]
articles['abc'] = feedparser.parse(RSS_FEED['abc'])['entries'][:5]
articles['elm'] = feedparser.parse(RSS_FEED['elm'])['entries'][:5]

@app.route("/")
def get_news():
  return render_template("home.html", articles=articles,titles=Titles)

@app.route("/news/<journal>")
def get_one_journal(journal):
  if(journal not in articles):
     journal='elm'
  dict_articles = {}
  dict_titles = {}
  dict_articles[journal] = articles[journal]
  dict_titles[journal] = Titles[journal]
  return render_template("home.html", articles=dict_articles,titles=dict_titles)

if __name__ == '__main__':
  app.run(host="0.0.0.0",port=5300,debug=True)

