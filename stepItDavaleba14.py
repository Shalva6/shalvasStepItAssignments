cartStuff = {}
class shoppingCart:
    def addItem(self, itemToAdd, amountToAdd):
        self.itemToAdd = itemToAdd
        self.amountToAdd = amountToAdd
        cartStuff[self.itemToAdd] = self.amountToAdd

    def removeItem(self, itemToRemove):
        self.itemToRemove = itemToRemove
        if self.itemToRemove in cartStuff:
            cartStuff.pop(self.itemToRemove)
    
    def count(self):
        count = 0
        for value in cartStuff.values():
            count += value
        return f"There are {count} items in the cart"
    
    def currentItems(self):
        listOfItems = []
        for keys, values in cartStuff.items():
            listOfItems.append(f"There is an {values} amount of {keys} in the cart")
        return listOfItems
        
cart = shoppingCart()
cart.addItem("პური", 2)
cart.addItem("კარაქი", 1)
cart.addItem("წყალი", 6)
cart.addItem("ზეთი", 2)
print(cart.currentItems())
print(cart.count())

cart.removeItem("ზეთი")
print(cart.currentItems())
print(cart.count())