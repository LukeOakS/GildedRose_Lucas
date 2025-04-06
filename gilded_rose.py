# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:

            if (item.quality > 0 and item.quality < 50) or item.name == "Aged Brie":

                if item.name == "Aged Brie":
                    self.__handle_aged_brie(item)

                elif item.name == "Backstage passes to a TAFKAL80ETC concert":
                    self.__handle_backstage(item)
                
                elif item.name == "Conjured Mana Cake":
                    self.__handle_conjured(item)
                
                else:
                    self.__handle_common_items(item)

            if item.name != "Sulfuras, Hand of Ragnaros":
                item.sell_in -= 1
            else:
                self.__handle_sulfuras()

    def __handle_common_items(self, item):
        item.quality -= 1

        if item.sell_in < 0 and item.quality > 0:
            item.quality -= 1

    def __handle_aged_brie(self, item):
        if item.quality < 50: 
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

    def __handle_sulfuras(self):
        return
        
    def __handle_conjured(self, item):
        item.quality -= 1

        if item.quality > 0:
            item.quality -= 1

        if item.sell_in < 0:
            item.quality -= 1
            if item.quality > 0:
                item.quality -= 1

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
