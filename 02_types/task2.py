
start_sum = float(input())
final_sum = float(input())
procent = float(input())

counter = 0

while (start_sum < final_sum):
    start_sum *= (1 + procent/100)
    counter += 1

print(counter)
