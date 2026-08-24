from fastapi import APIRouter

import data.money as money
import data.prices
from data.prices import rest_cost
from data.prices import edible_food
from api.models.activity import RequestShiftOnWarehouse, ResponseRest, ResponseShiftOnWarehouse, ResponseGoShopping

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
    if money.ppon_balance < rest_cost:
        return {
            "error": f"Недостаточно средств, ППОН. Стоимость отдыха: {rest_cost}, а у тебя {money.ppon_balance}"}
    money.ppon_balance -= rest_cost
    return ResponseRest(wasted=rest_cost, current_balance=money.ppon_balance)

@router.post("/shopping")
def go_shopping(food: list[str]):
    """Закупиться в пятёрочке всяким вкусным"""
    total_cost = 0
    for item in food:
        total_cost += edible_food.get(item, 0)
    if total_cost == 0:
        return {"error": f"PPON, всё, что ты выбрал - не съедобное. Съедобная пища: {edible_food.keys()}"}
    if money.ppon_balance < total_cost:
        return {
            "error": f"Недостаточно средств, ППОН. Стоимость покупки: {total_cost}, а у тебя {money.ppon_balance}"}
    money.ppon_balance -= total_cost
    return ResponseGoShopping(spent=total_cost, current_balance=money.ppon_balance)