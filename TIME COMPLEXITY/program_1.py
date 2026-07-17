
# calculate time complexity of list:

list_var = [10,20,30]

# Time Complexity: O(1)

print("------------------------------------------------------")

list_var = []

while True:
    val = int(input("Please enter value: "))
    list_var.append(val)

    isContinue = input("Press Y to continue: ")
    if isContinue!="Y":
        break

# Time Complexity: O(n)