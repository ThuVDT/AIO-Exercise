def levenshtein_distance(source, target):
    matrix = []
    for _ in range(len(source) + 1):
        row = []
        for _ in range(len(target) + 1):
            row.append(0)
        matrix.append(row)

    for i in range(len(target) + 1):
        matrix[0][i] = i

    for i in range(len(source) + 1):
        matrix[i][0] = i

    for i in range(len(source)):
        for j in range(len(target)):
            if source[i] == target[j]:
                matrix[i+1][j+1] = matrix[i][j]
            else:
                val_1 = matrix[i][j]
                val_2 = matrix[i+1][j]
                val_3 = matrix[i][j+1]
                matrix[i+1][j+1] = min(val_1, val_2, val_3) + 1
    print(matrix[len(source)][len(target)])


levenshtein_distance('kitten', 'sitting')
