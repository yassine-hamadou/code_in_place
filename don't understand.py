sandwhich_orders = [
    'maca',
    'viande',
    'pastrami', 
    'capo', 
    'pastrami', 
    'pastrami',
    ]
finished_orders = []

for sandwhich_order in sandwhich_orders[:]:
    if sandwhich_order == 'pastrami':
        print(f"The deli has run out of {sandwhich_order}.")
    else:
        print(f"your {sandwhich_order} sandwhich is made.")
        finished_orders.append(sandwhich_order)
        sandwhich_orders.remove(sandwhich_order)

for finished_order in finished_orders:
    print(f"{finished_order} has been made.")

while 'pastrami' in sandwhich_orders:
    sandwhich_orders.remove('pastrami')

print(sandwhich_orders)
print(finished_orders)