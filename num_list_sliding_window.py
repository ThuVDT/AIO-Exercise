num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
k = 3
output = []


for i in range(0, len(num_list)):
    sliding_window = []
    if i + k <= len(num_list):
        for j in range(i, i + k):
            sliding_window.append(num_list[j])
        max_val = max(sliding_window)
        output.append(max_val)

print(output)
