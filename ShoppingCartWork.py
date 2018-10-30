from shopping_cart import ShoppingCart

shopping_cart = ShoppingCart()

print(shopping_cart.total)
print(shopping_cart.employee_discount)

print(shopping_cart.add_item("rainbow sandals", 45.99)) # 45.99
print(shopping_cart.add_item("agyle socks", 10.50)) # 56.49
print(shopping_cart.add_item("jeans", 50.00, 3)) # 206.49
print(shopping_cart.add_item("plants", 20.00, 2)) #246.49

shopping_cart.median_item_price() # 50.00  <<< how is that the answer to the median question? should be $45.99 when have the 1st 3 items in cart
shopping_cart.mean_item_price() 
