head = {} #root node


def add(word):
	cur = head;
	for ch in word:
		if ch not in cur:
			cur[ch] = {} #starting to create nodes
		cur = cur[ch]
	cur['*'] = True
	
	
def search(word):
	cur = head;
	for ch in word:
		if ch not in cur:
			return False
		cur = cur[ch]
	if '*' in cur:
		return True
	else:
		return False
		
		
add('hello')
add('hella')
add('helicopter')
print(search('hello'))
print(search('hellay'))
