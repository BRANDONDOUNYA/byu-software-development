"""
Compute the price of a meal as follows by asking for
the price of child and adult meals, the number of each,
and then the sales tax rate. Use these values to determine 
the total price of the meal. Then, ask for the payment amount
and compute the amount of change to give back to the customer.

author: ASILATSA DOUNYA BRANDON
Purpose: Meal Price Calculator

"""
#  I added the variables child_drink_price and adult_drink_price to ask for the
#  user to enter the prices of children and adult drinks, thenn I did multiplication
#  to find the children and adult drink subtotals and finally added to the child and 
#  adults meal subtotals to find the final subtotal.
child_meal_price = float(input("\nWhat is the price of a child's meal? "))
child_drink_price = float(input("What is the price of a child's drink? "))
adult_meal_price = float(input("What is the price of an adult's meal? "))
adult_drink_price = float(input("What is the price of an adult's drink? "))
num_children = int(input("What is the number of children? "))
num_adults = int(input("What is the number of adults? "))

children_meal_sub = num_children * child_meal_price
children_drink_sub = num_children * child_drink_price
adults_meal_sub = num_adults * adult_meal_price
adult_drink_sub = num_adults * adult_drink_price

children_subtotal = children_meal_sub + children_drink_sub
adults_subtotal = adults_meal_sub + adult_drink_sub

subtotal = children_subtotal + adults_subtotal

print(f"\nSubtotal: ${subtotal:.2f}")

sales_tax_rate = float(input("\nWhat is the sales tax rate? "))
sales_tax = (subtotal * sales_tax_rate) / 100 

print(f"Sales Tax: ${sales_tax:.2f}")

total = subtotal + sales_tax

print(f"Total: ${total:.2f}")

payment_amount = float(input("\nWhat is the payment amount? "))
change = payment_amount - total

print(f"Change: ${change:.2f}")