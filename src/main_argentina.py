
import json
import feedparser
from helpers.base_rss import feeds
from helpers.tools import pprint_data, get_file_tree, append_data, wait_random_time


def build_row(name, section, i):
    data = {
        "news_paper": name,
        "section": section,
        "title": i.get("title", ""),
        "link": i.get("link", ""),
        "summary": i.get("summary", ""),
        "published": i.get("published", ""),
        "tags": i.get("tags", ""),
        "credit": i.get("credit", ""),
    }
    my_file = get_file_tree(name, section, "Argentina")
    try:
        with open(my_file, "a") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
            print("------------------------------------ | Adding one.")
    except UnicodeEncodeError as e:
        print(f"Encoding error: {e}")
        pass
    except FileNotFoundError as e:
        print(f"File not found: {e}")
        pass


def parse_url(name, section, url):
    NewsFeed = feedparser.parse(url)
    for i in NewsFeed.entries:
        entrie = dict(i)
        if "Milei" in entrie["title"]:
            build_row(name, section, entrie)
            break


if __name__ == "__main__":
    f = list(feeds.keys())
    for i in f:
        secciones = feeds[i].keys()
        wait_random_time()
        for j in secciones:
            url = feeds[i][j]
            parse_url(i, j, url)
            wait_random_time()
