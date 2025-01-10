import feedparser
from helpers.global_rss import global_feeds
from helpers.tools import pprint_data, get_file_tree, append_data, wait_random_time
import json


def build_row(name, section, entry):
    data = {
        "news_paper": name,
        "section": section,
        "title": entry.get("title", ""),
        "link": entry.get("link", ""),
        "summary": entry.get("summary", ""),
        "published": entry.get("published", ""),
        "tags": entry.get("tags", ""),
        "credit": entry.get("credit", ""),
    }
    my_file = get_file_tree(name, section, "World")
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
    print("=" * 55)
    print(f"SECTION: {section}")
    print(f"NAME: {name}")
    print("=" * 55)
    NewsFeed = feedparser.parse(url)
    entries = []
    for entry in NewsFeed.entries:
        if "Milei" in entry["title"]:
            entries.append(entry)
            break

    if entries:
        for entry in entries:
            try:
                build_row(name, section, entry)
            finally:
                wait_random_time()


if __name__ == "__main__":
    zonas = list(global_feeds.keys())
    for zona in zonas:
        if zona != "General":
            diarios = global_feeds[zona].keys()
            for diario in diarios:
                sections = global_feeds[zona][diario].keys()
                for section in sections:
                    url = global_feeds[zona][diario][section]
                    parse_url(diario, section, url)
        else:
            diarios = global_feeds[zona].keys()
            for diario in diarios:
                url = global_feeds[zona][diario]
                parse_url(diario, "random", url)
