from dataclasses import dataclass
from information_accessor import dao

@dataclass
class AccessoryData:
    accessory_id: int
    accessory_type_id: int
    version: int
    product_name: str

    def __str__(self):
        return f"Accessoire {self.accessoire_id}: {self.product_name} ({dao.get_accessory_type(self.accessory_type_id)}))"


