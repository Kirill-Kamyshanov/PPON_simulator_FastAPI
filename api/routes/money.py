from fastapi import APIRouter

from data.money import ppon_balance

router = APIRouter(prefix="/finance", tags=["finance"])


@router.get("/balance")
def get_balance():
    return {f"Остаток средств ППОНа: {ppon_balance}"}

