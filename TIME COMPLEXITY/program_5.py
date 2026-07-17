
list_var = [10,20,30]

# access value at 2 position:
print(list_var[2])

# time complexity: O(1)

# search value from list

list_1 = [10,20,30,40,50]

search = 40

for i in range(0,len(list_1)):
    if search==list_1[i]:
        print(i)
        break
# time complexity: O(n)

# insert at begining

list_1.insert(0,99) # time complexity: O(n)

# insert at middle

list_1.insert(2,99) # time complexity: O(n)

print(list_1)