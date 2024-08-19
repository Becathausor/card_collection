from dataclasses import dataclass


@dataclass
class RarityData:
    rarity_id: int
    name: str

    def __str__(self):
        return self.name
    