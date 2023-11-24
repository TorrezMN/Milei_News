import feedparser
from helpers.global_rss import global_feeds
from helpers.tools import pprint_data, get_file_tree, append_data,wait_random_time




def build_row(name,section,i):
    data = {
            'news_paper':name,                    
            'section':section,                                
            'title':i.get('title',''),                             
            'link':i.get('link',''),                            
            'summary':i.get('summary',''),                             
            'published':i.get('published',''),                    
            'tags':i.get('tags',''),
            'credit':i.get('credit',''),     
            }
    my_file = get_file_tree(name,section,'Argentina')
    print('Adding one.')
    append_data(str(my_file),data)



def parse_url(name,section, url):
    print('Parsing url: ',url)
    NewsFeed = feedparser.parse(url)
    print('\n'*5)
    print('\n'*5)
    print(dict(NewsFeed)['feed'])
    print('\n'*5)
#    for i in NewsFeed.entries:
#        print(i)
       # entrie = dict(i)
       # if('Milei' in entrie['title']):
       #     build_row(name,section,entrie) 
       #     break



if __name__ == "__main__":
    f = list(global_feeds.keys())
    for i in f:
         secciones = global_feeds[i].keys()
         wait_random_time()
         for j in secciones:
             url = global_feeds[i][j]
             parse_url(i,j,url)
    #         wait_random_time()
             break
         break



