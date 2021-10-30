from functools import lru_cache
import logging
import json
import requests
from bs4 import BeautifulSoup

cache = {}

logger = logging.getLogger("my_rss_reader")


def get_inf(source):
    """Get content into the cache"""
    responce = requests.get(source)
    soup = BeautifulSoup(responce.content, 'xml')
    articles = soup.findAll('item')
    news_title = ""
    news_source = "See source using a link "
    news_link = ""
    news_pub_date = ""
    news_description = "Get more information using a link"
    news_content = []
    for item in articles:
        media = []
        if item.find('title'):
            news_title = item.find('title').text
        if item.find('source'):
            news_source = item.find('source').get('url')
        if item.find('link'):
            news_link = item.find('link').text
        if item.find('pubDate'):
            news_pub_date = item.find('pubDate').text
        if item.find('description'):
            news_description = item.find('description').text
        if item.find('media:content'):
            s = item.findAll('media:content')
            for i in s:
                media.append(i.get("url"))
        if item.find('enclosure'):
            s = item.findAll('enclosure')
            for i in s:
                media.append(i.get("url"))

        news_content.append(
            {
                "Title": news_title,
                "Description": news_description,
                "Source": news_source,
                "Link": news_link,
                "Date": news_pub_date,
                "Media": media,
            }
        )

    return news_content


@lru_cache()
def read_inf(source):
    """Write information into cache and save it in json-file"""
    if source not in cache:
        cache[source] = get_inf(source)
        try:
            with open("cache.json", "w", encoding="utf-8") as file:
                file.write(json.dumps(cache, indent=4, ensure_ascii=False))
        except Exception as ex:
            logger.warning("File is invalid")
            logger.exception(ex)
            raise ex
    return cache[source]
