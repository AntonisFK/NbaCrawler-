# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BasketballItem(scrapy.Item):
    title = scrapy.Field()
    Season = scrapy.Field()
    Age = scrapy.Field()
    Tm = scrapy.Field()
    Lg = scrapy.Field()
    Pos = scrapy.Field()
    G = scrapy.Field()
    GS = scrapy.Field()
    MP = scrapy.Field()
    FG = scrapy.Field()
    FGA = scrapy.Field()
    FGP = scrapy.Field()
    ThreeP = scrapy.Field()
    ThreePA = scrapy.Field()
    Threepp = scrapy.Field()
    TwoP = scrapy.Field()
    TWOPA = scrapy.Field()
    TWOP = scrapy.Field()
    FT = scrapy.Field()
    FTA = scrapy.Field()
    FTP = scrapy.Field()
    ORB = scrapy.Field()
    DRB = scrapy.Field()
    TRB = scrapy.Field()
    AST = scrapy.Field()
    BLK = scrapy.Field()
    TOV = scrapy.Field()
    PF = scrapy.Field()
    PTS = scrapy.Field()
    pass
