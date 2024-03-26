# ## for Loops
seq = [1,2,3,4,5]
for item in seq:
    print(item)

for item in seq:
    print('Yep')


for jelly in seq:
    print(jelly+jelly)


for x in range(10):
    if (x is 1):
        continue
    if (x > 5):
        break
    print(x)


for char in 'HADOOP ECHO SYSTEM':
 if  char == ' ' :
   break
 print (char, end=' ')
 if char == 'P':
   continue


# ## while Loops

i = 1
while i < 5:
    print('i is: {}'.format(i))
    i = i+1


x = 0
while (x < 10):
    print(x)
    x += 1


students = {'name': 'Sam', 'age':23 , 'major': 'cis','gpa':3.9}
while students:
    print(students.popitem())
print('Great')


students = {'name': 'Sam', 'age':23 , 'major': 'cis','gpa':3.9}
while len(students) > 4:
    print(students.popitem())
print('done.')



list1 = ['Apple', 'Banana', 'Orange', 'Cherry', 'Strawberry']
while list1:
    if len(list1) < 3:
           continue
    print(list1.pop())
print('Done.')



a = ['foo', 'bar', 'baz', 'qux', 'corge']
while a:
    if len(a) < 3:
           break
    print(a.pop())
print('Done.')


range(5)


for i in range(5):
    print(i)



list(range(5))


# ## list comprehension

x = [1,2,3,4]



out = []
for item in x:
    out.append(item**2)
print(out)
