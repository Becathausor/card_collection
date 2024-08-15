from . import product_filter
from . import selector

class QueueFactory:
    def __init__(self, product_filterer: product_filter.ProductFilter, selector: selector.Selector):
        self.filterer = product_filterer
        self.selector = selector
        pass

    def get(self):
        data = self.filterer.apply(self._getAllData())
        for i in range(len(data)):
            i, datum = self.selector.pop_best(data)
            yield datum

    def _getAllData(self):
        raise NotImplementedError
    