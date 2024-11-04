from typing import List, Optional, Literal

from pydantic import BaseModel


class Salary(BaseModel):
    amount: float
    times: int


class Bonus(BaseModel):
    amount: float
    festivalName: Optional[str]


class ProfitFromInvestment(BaseModel):
    amount: float
    name: Optional[str]


class Income(BaseModel):
    salaries: List[Salary]
    bonuses: List[Bonus]
    profitFromInvestments: List[ProfitFromInvestment]


class Information(BaseModel):
    gender: Literal["Male", "Female"]
    income: Income

