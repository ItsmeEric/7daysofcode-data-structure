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

class ShoppingList():
	def __init__(self):
		self.items = []
		self.quantities = []

	# Adding new item into the shopping list
	def add_item(self, item, quantity):
		if self.validate_product_name(item) and self.validate_quantity(quantity):
			self.items.append(item)
			self.quantities.append(quantity)
		else:
			print("Invalid item or quantity")

	# Removing item from the shopping list
	def remove_item(self, item):
		if item in self.items:
			item_index = self.items.index(item)
			self.items.pop(item_index)
			self.quantities.pop(item_index)
		else:
			print("Item not found in the shopping list.")

	# Listing all items in the basket
	def list_items(self):
		print("Shopping list")
		for i in range(len(self.items)):
			print(f"{self.items[i]}: {self.quantities[i]}")

	# Validate the product format
	def _validate_product_name(self, item):
		if item.isalnum() or ' ' in item:
			return True
		print("Invalid product name format")
		return False
	
	# Validate product quantity
	def _validate_quantity(self, quantity):
		if isinstance(quantity, int) and quantity > 0:
			return True
		print("Invalid quantity format")
		return False
	

shopping_list = ShoppingList()

shopping_list.add_item('Bread', 1)
shopping_list.add_item('Banana', 5)
shopping_list.add_item('Cookies', 2)
shopping_list.add_item('Melon', 1)

shopping_list.list_items()

shopping_list.remove_item('Cookies')

shopping_list.list_items()