
class RetailItem:
    class RetailItem:

        # The __init__ method initializes the attributes.
        def __init__(self, item, units, price):
            self.__item = item
            self.__units = units
            self.__price = price

        # The following methods are mutators for the class.
        def set_item(self, item):
            self.__item = item

        def set_units(self, units):
            self.__units = units

        def set_price(self, price):
            self.__price = price

        # The following methods are accessors for the class.
        def get_item(self):
            return self.__item

        def get_units(self):
            return self.__units

        def get_price(self):
            return self.__price

        # The __str__ method returns the object's state as a
        #   string.
        def print(self):
            return 'Item Description:' + self.__item, \
                   '\tNumber of Units:' + self.__units, \
                   '\tPrice: $' + self.__price

        # The decrementInventory function decreases the number
        #   units each time called.
        def decrementInventory(units):
            if units > 0:
                units -= 1
            else:
                units = 0
class CashRegister():
    # The __init__ method initializes the attributes.
    global total = 0
    def __init__(self, purchase_item):
        self.__purchase_item = []

    def purchase_list(item, units):
        item_purchase.append(item)
        RetailItem.decrementInventory(units)

    def get_total(price):
        total += price
        return total

    def show_items(item_list):
        for item in item_list:
            print(item.get_item())
            print(item.get_units())
            print(item.get_price())
            print()

    def clear():
        purchase_list [:] = []




SHOW = 1
PURCHASE = 2
CART = 3
TOTAL = 4
EMPTY = 5
QUIT = 6

def main():
    mylist = make_list()
    mycashregister = CashRegister(mylist)

    choice = 0

    # Process menu selections until user quits program.
    while choice != QUIT:
        # Get the user's menu choice.
        choice = get_menu_choice()
        # Proces the choice.
        if choice == SHOW:
            mycashregister.print()
        elif choice == PURCHASE:
            purchase()
        elif choice == CART:
            mycashregister.cart(mycashregister)
        elif choice == TOTAL:
            mycashregister.total(mycashregister)
        elif choice == EMPTY:
            mycashregister.empty(mycashregister)

def make_list():

    item_list = []

    item = 'Jacket'
    units = 12
    price = 59.95
    entry = RetailItem(item, units, price)
    item_list.append(entry)

    item = 'Jeans'
    units = 40
    price = 34.95
    entry = RetailItem(item, units, price)
    item_list.append(entry)

    item = 'Shirt'
    units = 20
    price = 24.95
    entry = RetailItem(item, units, price)
    item_list.append(entry)

    return item_list

# The get_menu_choice function displays the menu and gets
#   a validated choice from the user.
def get_menu_choice():
    print()
    print('CASH REGISTER MENU')
    print('-------------------------')
    print('1. Show Retial Items')
    print('2. Purchase an Item(s)')
    print('3. Show Current Shopping Cart')
    print('4. Show Total of Items Purchased')
    print('5. Empty Your Shopping Cart')
    print('6. Quit the program')
    print()

    # Get the user's choice.
    choice = int(input('Enter your choice: '))

    # Validate the choice.
    while choice < SHOW or choice > QUIT:
        choice = int(input('Enter a valid choice: '))

    # Return the user's choice.
    return choice

def display_list(item_list):
    for item in item_list:
        print('Item Description:', item.get_item(), \
              '\tNumber of Units:', item.get_units(), \
              '\tPrice:', item.get_price())
    print()

def purchase():
    item_purchase = input('Enter the item you wish to purchase: ')
    CashRegister(item_purchase)

main()