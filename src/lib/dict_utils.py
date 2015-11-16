def key_exists(data, key):
	if key in data:
		return True
	else:
		return False

def get_key(data, key):
	if key_exists(data, key):
		return data[key]
	else:
		raise RuntimeError("Key does not exist")