print("The apple's price is 20 pesos")
apple = 20
print("The orange's price is 25 pesos")
orange = 25
total_number_of_apple_to_buy = int(input("How many apples would you prefer to buy?:"))
total_number_of_orange_to_buy = int(input("How many oranges would you prefer to buy?:")) 
TotalQuantityOfApples = apple * total_number_of_apple_to_buy
TotalQuantityOfOranges = orange * total_number_of_orange_to_buy
amount = TotalQuantityOfApples + TotalQuantityOfOranges
print(f"The total amount is {amount}.")