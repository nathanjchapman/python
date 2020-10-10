detail_string = "mon:0800:8,tue:0800:8,wed:0800:8,thu:0800:8,fri:0800:8"


def convert_string_shift(string):
	lst = []
	days = string.split(',')
	for day in days:
		shift = {}
		details = day.split(':')
		shift['weekday'], shift['start_time'], shift['hours'] = details[0], int(details[1]), int(details[2])
		lst.append(shift)
	return lst

shifts = convert_string_shift(detail_string)

print(shifts)
