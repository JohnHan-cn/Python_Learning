import shelve

db = shelve.open('class-shelve')

for key in db:
	print(key, '=>\n', db[key])

record = db['bob']
print(record)
fields = record
print(fields)

db.close()
