#!/usr/bin/env python

from pyquery import PyQuery as pq
from lxml import etree
import urllib
import urllib2
import time
import sys
import os

artist_name = sys.argv[1]
artist_url_name = urllib.quote(artist_name.decode(sys.stdin.encoding).encode('utf-8'))

def xiami():
    global artist_url_name
    xiami_artist_search_url = 'http://www.xiami.com/search/artist?key=' + artist_url_name
    try:
        search_result_object = pq(url=xiami_artist_search_url)
        artist_info_element = search_result_object('div.artistBlock_list div.artist_item100_block p.buddy a.artist100')
        artist_info_url = 'http://www.xiami.com' + artist_info_element.attr('href')
        artist_info_object = pq(url=artist_info_url)
        artist_picture_element = artist_info_object('a#cover_lightbox')
        artist_picture_url = artist_picture_element.attr('href').encode('utf-8', 'ignore')
        return artist_picture_url
    except Exception, e:
        raise

def ting():
    global artist_url_name
    ting_artist_search_url = 'http://ting.baidu.com/search?key=' + artist_url_name
    try:
        search_result_object = pq(url=ting_artist_search_url)
        artist_info_element = search_result_object('div#target_artist a.avatar')
        artist_info_url = 'http://ting.baidu.com' + artist_info_element.attr('href')
        artist_info_object = pq(url=artist_info_url)
        artist_picture_element = artist_info_object('div.mod-info-up img')
        artist_picture_url = artist_picture_element.attr('src').encode('utf-8', 'ignore')
        return artist_picture_url
    except Exception, e:
        raise

def main():
    try:
        picture_url = xiami()
    except Exception, e:
        try:
            picture_url = ting()
        except Exception, e:
            #xiami and ting can not worked, i can do nothing for this
            return -1
    print picture_url
if __name__ == '__main__':
    main()
