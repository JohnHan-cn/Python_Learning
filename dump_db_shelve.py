import shelve
bob = {'name':'Bob Smith', 'age':42, 'pay':30000, 'job':'dev'}
sue = {'name':'Sue Jones', 'age':45, 'pay':40000, 'job':'hdw'}
tom = {'name':'Tom', 'age':50, 'pay':0, 'job':None}
db = shelve.open('class-shelve')
db['bob'] = bob
db['sue'] = sue
db['tom'] = tom

for key in db:
	print(key, '=>\n', db[key])
print(db['sue']['name'])
db.close()
