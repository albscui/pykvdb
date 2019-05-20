# pykvdb

A key-value datastore implemented in Python with b-tree.

## Example

```python
from pykvdb.kv import KV

db = KV(int)
data = {1: "hello", 2: "world", 3: "lorem", 4: "ipsum"}
for key, value in data.items():
    db.set(key, value)

print(db.range_query([1,3]))

db.save("kv_example")
db2 = KV.load("kv_example")

print(db2.range_query([1,3]))

more_data = {
    5: "Python",
    6: "is",
    7: "awesome!"
}
db2.load_from_dict(more_data)
print(db2.range_query([4,8]))
print(db2.get(5))
```

## TODO

- Enhance the API by making it more "Pythonic" using special methods for set and get
- Use a different serializer so that we can use different versions of Python (maybe JSON?)
- Add a `delete` method that can remove nodes from the kv store
- Save out to multiple files using the keys as pointers to files for bigger databases
- Implement the kv store on top of a B+Tree, another variant of the b-tree family of data structures
