from shopping_cart import ShoppingCart

shopping_cart = ShoppingCart()

shopping_cart.add_item("rainbow sandals", 45.99)
shopping_cart.add_item("agyle socks", 10.50)
shopping_cart.add_item("jeans", 50.00, 3)
shopping_cart.add_item("plants", 20.00, 2)


print(shopping_cart.get_total())


print(shopping_cart.median_item_price()) # 50.00  <<< how is that the answer to the median question? should be $45.99 when have the 1st 3 items in cart
print(shopping_cart.mean_item_price())

discount_shopping_cart = ShoppingCart(20)
print(shopping_cart.apply_discount())

print(shopping_cart.item_names())

print(shopping_cart.void_last_item())
