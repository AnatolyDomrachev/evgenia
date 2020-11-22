 
 a[{'name': 'vasya', 'age': 20}, {'name': 'petya', 'age': 30}]
 
 
 f=open('123', 'w')
 
 f.write(json.dumps(a))
60 
 f.close()
 
 
 f=open('123', 'r')
 
 b=json.loads(f.read())
 
 
 f.close()
 
 b[{'name': 'vasya', 'age': 20}, {'name': 'petya', 'age': 30}]
 
 
 
 a2{'name': 'petya', 'age': 30}
 
 
 a2.
a2.clear(       a2.fromkeys(    a2.items(       a2.pop(         a2.setdefault(  a2.values(      
a2.copy(        a2.get(         a2.keys(        a2.popitem(     a2.update(      
 a2['group'] = 'mlp'
 
 a2{'name': 'petya', 'age': 30, 'group': 'mlp'}
 
 
 
 for x in a2:
...  x... 
'name'
'age'
'group'
 

