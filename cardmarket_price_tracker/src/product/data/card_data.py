from dataclasses import dataclass
@dataclass
class CardData:
    card_id: int
    name: str
    extension_id: int
    rarity: int
    