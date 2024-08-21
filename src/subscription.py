from datetime import timedelta

class Subscription:
    def __init__(self, category, plan, start_date):
        self.category = category
        self.plan = plan
        self.start_date = start_date
        self.end_date = self.calculate_end_date()

    def calculate_end_date(self):
        plan_duration = {
            "FREE": 1,
            "PERSONAL": 1,
            "PREMIUM": 3
        }
        return self.start_date + timedelta(days=plan_duration[self.plan] * 30)

    def get_reminder_date(self):
        return self.end_date - timedelta(days=10)

    def get_cost(self):
        cost = {
            "MUSIC": {"FREE": 0, "PERSONAL": 100, "PREMIUM": 250},
            "VIDEO": {"FREE": 0, "PERSONAL": 200, "PREMIUM": 500},
            "PODCAST": {"FREE": 0, "PERSONAL": 100, "PREMIUM": 300}
        }
        return cost[self.category][self.plan]

class SubscriptionManager:
    def __init__(self):
        self.subscriptions = []
        self.topup = None
        self.start_date = None

    def set_start_date(self, start_date):
        self.start_date = start_date

    def add_subscription(self, category, plan):
        if self.start_date:
            subscription = Subscription(category, plan, self.start_date)
            self.subscriptions.append(subscription)

    def set_topup(self, topup):
        self.topup = topup

    def print_renewal_details(self):
        total_cost = 0
        for sub in self.subscriptions:
            reminder_date = sub.get_reminder_date().strftime("%d-%m-%Y")
            cost = sub.get_cost()
            total_cost += cost
            print(f"RENEWAL_REMINDER {sub.category} {reminder_date}")
        
        if self.topup:
            total_cost += self.topup.get_cost()
        
        print(f"RENEWAL_AMOUNT {total_cost}")
