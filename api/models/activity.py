from typing import Literal

from pydantic import BaseModel


class RequestShiftOnWarehouse(BaseModel):
    pace: Literal["relax", "medium", "hard"] = "medium"


class ResponseShiftOnWarehouse(BaseModel):
    earned_today: int
    current_balance: int


class ResponseRest(BaseModel):
    status: str = "Более-менее отдохнул"
    wasted: int
    current_balance: int
