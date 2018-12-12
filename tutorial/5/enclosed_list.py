vec=[-4,-2,0,2,4]
print([x*2 for x in vec])

print([x for x in vec if x >= 0])

#abs絶対値
print([abs(x) for x in vec])
print([abs(x) for x in vec if x >= 0])

print([(x,x**2) for x in range(6)])
