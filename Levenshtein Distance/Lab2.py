
def levenshtein_distance(str1, str2):
    len_str1 = len(str1) + 1
    len_str2 = len(str2) + 1

    matrix = [[0 for n in range(len_str2)] for m in range(len_str1)]

    for i in range(len_str1):
        matrix[i][0] = i
    for j in range(len_str2):
        matrix[0][j] = j

    for i in range(1, len_str1):
        for j in range(1, len_str2):
            if str1[i - 1] == str2[j - 1]:
                S = 0 
            else: 
                S = 1
            matrix[i][j] = min(
                matrix[i - 1][j] + 1,
                matrix[i][j - 1] + 1,
                matrix[i - 1][j - 1] + S
            )

    return matrix[len_str1 - 1][len_str2 - 1]

word1 = "топот"
word2 = "грохот"
distance = levenshtein_distance(word1, word2)
print(f"Расстояние Левенштейна между '{word1}' и '{word2}': {distance}")
