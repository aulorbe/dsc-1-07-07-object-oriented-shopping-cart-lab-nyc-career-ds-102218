from shopping_cart import ShoppingCart

shopping_cart = ShoppingCart()

shopping_cart.add_item("rainbow sandals", 45.99)
shopping_cart.add_item("agyle socks", 10.50)
shopping_cart.add_item("jeans", 50.00, 3)
shopping_cart.add_item("plants", 20.00, 2)

# print(shopping_cart.add_item("rainbow sandals", 45.99)) # 45.99
# print(shopping_cart.add_item("agyle socks", 10.50)) # 56.49
# print(shopping_cart.add_item("jeans", 50.00, 3)) # 206.49
# print(shopping_cart.add_item("plants", 20.00, 2)) #246.49
# print(shopping_cart.add_item("plants", 10.00))

shopping_cart.get_total()


shopping_cart.median_item_price() # 50.00  <<< how is that the answer to the median question? should be $45.99 when have the 1st 3 items in cart
shopping_cart.mean_item_price()

discount_shopping_cart = ShoppingCart(20)
print(shopping_cart.apply_discount())

print(shopping_cart.item_names())

print(shopping_cart.void_last_item())
