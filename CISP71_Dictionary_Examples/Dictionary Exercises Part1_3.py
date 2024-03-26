#Reference https://www.w3resource.com/python-exercises/dictionary/
#8. Write a Python script to merge two Python dictionaries
d1 = {'a': 100, 'b': 200}
d2 = {'x': 300, 'y': 200}
d = d1.copy()
print("before merging d is")
print(d)
print("after merging d is")
d.update(d2)
print(d)
