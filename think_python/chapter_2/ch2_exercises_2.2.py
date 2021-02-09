
#2. Suppose the cover price of a book is $24.95, but bookstores get a 40% discount.
# Shipping costs $3 for the first copy and 75 cents for each additional copy.
# What is the total wholesale cost for 60 copies?
book_price = float(24.95)
print(f"Book price: ${book_price:.2f}")

discount = float(40)
print(f"Discount: {discount}%")

int_shipping_cost = float(3)
print(f"Initial shipping cost: ${int_shipping_cost}")

shipping_cost = float(.75)
print(f"Shipping cost after initial cost: ${shipping_cost}")

copies_ordered = float(60)
print(f"Copies ordered: {copies_ordered} copies")

total_book_cost = copies_ordered * book_price
print(f"Total book cost: ${total_book_cost:.2f}")

discount_amount = (total_book_cost) * (discount/100)
print(f"Discount amount: ${discount_amount:.2f}")

discounted_book_cost = total_book_cost - discount_amount
print(f"Discounted total book cost: ${discounted_book_cost:.2f}")

total_shipping_cost = int_shipping_cost + ((copies_ordered - 1) * shipping_cost)
print(f"Total shipping cost: ${total_shipping_cost:.2f}")

total_wholesale_cost = discounted_book_cost + total_shipping_cost
print(f"Total wholesale cost: ${total_wholesale_cost:.2f}")