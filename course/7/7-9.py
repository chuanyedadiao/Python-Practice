sandwich_orders = ["pastrami","beefsandwich","pastrami","eggsandwich","pastrami","porksandwich"]

finished_sandwiches =[]

while "pastrami" in sandwich_orders:
    sandwich_orders.remove("pastrami")

while sandwich_orders:
    print("I made your tuna sandwich")
    finished_sandwiches.append(sandwich_orders.pop())
print("All done")

for sandwich in finished_sandwiches:
    print(sandwich)
