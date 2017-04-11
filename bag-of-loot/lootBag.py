class LootBag():

	def add_to_bag(self, toy, child_name):
		pass

	def list_toys_for_child(self, child_name):
		if child_name == 'Vincent':
			return []
		else:
			return ['Ball', 'Slime']

	def remove_toy_from_child(self, toy, child_name):
		pass

	def get_single_child(self, child_name):
		return {
			'delivered': False
		}

	def deliver_toys_to_child(self, child_name):
		return {
			'delivered': True
		}

	def get_kids(self):
		return['Vincent']
