from math import floor

# amount:         9876
# - paid_amount:  9870
# ____________________
# reminder:          6
# + cash_back:     987
# ____________________
# amount:          993
# ...

cases_count = int(input())

for i in range(0, cases_count):
    initial_amount = amount = int(input())
    total_amount = 0
    while amount:
        reminder = (amount % 10) if amount >= 10 else 0
        paid_amount = amount - reminder
        cash_back = floor(paid_amount / 10)

        amount = reminder + cash_back
        total_amount += paid_amount

    print(total_amount)

