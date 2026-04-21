# Import date
from datetime import date

# Import Optional
from typing import Optional

# Import BaseModel
from pydantic import BaseModel

# Define model Item
class Item(BaseModel):
    name: str
    quantity: int = 0
    expiration: Optional[date] = None