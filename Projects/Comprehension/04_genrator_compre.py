daily_sales = [5, 10, 12, 7, 3, 8, 9, 15]

total_cups = sum(sale for sale in daily_sales if sale > 5) # it will gives sum(10,12,7,8,9,15) and the sum function gives addition of all
print(total_cups)