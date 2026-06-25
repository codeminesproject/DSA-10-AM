
# prepare queue using list:

queue_var = []

print("---------- add first value 10 -----------")
queue_var.append(10)
print("value after adding 10:",queue_var)

print("---------- add first value 20 -----------")
queue_var.append(20)
print("value after adding 20:",queue_var)

print("---------- add first value 30 -----------")
queue_var.append(30)
print("value after adding 30:",queue_var)

print("----- remove value at first position ---------")

queue_var_1 = queue_var
for i in range(0,len(queue_var)):
    print(queue_var_1.pop(0))
    print("after removing at 0 position:",queue_var_1)
