'''
# A shopping basket
# Add new items to the basket
# Remove items and list items
# When adding a new item into the basket the client must:
	a. The name;
	b. Quantity
# When removing Item the client must specify:
	a.The product name
# When listing all the basket products the list must show:
	a. The product name
	b. And a visible list

# Validations 
	a. Verify if the product name has a valid format
	b. If the product quantity is an number greater than 0
'''

class shopping_list():
	def __init__(self):
		self.items = []
		self.quantity = []

	# Adding new item into the shopping list
	def add_item(self, item, quantity):
		self.items.append(item)
		self.quantity.append(quantity)

	# Removing item from the shopping list
	def remove_item(self, item):
		item_index = self.items.index(item)
		self.items.pop(item_index)
		self.quantity.pop(item_index)