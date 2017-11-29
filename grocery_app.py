class ShoppingList(object):
    def __init__(self,title,description):
        self.title = title
        self.description = description
        self.grocery_items = []

    def addItem(self,*args):
        self.args = args
        for arg in args:
            if arg not in self.grocery_items:
                self.grocery_items.append(arg)

    def printList(self):
        print "\b"
        print self.title + " list: " + self.description
        for grocery_item in self.grocery_items:
            print grocery_item.title
        print "\b"

class GroceryItem(object):
    def __init__(self,title):
        self.title = title

fiesta = ShoppingList('Fiesta','What to get at Fiesta Mart')
walmart = ShoppingList('Walmart','What to get at Walmart')
sams_club = ShoppingList("Sam's Club","What to get at Sam's Club")
costco = ShoppingList('Costco','What to get at Costco')
randalls = ShoppingList('Randalls','What to get at Randalls')

milk = GroceryItem('Milk')
soda = GroceryItem('Soda')
fish = GroceryItem('Fish')
paper = GroceryItem('Paper')
napkins = GroceryItem('Napkins')
plate = GroceryItem('Plate')
chips = GroceryItem('Chips')
beef = GroceryItem('Beef')
eggs = GroceryItem('Eggs')
sugar = GroceryItem('Sugar')
salt = GroceryItem('Salt')
pepper = GroceryItem('Pepper')
honey = GroceryItem('Honey')
tv = GroceryItem('Television')
computer = GroceryItem('Computer')


fiesta.addItem(milk,soda,fish)
walmart.addItem(paper,napkins,plate,chips)
sams_club.addItem(beef,eggs,sugar,salt,pepper,honey)
costco.addItem(tv,computer)

fiesta.printList()
walmart.printList()
sams_club.printList()
costco.printList()
