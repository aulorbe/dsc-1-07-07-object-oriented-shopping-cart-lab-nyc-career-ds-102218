#read is get ; write is set

class ShoppingCart:
    # write your code here
    def __init__(self,total=0,items=[],employee_discount=None):
        self._total = total
        self._items = items
        self._employee_discount = employee_discount

    def get_total(self):
        return self._total

    def set_total(self,total):
        self._total = total

    def del_total(self):
        self._total = None #this way, you're not permanently deleting your total section in your class, you're just saying it's nothing right now

    total = property (get_total,set_total,del_total)

    def get_item(self):
        return self._item

    def set_item(self,item):
        self._item= item

    def del_item(self):
        self._item = None

    item = property (get_item,set_item,del_item)

    def get_employee_discount(self):
        return self._employee_discount

    def set_employee_discount(self,employee_discount):
        self._employee_discount= employee_discount

    def del_employee_discount(self):
        self._employee_discount = None

    employee_discount = property (get_employee_discount,set_employee_discount,del_employee_discount)


# Next, we want to define an instance method called add_item that will add an item to our cart. It should take in the name of an
# item, its price and an optional quantity. The method should increase the shopping cart's total by the appropriate amount and
# return the new total for the shopping cart.

    def add_item(self,item_name,price,quantity=None):
        item = {'item_name': item_name, 'price': price, 'quantity': quantity}
        self._items.append(item)

        self.total = 0

        for i in self._items:
            if i['quantity'] != None:
                price = i['price'] * i['quantity']
                self.total += price
            else:
                self.total += i['price']

        return self.total

# self._items is a list of dictionaries and looks like:
# [{'item_name': 'eggs', 'price': 5, 'quantity': 10}, {'item_name': 'milk', 'price': 10, 'quantity': 2}]

    def median_item_price(self):
            import statistics

            item_prices = []
            for i in self._items:
                item_prices.append(i['price']) #putting all prices into a list

            sorting = sorted(item_prices) #sorting my list of dictionaries (self._items) in ascending order

            # Then check to see if there is an odd number of elements in our list. If so, the middle number is the median
            if len(sorting) % 2 != 0:
                median = statistics.median(sorting)
                print(median)
            else:
                print('you have an even number of items in your cart! find the mean instead!')


    def mean_item_price(self):
            import statistics

            item_prices = []
            for i in self._items:
                item_prices.append(i['price'])

            sorting = sorted(item_prices)

            if len(sorting) % 2 != 0:
                print('you have an odd number of items in your cart! find the median instead!')
            else:
                mean = statistics.mean(sorting)
                rounded = round(mean,2)
                print(rounded)

# applies a discount if one is provided and returns the discounted total. For example, if we initialize a new shopping cart with a discount
# of 20% then our total should be discounted in the amount of 20%. So, if our total were $100, after the discount we only would owe $80.
# If our shopping cart does not have an employee discount, then it should return a string saying: "Sorry, there is no discount to apply to your cart :("

    def apply_discount(self):
        if self._employee_discount:
            discount = self.employee_discount/100
            disc_total = self.total * (1 - discount)
            return disc_total
        else:
            return "Sorry, there is no discount to apply to your cart :("


# Let's define an instance method called item_names which returns a list of names which represent each item we have in our cart --
# if there are three socks the list should contain three "socks".

    def item_names(self):
        names = []
        for i in self._items:
            names.append(i['item_name'])
        return names

# Let's define a method called void_last_item that removes the last item from our shopping cart and updates its total.
# If there are no items in the shopping cart, void_last_item should return "There are no items in your cart!".
    def void_last_item(self):
        if self._items:
            removed_item = self._items.pop()
        else:
            return "There are no items in your cart!"
        self.total -= removed_item['price']
