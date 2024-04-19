# Type code for classes here
class ItemToPurchase:
    def __init__ (self,item_name='none',item_price=0,item_quantity=0,total=0,item_total=0):
        self.item_name=item_name
        self.item_price=item_price
        self.item_quantity=item_quantity
        self.total=total
        self.item_total=item_total
    
    def print_item_cost(self):
        print('{} {} @ ${:.0f} = ${:.0f}'.format(self.item_name,self.item_quantity,self.item_price,self.item_quantity * self.item_price))
    
    def item_input(__init__,self):
        self.item_name=input('Enter the item name: ')
        self.item_price=float(input('Enter the item price: '))
        self.item_quantity=int(input('Enter the item quantity: '))


if __name__ == "__main__":
    # Type main section of code here

    buy1 = ItemToPurchase()

    print('Item 1')
    buy1.item_input()

    buy2 = ItemToPurchase()

    print ('\nItem 2')
    buy2.item_name=input('Enter the item name: ')
    buy2.item_price=float(input('Enter the item price: '))
    buy2.item_quantity=int(input('Enter the item quantity: '))

    print('TOTAL COST')
    buy1.print_item_cost()
    buy2.print_item_cost()
    print('Total: ${:.0f}'.format(buy1.item_price*buy1.item_quantity + buy2.item_price*buy2.item_quantity))