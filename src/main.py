import feedparser
from helpers.base_rss import feeds



def build_row(i):
    data = {
            'news_paper':'',
            'section':'',

            }




def parse_url(name,section, url):
   # NewsFeed = feedparser.parse(url)
    print('DIARIO ', name)
    print('SECCION ', section)
    print('URL ', url)
   # for i in NewsFeed.entries:
   #     build_row(dict(i))



if __name__ == "__main__":
    f = list(feeds.keys())
    for i in f:
        secciones = feeds[i].keys()
        for j in secciones:
            url = feeds[i][j]
            parse_url(i,j,url)
            break



