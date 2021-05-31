M1 = [[1, 2, 3],
      [4, 5, 6],
      [7, 8, 9]]

M2 = [[13, 16, -2],
      [5, 7, -14],
      [-2, 5, 3]]

M3 = [[0, 0, 0],
      [0, 0, 0],
      [0, 0, 0]]

matrix_length = len(M1)

for i in range(len(M1)):
    for k in range(len(M2)):
        M3[i][k] = M1[i][k] * M2[i][k]

print("The multiplication of Matrix M1 and M2 = ", M3)
