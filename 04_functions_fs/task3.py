input_file = input()

count = {}
with open(input_file, 'r') as f:
    for line in f:
        for word in line.split():
            if word in count:
                count[word] += 1
            else:
                count[word] = 1

count = dict(sorted(count.items(), key=lambda x:x[0]))
sorted_count = dict(sorted(count.items(), key=lambda x:x[1], reverse=True))

for c,w in sorted_count.items():
    print(w, c)
