from dataclasses import dataclass
from abc import ABCMeta, abstractmethod

@dataclass
class ProductData(ABCMeta):
    id: int
    product_type_id: int
    product_id: int

    @abstractmethod
    def get_product_name(self):
        ...
    