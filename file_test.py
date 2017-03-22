import sys, shelve

shelvename = 'class-shelve'
db = shelve.open(shelvename)
file = open('class-shelve.txt', 'w')
text = db['sue']['name']
file.write(text)

file.close()
db.close()
