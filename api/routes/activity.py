from fastapi import APIRouter

import data.money as money
from api.models.activity import RequestShiftOnWarehouse, ResponseRest, ResponseShiftOnWarehouse

router = APIRouter(prefix="/activity", tags=["Activity"])


@router.post("/shift_on_warehouse")
def shift_on_warehouse(request: RequestShiftOnWarehouse) -> dict | ResponseShiftOnWarehouse:
    """Отработать смену на складе"""
    try:
        work_mode = request.pace
        current_wage = getattr(money.daily_wage, work_mode)
    except KeyError:
        return {"error": "Введённого темпа работы не существует"}

    money.ppon_balance += current_wage
    return ResponseShiftOnWarehouse(earned_today=current_wage, current_balance=money.ppon_balance)


@router.get("/rest")
def rest() -> dict | ResponseRest:
    """Отдохнуть как следует"""
    if money.ppon_balance < money.rest_cost:
        return {
            "error": f"Недостаточно средств, ППОН. Стоимость отдыха: {money.rest_cost}, а у тебя {money.ppon_balance}"}
    money.ppon_balance -= money.rest_cost
    return ResponseRest(wasted=money.rest_cost, current_balance=money.ppon_balance)
