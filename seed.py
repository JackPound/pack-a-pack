from .models import Item


items = [
	['blanket', 7],
	['book(large)', 2],
	['book(small)', 1],
	['compass', 1],
	['conditioner', 1],
	['deoderant', 1],
	['hackeysack', 1],
	['jacket', 5],
	['laptop', 6],
	['lighter', 1],
	['misc tools', 1],
	['pants', 4],
	['pocket knife', 1],
	['razor', 1],
	['shampoo', 1],
	['shirt', 4],
	['shoes', 5],
	['snacks(large)', 2],
	['snacks(small)', 1],
	['socks', 1],
	['souvenir', 1],
	['tablet', 2],
	['toilet paper', 2],
	['towel', 2],
	['underwear', 1],
	['water bottle', 1]	
]

def create_entry(to_list):
	for thing in to_list:
		n = thing[0]
		s = thing[1]
		new_item = Item.objects.create(name= n, size = s, category = 'misc')
# create_entry(items)