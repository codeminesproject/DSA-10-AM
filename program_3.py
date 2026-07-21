
def addition(num):
    if num==11:
        return 1
    else:
        return num + addition(num+1)

result=addition(1)
print(result)