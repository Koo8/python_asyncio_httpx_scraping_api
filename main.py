import asyncio
import time
import httpx
import requests

""" Scraping multiple URLs : using sync and async to compare performance time """
""" Example for using asyncio + httpx """

async def fetch():
    urls = [
        "https://books.toscrape.com/catalogue/category/books/default_15/page-1.html",
        "https://books.toscrape.com/catalogue/category/books/default_15/page-2.html",
        "https://books.toscrape.com/catalogue/category/books/default_15/page-3.html",
        "https://books.toscrape.com/catalogue/category/books/default_15/page-4.html",
        "https://books.toscrape.com/catalogue/category/books/default_15/page-5.html",
        "https://books.toscrape.com/catalogue/category/books/default_15/page-6.html",
        "https://books.toscrape.com/catalogue/category/books/default_15/page-7.html",
        "https://books.toscrape.com/catalogue/category/books/default_15/page-8.html",
    ]
    # 1: using requests synchronously - when run this method, remove 'async' from fetch()
    # re = [requests.get(url).text[:100] for url in urls]

    # 2: use asyncio and httpx - note: add 'async' for fetch() function
    # AsyncClient() is a context manager, its get() return coroutine object that can be consumed by asyncio.gather
    async with httpx.AsyncClient() as client:
        co_routine = [client.get(url) for url in urls] # client.get() return coroutine object

        re = [res_ponse.text[:100] for res_ponse in await asyncio.gather(*co_routine)] #Coroutines will be wrapped in a future and scheduled in the event loop. 

    print(re)

def main():
    start = time.perf_counter()
    # when use requests without asyncio
    # fetch()

    # when use https with asyncio
    asyncio.run(fetch())
    end = time.perf_counter()

    print(f'time used : {end-start}') 

""" Time used with requests.get() syncrnously : 
['\n\n<!DOCTYPE html>\n<!--[if lt IE 7]>      <html lang="en-us" class="no-js lt-ie9 lt-ie8 lt-ie7"> <![e', '\n\n<!DOCTYPE html>\n<!--[if lt IE 7]>      <html lang="en-us" class="no-js lt-ie9 lt-ie8 lt-ie7"> <![e', '\n\n<!DOCTYPE html>\n<!--[if lt IE 7]>      <html lang="en-us" class="no-js lt-ie9 lt-ie8 lt-ie7"> <![e', '\n\n<!DOCTYPE html>\n<!--[if lt IE 7]>      <html lang="en-us" class="no-js lt-ie9 lt-ie8 lt-ie7"> <![e', '\n\n<!DOCTYPE html>\n<!--[if lt IE 7]>      <html lang="en-us" class="no-js lt-ie9 lt-ie8 lt-ie7"> <![e', '\n\n<!DOCTYPE html>\n<!--[if lt IE 7]>      <html lang="en-us" class="no-js lt-ie9 lt-ie8 lt-ie7"> <![e', '\n\n<!DOCTYPE html>\n<!--[if lt IE 7]>      <html lang="en-us" class="no-js lt-ie9 lt-ie8 lt-ie7"> <![e', '\n\n<!DOCTYPE html>\n<!--[if lt IE 7]>      <html lang="en-us" class="no-js lt-ie9 lt-ie8 lt-ie7"> <![e']
time used : 2.4624923000001218
""" 

""" Time used with asyncio + httpx 
['\n\n<!DOCTYPE html>\n<!--[if lt IE 7]>      <html lang="en-us" class="no-js lt-ie9 lt-ie8 lt-ie7"> <![e', '\n\n<!DOCTYPE html>\n<!--[if lt IE 7]>      <html lang="en-us" class="no-js lt-ie9 lt-ie8 lt-ie7"> <![e', '\n\n<!DOCTYPE html>\n<!--[if lt IE 7]>      <html lang="en-us" class="no-js lt-ie9 lt-ie8 lt-ie7"> <![e', '\n\n<!DOCTYPE html>\n<!--[if lt IE 7]>      <html lang="en-us" class="no-js lt-ie9 lt-ie8 lt-ie7"> <![e', '\n\n<!DOCTYPE html>\n<!--[if lt IE 7]>      <html lang="en-us" class="no-js lt-ie9 lt-ie8 lt-ie7"> <![e', '\n\n<!DOCTYPE html>\n<!--[if lt IE 7]>      <html lang="en-us" class="no-js lt-ie9 lt-ie8 lt-ie7"> <![e', '\n\n<!DOCTYPE html>\n<!--[if lt IE 7]>      <html lang="en-us" class="no-js lt-ie9 lt-ie8 lt-ie7"> <![e', '\n\n<!DOCTYPE html>\n<!--[if lt IE 7]>      <html lang="en-us" class="no-js lt-ie9 lt-ie8 lt-ie7"> <![e']
time used : 0.3473322999998345
"""



if __name__ == "__main__":
    main()