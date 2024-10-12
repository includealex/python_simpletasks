n_inputs = int(input())
input_dct = {}

for _ in range(n_inputs):
    values = [int(i) for i in input().split()]
    coord = values[0]
    mass = values[1]
    input_dct[coord] = mass

sorted_dct = {k: v for k, v in sorted(input_dct.items(), key=lambda item: item[1], reverse=True)}

for coord in sorted_dct:
    print(coord)

