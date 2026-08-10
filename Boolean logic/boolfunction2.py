
paths=[1, 2, 3, 4]
list2=[]

for path in paths:
    if path > 5:
        list2.append(path)

if list2:
    print(list2)
else:
    print("No paths available.")