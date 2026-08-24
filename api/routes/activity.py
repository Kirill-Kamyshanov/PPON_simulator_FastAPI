from fastapi import APIRouter

from data.money import ppon_balance, daily_wage

router = APIRouter(prefix="/activity", tags=["act"])


# @router.post("/post")
# def shift_on_warehouse():
