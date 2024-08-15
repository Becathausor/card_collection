from . import product_filter
from . import selector
from . import queue_factory

class ProductLoader:
    def __init__(self, product_filterer=product_filter.default_filter, selector=selector.default_selector):
        self.filter = product_filterer
        self.priority_selector = selector
        self.queue_factory = queue_factory.QueueFactory(self.filter, self.priority_selector)
        self.queue = None
        pass

    def next(self):
        if self.queue in None:
            self.queue = self._loadNewQueue()
        return self.queue
    
    def nextBatch(self, batch_size: int=50):
        return [self.next() for i in range(batch_size)]
    
    def _loadNewQueue(self):
        self.queue_factory.get()

