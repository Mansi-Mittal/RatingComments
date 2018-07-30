class HashMap:
	def __init__(self):
		self.size = 6
		self.map = [None] * self.size
		
	def _get_hash(self, key):
		hash = 0
		for char in str(key):
			hash += ord(char)
		return hash % self.size
		
	def add(self, key, value):
		key_hash = self._get_hash(key)
		key_value = [key, value]
		
		if self.map[key_hash] is None:
			self.map[key_hash] = list([key_value])
			return True
		else:
			for pair in self.map[key_hash]:
				if pair[0] == key:
					pair[1] = value
					return True
			self.map[key_hash].append(key_value)
			return True
			
	def get(self, key):
		key_hash = self._get_hash(key)
		if self.map[key_hash] is not None:
			for pair in self.map[key_hash]:
				if pair[0] == key:
					return pair[1]
		return None
			
	
				
h = HashMap()
h.add('slapped', 'true')
h.add('slap', 'true')
h.add('hate', 'true')
h.add('blood', 'true')
h.add('shoot', 'true')
h.add('kill', 'true')
h.add('killed', 'true')
h.add('killing', 'true')
h.add('dead', 'true')
h.add('death', 'true')
h.add('saala', 'true')
h.add('pussy', 'true')
h.add('bitch', 'true')
h.add('bastard', 'true')
h.add('shag', 'true')
h.add('faggot', 'true')
h.add('cock', 'true')
h.add('dipshit', 'true')
h.add('fuck', 'true')
h.add('chuda', 'true')
h.add('bsdk', 'true')
h.add('bhosadike', 'true')
h.add('gaand', 'true')
h.add('gand', 'true')
h.add('chutiya', 'true')
h.add('stupid', 'true')
h.add('asses', 'true')
h.add('asshole', 'true')
h.add('boob', 'true')
h.add('boobs', 'true')
h.add('cunt', 'true')
h.add('fuckk', 'true')
h.add('shit', 'true')
h.add('chutiye', 'true')
h.add('dog', 'true')
h.add('kutte', 'true')
h.add('kutta', 'true')
h.add('piss', 'true')
h.add('sex', 'true')
h.add('sexy', 'true')
h.add('nanga', 'true')
h.add('nangi', 'true')
h.add('bhenchod', 'true')
h.add('behnchodd', 'true')
h.add('behnnchod', 'true')
h.add('bhenchhod', 'true')
h.add('madarchhod', 'true')
h.add('madarchodd', 'true')
h.add('madarchod', 'true')
h.add('randi', 'true')
h.add('anarchist', 'true')
h.add('ape', 'true')
h.add('arse', 'true')
h.add('arselicker', 'true')
h.add('butthead', 'true')
h.add('doofus', 'true')
h.add('dickhead', 'true')
h.add('dick', 'true')
h.add('gangster', 'true')
h.add('terrorist', 'true')
h.add('motherfucker', 'true')
h.add('MILF', 'true')
h.add('milf', 'true')
h.add('freak', 'true')
h.add('pig', 'true')
h.add('retard', 'true')
h.add('son of a bitch', 'true')
h.add('swine', 'true')
h.add('idiot', 'true')
h.add('chut', 'true')
h.add('choot', 'true')
h.add('chutt', 'true')
		
