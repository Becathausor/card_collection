import abc

class Filterer(abc.ABCMeta):
    def __init__(self) -> None:
        pass

    @abc.abstractmethod
    def _discrimination_method(self, datum):
        ...

    def apply(self, data):
        return list(filter(self._discrimination_method, data))
    

class NoFilter(Filterer):
    def _discrimination_method(self, datum):
        return True
        
