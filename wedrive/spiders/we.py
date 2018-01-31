# -*- coding: utf-8 -*-
import scrapy
from urllib.parse import urljoin

## Funciones auxiliares
def get_body(response):
    return response.css('div[id=content]').extract_first()

def get_images(response):
    return response.css('div[id=content] img::attr(src)').extract()

def get_title(response):
    return response.css('title::text').extract_first()

def extract_links(response):
    return response.css('div[class=floatnone] a::attr(href)').extract()

def extract_links_menu(response):
    return response.css('div[id=ProjectNavPages] a::attr(href)').extract()

BASE = 'http://es.wikieducator.org/'

## Spider

class WeSpider(scrapy.Spider):
    name = 'we'
    allowed_domains = ['wikieducator.org']
    start_urls = ['http://es.wikieducator.org/Google_drive']
    urls_visitadas = []

    def parse(self, response):
        info = {}
        info['page'] = response.url
        info['images'] = get_images(response)
        info['title'] = get_title(response)
        info['html'] = get_body(response)
        yield info
        for e in extract_links(response):
            if e not in self.urls_visitadas and 'Archivo:' not in e:
                self.urls_visitadas.append(e)
                yield scrapy.Request(urljoin(BASE, e), callback = self.parse)
        for e in extract_links_menu(response):
            if e not in self.urls_visitadas:
                self.urls_visitadas.append(e)
                yield scrapy.Request(urljoin(BASE, e), callback = self.parse)



