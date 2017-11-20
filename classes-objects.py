class Restaurant:

    def __init__(self,title,description):
        self.title = title
        self.description = description
        self.itemsOrdered = 0

    def print_description(self):
        print(self.title + self.description)

    def orderItem(self):
        self.itemsOrdered += 1

    def checkOutPurchase(self):
        print("We ordered " + str(self.itemsOrdered) + " item(s) today.")

aliceRestaurant = Restaurant("Alice's Restaurant: ","This song is about Alice, and her restaurant, but this restaurant's name is not Alice's Restaurant, that's what the song's called")
aliceRestaurant.print_description()
aliceRestaurant.orderItem()
aliceRestaurant.checkOutPurchase()
