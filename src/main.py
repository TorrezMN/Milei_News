import feedparser
from helpers.base_rss import feeds


def parse_url(url):
    NewsFeed = feedparser.parse(url)
    #print('entries ->', NewsFeed.entries)
    for i in NewsFeed.entries:
        if ('Milei' in i.title):
            print(i.title)
            print('='*55)

if __name__ == "__main__":
    f = list(feeds.keys())
    k = list(feeds[f[0]].keys())
    url = feeds[f[0]][k[0]]
    parse_url(url)

