from dataclasses import dataclass
from .product_data import ProductData


@dataclass
class BoosterData:
    booster_id: int
    extension_id: int
    booster_type_id: int

    def __str__(self):
        return f"Booster "
    