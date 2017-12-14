# CTI-110 
# M2HW2 - Tip Tax Total 
# William Thomas
# 14 September 2017
# Calculates and displays tip, tax, and total amount when given a net bill amount (user input.)

# Get input for net bill amount (net_bill).
net_bill = float (input('Enter the original bill amount: $ '))

# Get input for discount rate.
discount = input('Enter the discount rate (if none, enter 0): ')

# Calculate discount rate as a percentage.
if discount.isdigit():
    discount_rate = float(discount) /100 * net_bill

# Calculate discount_bill as net_bill minus discount_rate.
discount_bill = net_bill - discount_rate

# Calculate tax as 7% of discount_bill.
tax = discount_bill * 0.07

# Calculate tip as 18% of discount_bill.
tip = discount_bill * 0.18

# Calculate total cost as net_bill + tax + tip.
total_cost = discount_bill + tip + tax

# Display net bill, discount, tax, tip, and total amount in U.S.D. with two decimal places.
print('Original bill: $', format(net_bill, ',.2f'))
print('The discounted bill is: $', format(discount_bill, ',.2f'))
print('Tax: $', format(tax, ',.2f'))
print('Tip: $', format(tip, ',.2f'))
print('Total cost: $', format(total_cost, ',.2f'))
