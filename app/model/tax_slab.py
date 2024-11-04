from typing import List

from pydantic import BaseModel


class Slab(BaseModel):
    name: str
    amount: int
    percent: float


class TaxSlabs(BaseModel):
    slabs: List[Slab]
