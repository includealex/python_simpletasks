num_str = input()
arr = num_str.split('')
arr.sort()

idx = 0
while (arr[idx] == 0):
    idx += 1

arr.insert(0, arr.pop(idx))

res_str = ""
for el in arr:
    res_str += str(el)

print(res_str)

