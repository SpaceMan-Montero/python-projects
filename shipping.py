# Sal's Shipping

# This program will take the weight of a package and determine the
# cheapest way to ship that package using Sal’s Shippers.

def sal_shipping(weight):

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

    # Ground Shipping Premium

    cost_ground_premium = 125.00
    print("Ground Shipping Premium $", cost_ground_premium)

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


sal_shipping(4)
