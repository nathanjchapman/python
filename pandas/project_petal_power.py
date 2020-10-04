import pandas as pd

inventory = pd.read_csv('inventory.csv')

print(inventory.head(10))

staten_island = inventory[:10]
print(type(staten_island))
product_request = staten_island.product_description
print(product_request)

seed_request = inventory[inventory.product_type == "seeds"]
print(seed_request)

in_stock = lambda x: True if x > 0 else False

inventory['in_stock'] = inventory.quantity.apply(in_stock)

total_value = lambda x: x.price * x.quantity

inventory['total_value'] = inventory.apply(total_value, axis=1)

combine_lambda = lambda row: \
	"{} - {}".format(row.product_type, row.product_description)

inventory['full_description'] = inventory.apply(combine_lambda, axis=1)

print(inventory)
