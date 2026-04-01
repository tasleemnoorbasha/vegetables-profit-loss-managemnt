# Vegetable Shop Management

veg = ["cabbage", "cauliflower", "capsicum"]
quantity = [10, 5, 15]

# cost price (what shopkeeper bought at)
cost_price = [20, 30, 25]

# selling price
sell_price = [35, 40, 60]

total_sales = 0
total_cost = 0

while True:
    print("\nAvailable items:", veg)
    customer_total = 0

    while True:
        item = input("Enter item you want (or type 'done' to finish): ")

        if item == "done":
            break

        if item in veg:
            idx = veg.index(item)
            qty = float(input("Enter quantity (kg): "))

            if qty <= quantity[idx]:
                amount = qty * sell_price[idx]
                cost = qty * cost_price[idx]

                quantity[idx] -= qty
                customer_total += amount
                total_sales += amount
                total_cost += cost

                print("Added to cart. Cost:", amount, "rupees")
            else:
                print("Out of stock")
        else:
            print("Item not available")

    print("Customer bill:", customer_total, "rupees")

    ch = input("Next customer? (yes/no): ")
    if ch == "no":
        break

# Shop summary
print("\n--- SHOP SUMMARY ---")
print("Total Sales:", total_sales)
print("Total Cost:", total_cost)

profit = total_sales - total_cost

if profit > 0:
    print("Profit:", profit)
else:
    print("Loss:", profit)

print("\nRemaining Stock:")
for k in zip(veg, quantity):
    print(k[0], "-", k[1], "kgs")
