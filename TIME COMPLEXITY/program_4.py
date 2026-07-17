
list_var = []

while True:
    val = int(input("Please enter value: "))
    list_var.append(val)

    isContinue = input("Press Y to continue: ")
    if isContinue!="Y":
        break

# Time Complexity: O(n)
# space complexity: O(n)

print(list_var)
# Time Complexity: O(1)