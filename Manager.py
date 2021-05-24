from enum import Enum


class SortOrder(Enum):
    ASC = False
    DESC = True


class MeasureInstrumentManager:

    def __init__(self, items=list):
        self.items = items

    def search_by_producer(self, search_producer: str):
        result = []
        for item in self.items:
            if item.producer == search_producer:
                result.append(item)
        return result

    def sort_by_price(self, order: SortOrder):
        self.items.sort(key=lambda i: i.price, reverse=order.value)
        result = self.items
        return result
