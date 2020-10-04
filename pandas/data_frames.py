import pandas as pd



# df1 = pd.DataFrame({
# 	'Product ID': [1,2,3,4],
# 	'Product Name': ['t-shirt', 't-shirt', 'skirt', 'skirt'],
# 	'Color': ['blue', 'green', 'red', 'black']

# 	})
# # print(df1)



# df2 = pd.DataFrame(
# 	[
# 		[1, 'San Diego', 100],
# 		[2, 'Los Angeles', 120],
# 		[3, 'San Francisco', 90],
# 		[4, 'Sacramento', 115],
# 	],
# 	columns = ['Store ID', 'Location', 'Number of Employees']
# )
# print(df2)

# df = pd.read_csv('sample.csv')

# # print(df)

# imdb = pd.read_csv('imdb.csv')
# print(imdb.info())

# movie = imdb[imdb.name == 'The Dark Knight']
# print(movie)





# df = pd.read_csv('employees.csv')

# get_last_name = lambda name: name.split(" ")[-1]

# df['last_name'] = df.name.apply(
#   get_last_name
# )

# print(df)





# df = pd.read_csv('employees.csv')
# print(df.head())


# total_earned = lambda row: \
# 	(row['hourly_wage'] * 40) + (row['hours_worked'] - 40) * (row['hourly_wage'] * 1.5) \
# 	if row['hours_worked'] > 40 \
# 	else row['hours_worked'] * row['hourly_wage']

# df['total_earned'] = df.apply(total_earned, axis=1)






# orders = pd.read_csv('shoefly.csv')

# is_vegan = lambda mat: 'animal' if mat == 'leather' else 'vegan'

orders['shoe_source'] = orders.shoe_material.apply(is_vegan)

is_gender = lambda row: \
  'Dear Mr. {}'.format(row.last_name) \
  if row.gender == 'male' \
  else 'Dear Ms. {}'.format(row.last_name)

orders['salutation'] = orders.apply(is_gender, axis=1)

print(orders.head(12))

mylambda = lambda x: x**2 + 3*x \
    if x > 7 \
    else 2*x - 10
print(mylambda(4))

# Generally, you’ll always see a groupby statement followed by reset_index:
df.groupby('column1').column2.measurement().reset_index()

# In Pandas, the command for pivot is:

df.pivot(columns='ColumnToPivot',
         index='ColumnToBeRows',
         values='ColumnToBeValues')








user_visits = pd.read_csv('page_visits.csv')

print(user_visits.head())

click_source = user_visits.groupby('utm_source').id.count().reset_index()

print(click_source.rename(columns={'id': 'count'}))

click_source_by_month = user_visits.groupby(['utm_source', 'month']).id.count().reset_index()

click_source_by_month_pivot = click_source_by_month.pivot(columns="month", index="utm_source", values="id").reset_index()

print(click_source_by_month_pivot)