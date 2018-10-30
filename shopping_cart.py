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
        total = []
        for i in self._items:
            if i['quantity'] == None:
                total.append(i['price']*1)
            else:
                total.append(i['price']*i['quantity'])

        return sum(total)

# Finally, if there is an even number of elements in the list, the median will be the average or mean of the two center elements
#  (e.g. given the list [1,2,3,4] the elements 2 and 3 are the two center elements and the median would be (2 + 3)/2 or 2.5).

    def median_item_price(self,item_name,price,quantity=None):
        import statistics #return average price per item
        item = {'item_name': item_name, 'price': price, 'quantity': quantity}
        self._items.append(item)

         # self._items is a list of dictionaries and looks like:
         # [{'item_name': 'eggs', 'price': 5, 'quantity': 10}, {'item_name': 'milk', 'price': 10, 'quantity': 2}]

        sorting = sorted(self._items,key = lambda i:  i['price']) #sorting my list of dictionaries (self._items) in ascending order

        item_prices = []
        for i in sorting:
            item_prices.append(i['price'])

        # Then check to see if there is an odd number of elements in our list. If so, the middle number is the median
        if len(item_prices) % 2 != 0: #if there is an odd number of items in your cart...
            median = statistics.median(item_prices)
            print(median)
        else:
            print('you have an even number of items in your cart! find the mean instead!')


    def mean_item_price(self): #return median price per item
        pass
