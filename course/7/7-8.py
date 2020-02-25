sandwich_orders = ["beefsandwich","eggsandwich","porksandwich"]

finished_sandwiches =[]

while sandwich_orders:
    print("I made your tuna sandwich")
    finished_sandwiches.append(sandwich_orders.pop())
print("All done")

for sandwich in finished_sandwiches:
    print(sandwich)
