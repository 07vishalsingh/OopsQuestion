'''
1. You are building a simple shopping cart application. Your application needs to calculate the total cost of items in the cart, taking into account any applicable discounts. There are three types of discounts:

Percentage discount: A certain percentage off the total cost.
Fixed discount: A fixed amount deducted from the total cost.
Buy One Get One Free (BOGO) discount: For every two items of the same type, one item is free.
Your task is to implement a function in Python that takes the following inputs:

A dictionary representing the items in the cart, where the keys are item names and the values are quantities of those items.
A dictionary representing the discounts available, where the keys are discount types ("percentage", "fixed", "bogo") and the values are the discount amounts.
The function should return the total cost of the cart after applying the discounts.
'''
def calculate_total_cost(cart, discounts):
    total_cost = 0
    
    # Calculate total cost without considering discounts
    for item, quantity in cart.items():
        total_cost += item_price[item] * quantity
    
    # Apply percentage discount
    if "percentage" in discounts:
        percentage_discount = total_cost * (discounts["percentage"] / 100)
        total_cost -= percentage_discount
    
    # Apply fixed discount
    if "fixed" in discounts:
        total_cost -= discounts["fixed"]
    
    # Apply BOGO discount
    if "bogo" in discounts:
        for item, quantity in cart.items():
            # Calculate the number of free items for BOGO discount
            free_items = quantity // 2
            # Deduct the cost of free items
            total_cost -= item_price[item] * free_items
    
    return total_cost

# Example usage
item_price = {"apple": 2, "banana": 1.5, "orange": 1}
cart = {"apple": 3, "banana": 2, "orange": 1}
discounts = {"percentage": 10, "fixed": 2, "bogo": None}  # Percentage: 10%, Fixed: $2, BOGO: Buy One Get One Free

total_cost = calculate_total_cost(cart, discounts)
print("Total cost after applying discounts:", total_cost)
