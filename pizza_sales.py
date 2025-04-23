# You work at Len’s Slice, a new pizza joint in the neighborhood. You are
# going to use your knowledge of Python lists to organize some of your
# sales data.

# Your code below:

# Create list of toppings
toppings = ["pepperoni", "pineapple", "cheese",
            "sausage", "olives", "anchovies", "mushrooms"]

# Create list of prices
prices = [2, 6, 1, 3, 2, 7, 2]

# Count the number of instances of 2 in the prices list
num_two_dollar_slices = prices.count(2)
print(num_two_dollar_slices)

# Find the length of the toppings list
num_pizzas = len(toppings)
print(num_pizzas)

print(f"We sell {num_pizzas} different kinds of pizza!")

# Create a list of prices and toppings with each set in a seperate list


def create_pizza_and_prices(prices, toppings):
    return [[price, topping_name]
            for price, topping_name in zip(prices, toppings)]


pizza_and_prices = create_pizza_and_prices(prices, toppings)
print(pizza_and_prices)

# Sorting list by prices
# The first index of each list is a price integer
# so the the list will be sorted from lowest to largest number
pizza_and_prices.sort()
print(pizza_and_prices)
print("\n")

# Identify cheapest and priciest pizzas
cheapest_pizza = pizza_and_prices[0]
pricest_pizza = pizza_and_prices[-1]

# Remove the most expensive pizza/price set
pizza_and_prices.pop()

# Update list with new topping
pizza_and_prices.insert(4, [2.5, "peppers"])
print(pizza_and_prices)

# Extract and print three cheapest pizzas
three_cheapest = pizza_and_prices[:3]
print(three_cheapest)
