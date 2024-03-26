#Functions with branches/loops
#Example: ebay_fee() function from zybooks
#A function's block of statements may include branches, loops, and other statements.
#The following example uses a function to compute the amount 
# that an online auction/sales website charges a customer who sells an item online.
def ebay_fee(sell_price):
    """Returns the fees charged by ebay.com given the selling
    price of fixed-price books, movies, music, or video games.
    fee is $0.50 to list plus 13% of selling price up to $50.00,
    5% of amount from $50.01 to $1000.00, and 
    2% for amount $1000.01 or more."""

    p50 = 0.13  # for amount $50 and lower
    p50_to_1000 = 0.05  # for $50.01-$1000
    p1000 = 0.02  # for $1000.01 and higher
    fee = 0.50  # fee to list item

    if sell_price <= 50:
        fee  = fee + (sell_price*p50)
    elif sell_price <= 1000:
        fee = fee + (50*p50) + ((sell_price-50)*p50_to_1000)
    else:
        fee = fee + (50*p50) + ((1000-50)*p50_to_1000) \
                  + ((sell_price-1000)*p1000)

    return fee

selling_price = float(input('Enter item selling price (ex: 65.00): '))
print('Ebay fee: $', ebay_fee(selling_price))

#6.9.2: Missing return common error.

def steps_to_feet(num_steps):
    feet_per_step = 3
    feet = num_steps * feet_per_step
    # Missing return statement!
	
feet_per_mile = 5280
steps = 1000
feet = steps_to_feet(steps)
print("Distance walked in feet:", feet)