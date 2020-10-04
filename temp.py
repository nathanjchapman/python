def return_translated_point(x, y, change_x, change_y):
  return x + change_x, y + change_y

a, b = return_translated_point(1, 2, 5, 8)
print(b)