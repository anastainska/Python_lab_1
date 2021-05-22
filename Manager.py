from enum import Enum


class SortOrder(Enum):
    ASC = 1
    DESC = 2


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
        result = []
        self.items.sort(key=lambda i: i.price, reverse=order.value)
        result.append(self.items)
        return result


class SortOrder(Enum):
    ASC = False
    DESC = True
