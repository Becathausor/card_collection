from dataclasses import dataclass
from . import dataclasslist

@dataclass
class ProductType:
    id: int
    product_name: str