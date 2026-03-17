# -*- coding: utf-8 -*-

class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


class ItemUpdater:
    """Strategy base class: one updater per item type."""

    def __init__(self, item: Item):
        self.item = item

    def update(self):
        raise NotImplementedError

    def _decrease_sell_in(self):
        self.item.sell_in -= 1

    def _increase_quality(self, amount: int = 1):
        self.item.quality = min(50, self.item.quality + amount)

    def _decrease_quality(self, amount: int = 1):
        self.item.quality = max(0, self.item.quality - amount)


class NormalItemUpdater(ItemUpdater):
    def update(self):
        self._decrease_quality()
        self._decrease_sell_in()
        if self.item.sell_in < 0:
            self._decrease_quality()


class AgedBrieUpdater(ItemUpdater):
    def update(self):
        self._increase_quality()
        self._decrease_sell_in()
        if self.item.sell_in < 0:
            self._increase_quality()


class SulfurasUpdater(ItemUpdater):
    def update(self):
        # Legendary item: no changes to sell_in or quality
        pass


class BackstagePassUpdater(ItemUpdater):
    def update(self):
        if self.item.sell_in > 10:
            self._increase_quality()
        elif self.item.sell_in > 5:
            self._increase_quality(2)
        elif self.item.sell_in >= 0:
            self._increase_quality(3)

        self._decrease_sell_in()

        # After the concert (sell_in < 0) quality drops to 0
        if self.item.sell_in < 0:
            self.item.quality = 0


class ConjuredItemUpdater(ItemUpdater):
    def update(self):
        self._decrease_quality(2)
        self._decrease_sell_in()
        if self.item.sell_in < 0:
            self._decrease_quality(2)


def get_updater_for(item: Item) -> ItemUpdater:
    """Factory method returning the correct strategy for an item."""
    if item.name == "Aged Brie":
        return AgedBrieUpdater(item)
    if item.name == "Sulfuras, Hand of Ragnaros":
        return SulfurasUpdater(item)
    if item.name.startswith("Backstage passes"):
        return BackstagePassUpdater(item)
    if item.name.startswith("Conjured"):
        return ConjuredItemUpdater(item)
    return NormalItemUpdater(item)


class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            updater = get_updater_for(item)
            updater.update()

