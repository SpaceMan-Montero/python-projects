# Sal's Shipping

# This program will take the weight of a package and determine the
# cheapest way to ship that package using Sal’s Shippers.

def sal_shipping(weight):

    # Dictionary to contain various shipping costs.
    costs = {"Ground Shipping": 0,
             "Ground Shipping Premium": 0, "Drone Shipping": 0}

    # Ground Shipping

    if weight <= 2:
        cost_ground = 1.50*weight + 20
    elif 2 < weight <= 6:
        cost_ground = 3.00*weight + 20
    elif 6 < weight <= 10:
        cost_ground = 4.00*weight + 20
    else:
        cost_ground = 4.75*weight + 20
    print("Ground Shipping $", cost_ground)
    costs["Ground Shipping"] = cost_ground

    # Ground Shipping Premium

    cost_ground_premium = 125.00
    print("Ground Shipping Premium $", cost_ground_premium)
    costs['Ground Shipping Premium'] = cost_ground_premium

    # Drone Shipping

    if weight <= 2:
        cost_drone = 4.50*weight
    elif 2 < weight <= 6:
        cost_drone = 9.00*weight
    elif 6 < weight <= 10:
        cost_drone = 12.00*weight
    else:
        cost_drone = 14.25*weight
    print("Drone Shipping $", round(cost_drone, 3))
    costs['Drone Shipping'] = cost_drone

    # Determining Cheapest Shipping Costs (verison 1)

    minimum_cost = float('inf')
    shipping_method = None

    for key, value in costs.items():
        if value < minimum_cost:
            minimum_cost = value
            shipping_method = key

    print("The minimum shipping cost is", minimum_cost, "for", shipping_method)

    # Determining Cheapest Shipping Costs (verison 2)

    if cost_ground < cost_ground_premium and cost_ground < cost_drone:
        print("Cheapest option: Ground Shipping $", cost_ground)
    elif cost_ground_premium < cost_ground \
            and cost_ground_premium < cost_drone:
        print("Cheapest option: Ground Shipping Premium $",
              cost_ground_premium)
    else:
        print("Cheapest option: Drone Shipping $", cost_drone)


sal_shipping(4.8)
print("\n")
sal_shipping(41.5)

weight = float(input("Enter the package weight: "))
if weight <= 0:
    print("Weight must be a positive number")
    # exit()
else:
    sal_shipping(weight)
