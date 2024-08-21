class TopUp:
    def __init__(self, name, months):
        self.name = name
        self.months = months
        self.cost = self.calculate_cost()

    def calculate_cost(self):
        cost = {
            "FOUR_DEVICE": 50,
            "TEN_DEVICES": 100
        }
        return cost[self.name] * self.months

    def get_cost(self):
        return self.cost

class TopUpManager:
    def __init__(self):
        self.topup = None

    def add_topup(self, name, months):
        self.topup = TopUp(name, months)

    def get_topup(self):
        return self.topup
