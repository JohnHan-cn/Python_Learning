"""
实现哟用来查看和更新保存在shelve中类实例的基于web的界面，
shelve保存在服务器上
"""

import cgi, shelve, sys, os        #cgi.test()转储输入
shelvename = 'class-shelve'
fieldnames = ('name','age','job','pay')


form = cgi.FieldStorage()
print('Context-type: text/html')

sys.path.insert(0, os.getcwd())


#主html模板
replyhtml = """
<html>
<title>People Input Form</title>
<body>
<form method=POST action="peoplecgi.py">
    <table>
    <tr><th>key <td><input type=text name=key value="%(key)s">
    $ROWS$
    </table>
    <p>
    <input type=submit value="Fetch", name=action>
    <input type=submit value="Update", name=action>
</form>
</body>
</html>
"""

#为$ROWS$的数据行插入html
rowhtml = '<tr><th>%s<td><input type=text name=%s value="%%(%s)s">\n'
rowshtml = ''
for fieldname in fieldnames:
    rowshtml += (rowhtml % ((fieldname,) * 3))
replyhtml = replyhtml.replace('$ROWS$', rowshtml)

def htmlize(adict):
    new = adict.copy()
    for field in fieldnames:
        value = new[field]
        new[field] = cgi.escape(repr(value))
    return new

def fetchRecord(db, form):
    """
    file = open('D:\Python_Learning\Python_Learning\class-shelve.txt', 'w')
    text = db['sue']['name']
    file.write(text)
    file.write('\n-------------\n')
    text = repr(print(form))
    file.write(text)
    file.close()
    """
    try:
        key = form['key'].value
        #print(key)
        record = db[key]
        #fields = db[key]
        #print(record)
        #fields = record.__dict__
        fields = record
        #print(fields)
        fields['key'] = key
    except:
        fields = dict.fromkeys(fieldnames, '?')
        fields['key'] = 'Missing or invalid key!'
    return fields
 

def updateRecord(db, form):
    if not 'key' in form:
        fields = dict.fromkeys(fieldnames, '?')
        fields['key'] = 'Missing key input!'
    else:
        key = form['key'].value
        if key in db:
            record = db[key]
        else:
            from person import Person
            record = Person(name='?',age='?')
        for field in fieldnames:
            file = open('class-shelve.txt', 'a')
            import time
            file.write(time.asctime())
            file.write('\n')
            file.write(form[field].value)
            file.write('\n')
            record[field] = eval(form[field].value)
            #setattr(record, record[field], eval(form[field].value))
            #setattr(record, field, form[field].value)
        db[key] = record
        #fields = record.__dict__
        fields = record
        fields['key'] = key
    return fields

"""
db = shelve.open('class-shelve')

for key in db:
	print(key, '=>\n', db[key])

db.close()


db = shelve.open(shelvename)
for key in db:
    print(key, '=>\n', db[key])
    print('hello word!\n')
print('hello word!\n')
"""
db = shelve.open(shelvename)
"""
print(db)
print('Hello Word!\n')
print(form)
print('---------------------\n')
fetchRecord(db, form)
for key in db:
	print(key, '=>\n', db[key])
"""
action = form['action'].value if 'action' in form else None
"""
file = open('class-shelve.txt', 'a')
import time
file.write(time.asctime())
file.write('\n')
file.write(form['action'].value)
file.write('\n')
file.write(form['key'].value)
file.write('\n')
file.write(form['name'].value)
file.write('\n')
file.write(form['age'].value)
file.write('\n')
file.write(form['job'].value)
file.write('\n')
file.write(form['pay'].value)
file.write('\n')
"""
if action == 'Fetch':
    fields = fetchRecord(db, form)
elif action == 'Update':
    fields = updateRecord(db, form)
else:
    fields = dict.fromkeys(fieldnames, '?')
    fields['key'] = 'Missing or invalid action!'
db.close()
#print(fields)
#fields = {'name':'Bob Smith', 'age':42, 'pay':30000, 'job':'dev'}
print(replyhtml % htmlize(fields))


    










