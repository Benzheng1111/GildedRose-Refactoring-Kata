# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):
    def _update(self, item, days=1):
        """Helper: run update_quality for given days on a single item."""
        gr = GildedRose([item])
        for _ in range(days):
            gr.update_quality()
        return item

    def test_normal_item_degrades_by_one_before_sell_date(self):
        items = [Item("+5 Dexterity Vest", 10, 20)]
        gr = GildedRose(items)
        gr.update_quality()
        self.assertEqual(9, items[0].sell_in)
        self.assertEqual(19, items[0].quality)

    def test_aged_brie_increases_in_quality_up_to_50(self):
        item = Item("Aged Brie", 2, 49)
        self._update(item)
        self.assertEqual(1, item.sell_in)
        self.assertEqual(50, item.quality)

    def test_sulfuras_never_changes(self):
        item = Item("Sulfuras, Hand of Ragnaros", 0, 80)
        self._update(item)
        self.assertEqual(0, item.sell_in)
        self.assertEqual(80, item.quality)

    def test_backstage_passes_drop_to_zero_after_concert(self):
        item = Item("Backstage passes to a TAFKAL80ETC concert", 1, 49)
        # two days so that sell_in goes from 1 -> 0 -> -1
        self._update(item, days=2)
        self.assertEqual(-1, item.sell_in)
        self.assertEqual(0, item.quality)


if __name__ == '__main__':
    unittest.main()
