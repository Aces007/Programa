total_amount_of_money_you_can_spend = int(input("How much money do you possess?:"))
total_quantity_of_apples_you_want_to_buy = int(input("How much for the apple?:"))
you_can_purchase = total_amount_of_money_you_can_spend // total_quantity_of_apples_you_want_to_buy
your_change_is = total_amount_of_money_you_can_spend % total_quantity_of_apples_you_want_to_buy
print(f"You can buy {you_can_purchase} apples and your change is {your_change_is} pesos")