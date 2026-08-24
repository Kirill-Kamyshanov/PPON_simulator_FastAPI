import pytest

from api.models.activity import RequestShiftOnWarehouse
from api.routes.activity import shift_on_warehouse
from data.money import daily_wage


class TestActivity:
    @pytest.mark.parametrize("pace", ["relax", "medium", "hard"])
    def test_actual_wage_more_minimal_value(self, pace):
        """Проверка того, что за смену при выбранном темпе зарплата не ниже минимально допустимой"""
        actual_result = shift_on_warehouse(RequestShiftOnWarehouse(pace=pace))
        expected_min_wage = getattr(daily_wage, f"min_{pace}")
        assert actual_result.earned_today >= expected_min_wage, \
            f"Минимально возможный заработок при темпе работы {pace}: {expected_min_wage}, но получено: {actual_result.earned_today}"


    @pytest.mark.parametrize("pace", ["relax", "medium", "hard"])
    def test_actual_wage_less_maximal_value(self, pace):
        """Проверка того, что за смену при выбранном темпе зарплата не выше максимально допустимой"""
        actual_result = shift_on_warehouse(RequestShiftOnWarehouse(pace=pace))
        expected_max_wage = getattr(daily_wage, f"max_{pace}")
        assert actual_result.earned_today <= expected_max_wage, \
            f"Максимально возможный заработок при темпе работы {pace}: {expected_max_wage}, но получено: {actual_result.earned_today}"
