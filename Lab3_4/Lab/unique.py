import gen_random

class Unique(object):
    def __init__(self, items, **kwargs):
        self.ignore_case = kwargs.get('ignore_case', False)
        self.seen = set()

        if self.ignore_case:
            self.items = (str(item).lower() for item in items)
        else:
            self.items = iter(items)

    def __next__(self):
        while True:
            item = next(self.items)
            key = item.lower() if self.ignore_case else item
            if key not in self.seen:
                self.seen.add(key)
                return item

    def __iter__(self):
        return self
