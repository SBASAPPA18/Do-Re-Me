# DoReMi Subscription Management

## Overview
This project manages music, video, and podcast subscriptions with options for top-ups to increase the number of devices. It calculates renewal dates and total costs based on user inputs.

## Usage
1. Run `python src/main.py` with the appropriate commands.
2. Commands:
   - `START_SUBSCRIPTION DD-MM-YYYY`
   - `ADD_SUBSCRIPTION SUBSCRIPTION_CATEGORY PLAN_NAME`
   - `ADD_TOPUP TOP_UP_NAME NO_OF_MONTHS`
   - `PRINT_RENEWAL_DETAILS`

## Example
```shell
python src/main.py
START_SUBSCRIPTION 20-02-2022
ADD_SUBSCRIPTION MUSIC PERSONAL
ADD_SUBSCRIPTION VIDEO PREMIUM
ADD_TOPUP TEN_DEVICES 1
PRINT_RENEWAL_DETAILS
