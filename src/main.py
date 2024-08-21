from datetime import datetime
from subscription import SubscriptionManager
from topup import TopUpManager

def parse_date(date_str):
    return datetime.strptime(date_str, "%d-%m-%Y")

def main():
    subscription_manager = SubscriptionManager()
    topup_manager = TopUpManager()

    # Example command list; replace with actual command processing as needed
    commands = [
        "START_SUBSCRIPTION 20-02-2022",
        "ADD_SUBSCRIPTION MUSIC PERSONAL",
        "ADD_SUBSCRIPTION VIDEO PREMIUM",
        "ADD_TOPUP TEN_DEVICES 1",
        "PRINT_RENEWAL_DETAILS"
    ]

    start_date = None

    for command in commands:
        parts = command.split()
        action = parts[0]

        if action == "START_SUBSCRIPTION":
            start_date = parse_date(parts[1])
            subscription_manager.set_start_date(start_date)
        
        elif action == "ADD_SUBSCRIPTION":
            category = parts[1]
            plan = parts[2]
            subscription_manager.add_subscription(category, plan)
        
        elif action == "ADD_TOPUP":
            topup_name = parts[1]
            months = int(parts[2])
            topup_manager.add_topup(topup_name, months)
        
        elif action == "PRINT_RENEWAL_DETAILS":
            if start_date:
                subscription_manager.set_topup(topup_manager.get_topup())
                subscription_manager.print_renewal_details()

if __name__ == "__main__":
    main()
