import dataclasses
import random

# Сумма денег на счёте ППОНА
ppon_balance = 10000
# Стоимость отдыха ППОНА
rest_cost = 24000

@dataclasses.dataclass
class DailyWage:
    """Величина оплаты труда ППОНА при разных режимах работы"""
    min_relax = 3000
    max_relax = 4500
    min_medium = 5000
    max_medium = 6200
    min_hard = 5000
    max_hard = 8200
    relax: int|None = random.randint(min_relax, max_relax)
    medium: int|None  = random.randint(min_medium, max_medium)
    hard: int|None  = random.randint(min_hard, max_hard)


daily_wage = DailyWage()
