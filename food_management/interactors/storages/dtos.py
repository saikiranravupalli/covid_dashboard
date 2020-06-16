from dataclasses import dataclass
from datetime import date
from typing import List

@dataclass
class ItemQuantityDto:
    item_id: int
    quantity: int

@dataclass
class MealDto:
    meal_id: int
    on_date: date
    preference_type: str
    items: List[ItemQuantityDto]
