# Database
from ast import For
from unicodedata import category
# from backend.dbhandler import dbHandler
# Web fetch and parse
import httplib2
from bs4 import BeautifulSoup
from googletrans import Translator  # query translate
# Function cache
import functools

#### GLOBAL VAR DB LANGUAGE ####
englishDB = False

class fetchUtil:
    @functools.lru_cache(maxsize=128) #function cache to massively speed up repeated translations
    def translateQuery(query, to):
        print("fetch: translating "+query)
        translator = translator = Translator()
        trans = translator.translate(query, dest=to)
        query = trans.text
        print("fetch: translated "+query)
        return query
    def translateQueries(query, to):
        print("fetch: translating "+str(query))
        translator = translator = Translator()
        trans = translator.translate(query, dest=to)
        queryt = []
        for t in trans:
            queryt.append(t.text)
        print("fetch: translated "+str(queryt))
        return queryt

    @functools.lru_cache(maxsize=32)
    def fetchURL(url):
        # print("fetch: fetching "+url)
        h = httplib2.Http()
        resp, content = h.request(url)
        assert resp.status == 200
        return content

    def try_or(fn, default):
        try:
            return fn()
        except:
            return default

class fetchFoodComposition:
    @functools.lru_cache(maxsize=8) # function cache to massively speed up repeated searches
    def fetchBySearch(query, pages=20):
        # note, pages is actually x10 items per page
        def fetchLinks(query, pages):
            def fetchOnePage(query, page):
                # Find web page
                url = "https://www.boohee.com/food/search?keyword="+query+"&page="+str(page)
                # Download HTML
                content = fetchUtil.fetchURL(url)
                # Parse HTML
                soup = BeautifulSoup(content, "html.parser")
                earr = soup.find('ul', class_='food-list').find_all('h4')
                larr = []
                for h4 in earr:
                    larr.append("https://www.boohee.com" + h4.find('a')["href"])
                return larr

            # translate query
            if englishDB:
                query = fetchUtil.translateQuery(query, 'zh-CN')
            links = []
            # fetch and extract links
            ppage = []
            for i in range(1, pages+1):
                print("fetch: fetching links "+str(i))
                page = fetchOnePage(query, i)
                # check for duplicate link / last page
                if i>1 and page == ppage:
                    print('fetch: fetching links END')
                    break
                else:
                    links += page
                ppage = page
                    
            return links

        def fetchItem(url):

            def createItemsfromHTML(soup, url):

                ####### parse info #######
                name = soup.find('h2', class_='crumb').contents[len(soup.find('h2', class_='crumb').contents)-1].string.replace(" ", "").replace("\n","").replace("/","")
                aliases = fetchUtil.try_or(lambda: sorted(set(soup.find('ul', class_='basic-infor').find('li').contents[1].split('、'))), "") # error wrapper as not all items have aliases
                category = fetchUtil.try_or(lambda: soup.find('ul', class_='basic-infor').find_all('li')[2].find('a').string, "") # error wrapper as not all items have category

                nut_infop = soup.find('div', class_='nutr-tag').find_all('dd')
                nut_info = {}
                for i in range(2, len(nut_infop)):
                    nut_info[nut_infop[i].find_all('span')[0].string.split('(')[0]] = float(nut_infop[i].find_all('span')[1].string.replace('一', '0')) # weird rare case where 一 shows instead of 0

                units = {}
                if len(soup.find_all('div', class_='widget-unit')) >= 1: # not all items have serving quantities
                    for i in range(1, len(soup.find('div', class_='widget-unit').find_all('tr'))-1):
                        ent = soup.find('div', class_='widget-unit').find_all('tr')[i].find_all('a')+soup.find('div', class_='widget-unit').find_all('tr')[i].find_all('span')
                        units[ent[0].string] = round(float(ent[1].string.replace("大卡",""))/nut_info["热量"], 2)*100 # take the amount of kcal in portion and divide by amount of kcal in 100g then *100 to get the portion g
                units['标准(100克)'] = 100.0

                images = fetchUtil.try_or(lambda: {
                    'thumb': soup.find('div', class_='food-pic').find('img')['src'],
                    'hd': soup.find('div', class_='food-pic').find('a')['href']
                    }, {'thumbnail': '', 'hd': ''})

                ###### translate info #######
                if englishDB:
                    name = fetchUtil.translateQuery(name, 'en')
                    if len(aliases)>=1:
                        print(aliases)
                        aliases = sorted(set(fetchUtil.translateQueries(aliases, 'en')))
                    if category != "":
                        category = fetchUtil.translateQuery(category, 'en')

                    tnut_info = {}
                    for key in nut_info:
                        tnut_info[fetchUtil.translateQuery(key, 'en').replace('heat', 'calories').lower()] = nut_info[key]
                    nut_info = tnut_info
                    del tnut_info

                    if len(units)>1:
                        tunits = {}
                        for key in units:
                            tunits[fetchUtil.translateQuery(key, 'en').replace('heat', 'calories').lower()] = units[key]
                        units = tunits
                        del tunits

                ####### add to array + aliasing #####
                items = [
                    {
                        'name': name,
                        'type': 'entry',
                        'url': url,
                        'category': category,
                        'nutrition': nut_info,
                        'units': units,
                        'image': images
                    }
                ]
                for alias in aliases:
                    items.append({
                        'name': alias,
                        'type': 'alias',
                        'pointer': name
                    })
                return items

            content = fetchUtil.fetchURL(url)
            soup = BeautifulSoup(content, "html.parser")
            items = createItemsfromHTML(soup, url)

            return items

        # fetch pages
        links = sorted(set(fetchLinks(query, pages))) # remove duplicates, as the page number above limit just returns last page.
        items = []
        for link in links:
            print("fetch: ["+str(links.index(link)+1)+"/"+str(len(links))+"] fetching "+link)
            items+=fetchItem(link) # add items
        
        return items

        # Add to database


import timeit
print(timeit.timeit('fetchFoodComposition.fetchBySearch("奶茶")', globals=globals(), number=1))
print(timeit.timeit('fetchFoodComposition.fetchBySearch("奶茶")', globals=globals(), number=1))
