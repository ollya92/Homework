#!/usr/bin/env python
import json
import logging
import requests
import cache_news
from dateutil.parser import parse
import os
from converter import convert_to_pdf, convert_to_html
from bs4 import BeautifulSoup
from args_parameters import ArgParser


logger = logging.getLogger("my_rss_reader")
arg_parser = ArgParser()
config = arg_parser.get_args()


class Reader:
    def __init__(self):
        self.config = config
        self.source = self.config.source
        self.news_result = []

    def get_content(self):
        """Get content"""
        if self.config.json:
            logger.info("JSON format")
        else:
            logger.info(f"Get content using a link")
        try:
            self.r = requests.get(self.source)
            soup = BeautifulSoup(self.r.content, 'xml')
            self.articles = soup.findAll('item')
            self.feed = soup.find('title').text
            self.news_title = ""
            self.news_source = f"The source is {self.feed}"
            self.news_link = ""
            self.news_pub_date = ""
            self.news_description = "Get more information using a link"
            for item in self.articles[:self.config.limit]:
                self.media = []
                if item.find('title'):
                    self.news_title = item.find('title').text
                if item.find('source'):
                    self.news_source = item.find('source').get('url')
                if item.find('link'):
                    self.news_link = item.find('link').text
                if item.find('pubDate'):
                    self.news_pub_date = item.find('pubDate').text
                if item.find('description'):
                    self.news_description = item.find('description').text
                if item.find('media:content'):
                    s = item.findAll('media:content')
                    for i in s:
                        if i.endswith(('.jpg', '.jpeg', '.bmp')):
                            self.media.append(i.get("url"))
                        else:
                            i = i + ".jpg"
                            self.media.append(i.get("url"))
                if item.find('enclosure'):
                    s = item.findAll('enclosure')
                    for i in s:
                        self.media.append(i.get("url"))
                self.news_result.append(
                    {
                        "Title": self.news_title,
                        "Description": self.news_description,
                        "Source": self.news_source,
                        "Link": self.news_link,
                        "Date": self.news_pub_date,
                        "Media": self.media,
                    }
                )
        except Exception as ex:
            logger.warning("Source is invalid")
            logger.exception(ex)
            raise ex

    def console(self, d: list, num: int):
        """Console representation"""
        self.data = d
        print(f"№{num + 1}")
        print(f"Title: {self.data[num]['Title']}\n"
                f"Description: {self.data[num]['Description']}\n"
                f"Source: {self.data[num]['Source']}\n"
                f"Link: {self.data[num]['Link']}\n"
                f"Date: {self.data[num]['Date']}\n"
                f"Media: {self.data[num]['Media']}\n")
        print(f"{'-' * 100}")

    def print(self):
        """Print news data"""
        logger.info(f"Get content from {self.feed}")
        print(f"\nFeed: {self.feed}\n\n")
        if self.config.limit and self.config.limit <= len(self.news_result):
            if self.config.json:
                self.json_mode()
            else:
                num = 0
                while num < self.config.limit:
                    self.console(self.news_result, num)
                    num += 1
        else:
            if self.config.json:
                self.json_mode()
            else:
                num = len(self.news_result)
                n = 0
                while n < num:
                    self.console(self.news_result, n)
                    n += 1
        logger.info(f"All needed news is printed")

    def json_mode(self):
        """Print data in JSON format"""
        if not self.config.date:
            self.json_data = json.dumps(self.news_result, indent=4, ensure_ascii=False)
            print(self.json_data)

    def verbose_mode(self):
        """Print a verbose status messages"""
        formatter = logging.Formatter('%(asctime)s  %(name)s  %(levelname)s: %(message)s')
        logger = logging.getLogger("rss-reader")
        logger.setLevel("DEBUG")
        s_handler = logging.StreamHandler()
        s_handler.setFormatter(formatter)
        logger.addHandler(s_handler)
        logger.info("Verbose mode")
        logger.debug(self.config)

    def start(self):
        """Start to get content and print results"""
        if self.config.verbose:
            self.verbose_mode()
        else:
            logger.addHandler(logging.NullHandler())
            logger.propagate = False
        if self.source:
            self.get_content()
            cache_news.read_inf(self.source)
        if self.config.date:
            logger.info(f"News for {self.config.date}")
            count = 0
            try:
                with open("cache.json", "r", encoding="utf-8") as f:
                    if os.path.getsize("cache.json") == 0:
                        print(f"Cache is empty")
                    else:
                        data = json.load(f)
                        for i in data.values():
                            for value in i:
                                dt = parse(value["Date"])
                                only_date = dt.date()
                                if str(only_date).replace("-", "") == self.config.date:
                                    if self.config.limit:
                                        if count < self.config.limit:
                                            print(f"{value}\n")
                                            count += 1
                                    else:
                                        print(f"{value}\n")
                                        count += 1
                            if count == 0:
                                print(f"There is no news {self.config.date}")
            except Exception as ex:
                logger.warning("File is invalid")
                logger.exception(ex)
                raise ex
        else:
            self.print()
        if self.config.to_pdf:
            convert_to_pdf()
        if self.config.to_html:
            convert_to_html()


def main():
    r = Reader()
    r.start()


if __name__ == "__main__":
    main()


