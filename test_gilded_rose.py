# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    
    def test_foo(self):
        items = [Item("foo", 0, 0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual("foo", items[0].name)

    def test_item_attribute(self):
        items = [Item("foo", None, 0)]
        self.assertIsNone(items[0].sell_in)

    def test_quality_decrease_before_sell_in(self):
        items = [Item("foo", 0, 1)]
        gildedRose = GildedRose(items)
        gildedRose.update_quality()
        self.assertEqual(0, items[0].quality)

    def test_quality_decrease_after_sell_in(self):
        items = [Item("foo", -1, 2)]
        gildedRose = GildedRose(items)
        gildedRose.update_quality()
        self.assertEqual(0, items[0].quality)

    def test_quality_cannot_be_negative(self):
        items = [Item("foo", 0, 0)]
        gildedRose = GildedRose(items)
        gildedRose.update_quality()
        self.assertGreaterEqual(items[0].quality, 0)

    def test_aged_brie_increase_quality(self):
        items = [Item("Aged Brie", 0, 0)]
        gildedRose = GildedRose(items)
        gildedRose.update_quality()
        self.assertEqual(1, items[0].quality)

    def test_sulfuras_doesnt_change(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 1, 80)]
        items_validation = [Item("Sulfuras, Hand of Ragnaros", 1, 80)]
        gildedRose = GildedRose(items)
        gildedRose.update_quality()
        self.assertEqual(items_validation[0].name, items[0].name)
        self.assertEqual(items_validation[0].sell_in, items[0].sell_in)
        self.assertEqual(items_validation[0].quality, items[0].quality)

    def test_backstage_increase_quality(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 15, 20)]
        gildedRose = GildedRose(items)
        gildedRose.update_quality()
        self.assertEqual(21, items[0].quality)

    def test_backstage_increase_quality_when_sell_in_lessequal_ten(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 9, 20)]
        gildedRose = GildedRose(items)
        gildedRose.update_quality()
        self.assertEqual(22, items[0].quality)

    def test_backstage_increase_quality_when_sell_in_lessequal_five(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", 4, 20)]
        gildedRose = GildedRose(items)
        gildedRose.update_quality()
        self.assertEqual(23, items[0].quality)

    def test_backstage_decrease_to_zero(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", -1, 20)]
        gildedRose = GildedRose(items)
        gildedRose.update_quality()
        self.assertEqual(0, items[0].quality)

    def test_conjured_decrease_two_times_the_quality_before_sell_in(self):
        items = [Item("Conjured Mana Cake", 0, 6)]
        gildedRose = GildedRose(items)
        gildedRose.update_quality()
        self.assertEqual(4, items[0].quality)

    def test_conjured_decrease_two_times_the_quality_after_sell_in(self):
        items = [Item("Conjured Mana Cake", -1, 6)]
        gildedRose = GildedRose(items)
        gildedRose.update_quality()
        self.assertEqual(2, items[0].quality)
        
if __name__ == '__main__':
    unittest.main()
