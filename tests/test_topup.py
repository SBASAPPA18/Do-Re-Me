import pytest
from src.topup import TopUp, TopUpManager

def test_topup_cost():
    topup = TopUp("TEN_DEVICES", 1)
    assert topup.get_cost() == 100

def test_topup_manager():
    manager = TopUpManager()
    manager.add_topup("FOUR_DEVICE", 2)
    assert manager.get_topup().get_cost() == 100
