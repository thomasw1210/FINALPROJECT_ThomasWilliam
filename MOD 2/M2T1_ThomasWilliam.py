# CTI-110 
# M2T1 - Sales Prediction 
# William Thomas
# 12 September 2017
# Calculates and displays 23% of input value.

# Get input for total_sales.
total_sales = float (input('Enter the projected sales: '))

# Calculate profit as 23 percent of total sales.
profit = total_sales * 0.23

# Display profit calculation.
print('The profit is $', format(profit, ',.2f'))
