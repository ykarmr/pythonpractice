matrix=[
    [1,2,3,4],
    [5,6,7,8],
    [9,10,11,12]
]
print(matrix)

print([[row[i] for row in matrix]for i in range(4)])

#zip関数　行列のイメージ　zip('ABCD','xy') -> Ax,By
print(list(zip(*matrix)))
