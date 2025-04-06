# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:

            if item.quality < 50:
                if item.name == "Aged Brie":
                    self.__handle_aged_brie(item)

                elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                    self.__handle_backstage(item)
            
                elif item.name == "Sulfuras, Hand of Ragnaros":
                    self.__handle_sulfuras(item)
                
                elif item.name == "Conjured Mana Cake":
                    if item.quality > 0:
                        self.__handle_conjured(item)
                
                elif item.quality != 0:
                    item.quality -= 1
                    if item.sell_in < 0 and item.quality > 0:
                        item.quality -= 1
        
                item.sell_in -= 1

    def __handle_aged_brie(self, item):
        item.quality += 1
        
    def __handle_backstage(self, item):
        
        item.quality += 1

        if item.quality < 50:
            if item.sell_in < 11:
                item.quality += 1
            
            if item.sell_in < 6:
                item.quality += 1
        
        if item.sell_in < 0:
            item.quality = 0

    def __handle_sulfuras(self, item):
        item.sell_in = 0
        return
        
    def __handle_conjured(self, item):
        item.quality -= 1

        if item.quality > 0:
            item.quality -= 1

        if item.sell_in < 0 and item.quality - 1 > 0:
            item.quality -= 2

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
