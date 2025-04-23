# Carly's Clippers
# You are the Data Analyst at Carly’s Clippers, the newest hair salon on the
# block. Your job is to go through the lists of data that have been collected
# in the past couple of weeks. You will be calculating some important metrics
# that Carly can use to plan out the operation of the business for the rest of
# the month.

# Create list of hairstyles
hairstyles = ["bouffant", "pixie", "dreadlocks",
              "crew", "bowl", "bob", "mohawk", "flattop"]

# Create list of prices (corresponding to each respective hairstyles)
prices = [30, 25, 40, 20, 20, 35, 50, 35]

# Create list of number of times a haircut was purchased
# (corresponding to each respective hairstyles)
last_week = [2, 3, 5, 8, 4, 4, 6, 2]

# Calculate total price of all haircuts
total_price = 0
for price in prices:
    total_price += price

# Calculate average price of haircuts
average_price = total_price/len(prices)
print("Average Haircut Price:", average_price)

# Adjust prices by reducing $5 from each
new_prices = [price - 5 for price in prices]
print(new_prices)

# Calculate total revenue from last week


def calculate_total_revenue(prices, last_week):
    total_revenue = 0
    for i in range(0, len(prices)):
        total_revenue += prices[i]*last_week[i]
    return total_revenue


total_revenue = calculate_total_revenue(prices, last_week)
print("Total Revenue: ", total_revenue)

average_daily_revenue = total_revenue/7
print("Average Daily Revenue: ", average_daily_revenue)

# Determine haircuts under $30 after price reduction
cuts_under_30 = [hairstyles[i]
                 for i in range(len(new_prices)) if new_prices[i] < 30]

# cuts_under_30 = []
# for i in range(len(new_prices)):
#   if prices[i] < 30:
#     cuts_under_30.append(hairstyles[i])

print(cuts_under_30)
