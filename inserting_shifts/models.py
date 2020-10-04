class Employee:
	def __init__(self, full_name, number, start_date, shift_pref):
		self.full_name = full_name
		self.number =number 
		self.start_date = start_date
		self.shift_pref = shift_pref
		self.occurances = 0
		self.shift = 'no shift assigned'

	def __repr__(self):
		return "{}: {} ({})".format(self.number, self.full_name, self.shift)


class Shift:
	def __init__(self, description, max_size):
		self.description = description
		self.max_size = max_size
		self.employees = []

	def __repr__(self):
		return self.description

	def has_opening(self):
		if len(self.employees) < self.max_size:
			return True
		else:
			return False



# Sort employees based on seniority and shift openings
def assign_shifts(employees, shifts):
	for employee in employees:
		for shift in employee.shift_pref:
			if shifts[shift].has_opening():
				shifts[shift].employees.append(employee)
				employee.shift = shifts[shift]
				print("{} was assigned {}".format(employee.full_name, shifts[shift]))
				break
			else:
				print("{} tried to get {}, but it was full.".format(employee.full_name, shifts[shift]))


# shift_pref
# A = 0
# B = 1
# C = 2
# D = 3
employee_info = [
	{'number': 35362, 'full_name': 'Lauren Durham', 'start_date': '2019-10-05', 'shift_pref': [0, 2, 1, 3]},
	{'number': 31272, 'full_name': 'Grace Sellers', 'start_date': '2019-17-25', 'shift_pref': [3, 0, 1, 3]},
	{'number': 37154, 'full_name': 'Shirley Rasmussen', 'start_date': '2014-03-12', 'shift_pref': [0, 2, 1, 3]},
	{'number': 35342, 'full_name': 'Brian Rojas', 'start_date': '2015-02-09', 'shift_pref': [0, 2, 3, 1]},
	{'number': 31153, 'full_name': 'Samantha Mosley', 'start_date': '2011-05-1', 'shift_pref': [0, 2, 1, 3]},
	{'number': 33054, 'full_name': 'Louis Guzman', 'start_date': '2018-08-17', 'shift_pref': [1, 2, 0, 3]},
	{'number': 36042, 'full_name': 'Denise Mcclure', 'start_date': '1991-03-12', 'shift_pref': [0, 2, 1, 3]},
	{'number': 32976, 'full_name': 'James Raymond', 'start_date': '2016-10-10', 'shift_pref': [0, 3, 1, 2]},
	{'number': 36425, 'full_name': 'Noah Collier', 'start_date': '2019-10-05', 'shift_pref': [0, 2, 1, 3]},
	{'number': 37679, 'full_name': 'Donna Frederick', 'start_date': '2005-12-14', 'shift_pref': [2, 0, 1, 3]},
	{'number': 37489, 'full_name': 'Nathan Chapman', 'start_date': '2020-12-30', 'shift_pref': [2, 0, 1, 3]}
]

def get_start_date(employee):
    return employee.get('start_date')

# order by start_date (seniority)
employee_info.sort(key=get_start_date)

shift_info = [
	{'description': 'A shift', 'max_size': 3},
	{'description': 'B shift', 'max_size': 2},
	{'description': 'C shift', 'max_size': 4},
	{'description': 'D shift', 'max_size': 1}
]

employees_list = []

for employee in employee_info:
	employees_list.append(Employee(employee['full_name'], employee['number'], employee['start_date'], employee['shift_pref']))


shifts_list = []

for shift in shift_info:
	shifts_list.append(Shift(shift['description'], shift['max_size']))


assign_shifts(employees_list, shifts_list)

for s in shifts_list:
	print(s.description, s.max_size, s.employees)

for e in employees_list:
	print(e)

# Manually assign shift for "Nathan Chapman"
nathan = employees_list[10]
nathan.shift = shifts_list[3]
print(nathan)
