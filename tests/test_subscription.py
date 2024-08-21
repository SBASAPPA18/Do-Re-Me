import pytest
from datetime import datetime
from src.subscription import Subscription, SubscriptionManager

def test_subscription_cost():
    start_date = datetime(2022, 2, 20)
    sub = Subscription("MUSIC", "PERSONAL", start_date)
    assert sub.get_cost() == 100

def test_reminder_date():
    start_date = datetime(2022, 2, 20)
    sub = Subscription("VIDEO", "PREMIUM", start_date)
    assert sub.get_reminder_date() == datetime(2022, 5, 10)

def test_subscription_manager():
    manager = SubscriptionManager()
    manager.set_start_date(datetime(2022, 2, 20))
    manager.add_subscription("MUSIC", "PERSONAL")
    manager.add_subscription("VIDEO", "PREMIUM")
    assert len(manager.subscriptions) == 2
