from fastapi import APIRouter

import data.money as money

router = APIRouter(prefix="/information", tags=["Information"])


@router.get("/balance")
def get_balance():
    return {f"Остаток средств ППОНа: {money.ppon_balance}"}

