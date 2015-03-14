arr = (2,7,4,90,5,45,78)
key = 8
flag = False
for val in arr:
    if val == key:
        flag = True
        break
if flag:
    print "Found"
else :
    print("Not found")
