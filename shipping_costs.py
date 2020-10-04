def ground_shipping(weight):
	flat = 20.00
	cost = flat
	if weight <= 2:
		cost = (weight * 1.50) + flat
	elif weight <= 6:
		cost = (weight * 3.00) + flat
	elif weight <= 10:
		cost = (weight * 4.00) + flat
	else:
		cost = (weight * 4.75) + flat
	return cost

assert(ground_shipping(8.4) == 53.60)


def drone_shipping(weight):
	cost = 0.00
	if weight <= 2:
		cost = weight * 4.50
	elif weight <= 6:
		cost = weight * 9.00
	elif weight <= 10:
		cost = weight * 12.00
	else:
		cost = weight * 14.25
	return cost

assert(drone_shipping(1.5) == 6.75)

premium = 125.00

def compare_costs(weight):
	drone = drone_shipping(weight)
	ground = ground_shipping(weight)
	if (drone < ground) and (drone < premium):
		return "Drone shipping is the cheapest at: ${}".format(drone)
	elif (ground < drone) and (ground < premium):
		return "Ground shipping is the cheapest at: ${}".format(ground)
	elif (ground == drone) and (ground == premium):
		return "Both shipping methods cost the same, at: ${}".format(premium)
	else:
		return "Premium Ground shipping is the cheapest at: ${}".format(premium)

print(compare_costs(4.8))
print(compare_costs(41.5))
